from anvil import *
import anvil.server
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RowTemplate10(RowTemplate10Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def check_box_1_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    
    if event_args['sender'].checked:
      reply_message = self.text_box_1.text
      to_adr = self.label_1.text
      anvil.server.call('replyEmail',to_adr,reply_message)
      alert('You sent out an email to  ' + to_adr)
      self.check_box_1.enabled = False
      #self.text_box_1.enabled = False
      

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass


