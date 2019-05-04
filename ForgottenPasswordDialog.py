from anvil import *
import stripe.checkout
import tables
from tables import app_tables
import anvil.server
import google.auth, google.drive
from google.drive import app_files
import anvil.users

class ForgottenPasswordDialog (ForgottenPasswordDialogTemplate):
  def __init__(self, email=None, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    if email is not None:
      self.email_box.text = email

  def close_alert(self, **kws):
    """Close any alert we might be in with True value."""
    self.raise_event('x-close-alert', value=True)
