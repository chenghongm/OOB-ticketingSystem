from anvil import *
import anvil.server
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import date


class contact(contactTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def label_11_show(self, **event_args):
    """This method is called when the Label is shown on the screen"""
    user = anvil.users.get_user()
    if user is not None:
      self.label_11.text = 'Welcome, '+ user['email']

  
    

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Order')

  def label_greet_show(self, **event_args):
    """This method is called when the Label is shown on the screen"""
    
    user = anvil.users.get_user()
    self.label_greet.text = 'Hi, '+ user['email'] + ', thank you for contacting us, please select your question catagory.'

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    user = anvil.users.get_user()
    from_adr = user['email']
    subjet = self.drop_down_1.selected_value
    content = self.text_area_1.text
    date_sub = str(date.today())
    app_tables.message.add_row(text=content,
                               from_address=from_adr,
                               subject=subjet,
                               when=date_sub,
                               supporting_doc=self.file_loader_1.file)
    alert('Thank you, we will come back to you shortly!')

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('userAccount')

  def button_6_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Passenger')

  def button_7_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Query')

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('credit')

  def button_8_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.logout()
    open_form('Query')
    









