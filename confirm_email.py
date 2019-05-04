import tables
from tables import app_tables
import google.auth, google.drive, google.mail
from google.drive import app_files
import anvil.users
import anvil.server
from anvil.http import url_encode
import bcrypt
from random import SystemRandom
from anvil import *
import anvil.stripe
random = SystemRandom()


def mk_token():
  """Generate a random 14-character token"""
  return "".join([random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789") for i in range(14)])

@anvil.server.callable
def _send_password_reset(email):
  """Send a password reset email to the specified user"""
  user = app_tables.users.get(email=email)
  if user is not None:
    user['link_key'] = mk_token()
    google.mail.send(to=user['email'], subject="Reset your password", text="""
Hi,

Someone has requested a password reset for your account. If this wasn't you, just delete this email.
If you do want to reset your password, click here:

%s#?email=%s&pwreset=%s

Thanks!
""" % (anvil.server.get_app_origin('published'), url_encode(user['email']), url_encode(user['link_key'])))
    return True


@anvil.server.callable
def _send_email_confirm_link(email):
  """Send an email confirmation link if the specified user's email is not yet confirmed"""
  user = app_tables.users.get(email=email)
  if user is not None and not user['confirmed_email']:
    if user['link_key'] is None:
      user['link_key'] = mk_token()
    anvil.google.mail.send(to=user['email'], subject="Confirm your email address", text="""
Hi,

Thanks for signing up for our service. To complete your sign-up, click here to confirm your email address:

%s#?email=%s&confirm=%s

Thanks!
""" % (anvil.server.get_app_origin('published'), url_encode(user['email']), url_encode(user['link_key'])))
    return True


def hash_password(password, salt):
  """Hash the password using bcrypt in a way that is compatible with Python 2 and 3."""
  if not isinstance(password, bytes):
    password = password.encode()
  if not isinstance(salt, bytes):
    salt = salt.encode()

  result = bcrypt.hashpw(password, salt)

  if isinstance(result, bytes):
    return result.decode('utf-8')


@anvil.server.callable
def _do_signup(email, name, password):
  if name is None or name.strip() == "":
    return "Must supply a name"
  
  pwhash = hash_password(password, bcrypt.gensalt())

  # Add the user in a transaction, to make sure there is only ever one user in this database
  # with this email address. The transaction might retry or abort, so wait until after it's
  # done before sending the email.

  @tables.in_transaction
  def add_user_if_missing():
    user = app_tables.users.get(email=email)
    if user is None:
      user = app_tables.users.add_row(email=email, enabled=True, password_hash=pwhash)
      return user
    
  user = add_user_if_missing()

  if user is None:
    return "This email address has already been registered for our service. Try logging in."
  
  _send_email_confirm_link(email)
  
  # No error = success
  return None
  
    
def get_user_if_key_correct(email, link_key):
  user = app_tables.users.get(email=email)

  if user is not None and user['link_key'] is not None:
    # Use bcrypt to hash the link key and compare the hashed version.
    # The naive way (link_key == user['link_key']) would expose a timing vulnerability.
    salt = bcrypt.gensalt()
    if hash_password(link_key, salt) == hash_password(user['link_key'], salt):
      return user


@anvil.server.callable
def _is_password_key_correct(email, link_key):
  return get_user_if_key_correct(email, link_key) is not None

@anvil.server.callable
def _perform_password_reset(email, reset_key, new_password):
  """Perform a password reset if the key matches; return True if it did."""
  user = get_user_if_key_correct(email, reset_key)
  if user is not None:
    user['password_hash'] = hash_password(new_password, bcrypt.gensalt())
    user['link_key'] = None
    anvil.users.force_login(user)
    return True
    
@anvil.server.callable
def _confirm_email_address(email, confirm_key):
  """Confirm a user's email address if the key matches; return True if it did."""
  user = get_user_if_key_correct(email, confirm_key)
  if user is not None:
    user['confirmed_email'] = True
    user['link_key'] = None
    anvil.users.force_login(user)
    return True
''' 
@anvil.server.callable 
def do_email_confirm_or_reset():
  """Check whether the user has arrived from an email-confirmation link or a password reset, and pop up any necessary dialogs.
     Call this function from the 'show' event on your startup form.
  """
  h = anvil.get_url_hash()
  
  if 'confirm' in h:
      if anvil.server.call('_confirm_email_address', h['email'], h['confirm']):
        anvil.alert("Thanks for confirming your email address. You are now logged in.")
      else:
        anvil.alert("This confirmation link is not valid. Perhaps you have already confirmed your address?\n\nTry logging in normally.")
'''