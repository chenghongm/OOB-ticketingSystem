from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class userAccount(userAccountTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    user = anvil.users.get_user()
    self.box_f.text = user['First_Name']
    self.box_l.text = user['Last_Name']
    self.box_email.text = user['email']
    self.box_phone.text = user['Phone']
   
    # Any code you write here will run when the form opens.

 
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('orderhistory')

 

  def button_reset_click(self, **event_args):
    """This method is called when the button is clicked"""
    user = anvil.users.get_user()
    
    anvil.users.send_password_reset_email(user['email'])
    alert('Your reset eamil has sent out, please check your email! Thanks!')
    anvil.users.logout()
  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Query')

  def button_6_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Passenger')

  def button_update_click(self, **event_args):
    """This method is called when the button is clicked"""
    user = anvil.users.get_user()
    user['Valid_Document'] = self.file_loader_1.file
    alert('Your file is updated!')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('contact')

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('credit')

  def label_11_show(self, **event_args):
    """This method is called when the Label is shown on the screen"""
    user = anvil.users.get_user()
    if user is not None:
      self.label_11.text = 'Welcome, '+ user['email']

  def button_7_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.logout()
    open_form('Query')












  


  
  


