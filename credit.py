from anvil import *
import anvil.server
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables



class credit(creditTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run when the form opens.

  def label_11_show(self, **event_args):
    """This method is called when the Label is shown on the screen"""
    user = anvil.users.get_user()
    if user is not None:
      self.label_11.text = 'Welcome, '+ user['email']

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Query')

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('userAccount')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('orderhistory')

  def button_6_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Passenger')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('contact')

  def text_box_1_show(self, **event_args):
    """This method is called when the TextBox is shown on the screen"""
    user = anvil.users.get_user()
    self.text_box_1.text = user['Credit']
    

  def button_7_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.logout()
    
    open_form('Query')
    









