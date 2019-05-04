from anvil import *
import stripe.checkout
import anvil.server
import tables
from tables import app_tables
import google.auth, google.drive
from google.drive import app_files
import anvil.users

class SignupDialog (SignupDialogTemplate):
  def __init__(self, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def focus_email(self, **kws):
     """Focus on the email box."""
     self.email_box.focus()

  def focus_password(self, **kws):
    """Focus on the password box."""
    self.password_box.focus()

  def focus_password_repeat(self, **kws):
    """Focus on the password repeat box."""
    self.password_repeat_box.focus()

  def close_alert(self, **kws):
    """Close any alert we might be in with True value."""
    self.raise_event('x-close-alert', value=True)
