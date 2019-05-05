from anvil import *
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.email

class RowTemplate3(RowTemplate3Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def check_box_enable_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if event_args['sender'].checked:
      
      to_adr = self.label_1.text
      anvil.server.call('noticeEmail',to_adr)

  

