from anvil import *
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Admin(AdminTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #anvil.users.login_with_form()
    self.repeating_panel_user.items =app_tables.users.search()
    self.repeating_panel_1.items = app_tables.message.search()
  
    # Any code you write here will run when the form opens.

  def button_adLogout_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.logout()
    open_form('Query')
    
  def update_penal(self):
    self.repeating_panel_1.items = app_tables.message.search()
    

