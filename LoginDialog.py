from anvil import *
import stripe.checkout
import tables
from tables import app_tables
import anvil.server
import google.auth, google.drive
from google.drive import app_files
import anvil.users

class LoginDialog (LoginDialogTemplate):
  def __init__(self, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def confirm_lnk_click (self, **event_args):
    """Close any alert we might be in with 'confirm_email' value."""
    self.raise_event('x-close-alert', value='confirm_email')

  def reset_pw_link_click (self, **event_args):
    """Close any alert we might be in with 'reset_password' value."""
    self.raise_event('x-close-alert', value='reset_password')

  def focus_password(self, **kws):
     """Focus on the password box."""
     self.password_box.focus()

  def close_alert(self, **kws):
     """Close any alert we might be in with 'login' value."""
     self.raise_event('x-close-alert', value='login')

  

