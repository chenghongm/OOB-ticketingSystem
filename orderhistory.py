from anvil import *
import anvil.server
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class orderhistory(orderhistoryTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.items = app_tables.order.search()
    # Any code you write here will run when the form opens.

 

  def button_6_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Query')

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('userAccount')

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Passenger')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('contact')

  def button_7_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    items = app_tables.order.search()
    #print('call-m')
    m = anvil.server.call('downloadOrder',items)
    #print('m,called!')
    m=BlobMedia('text/html', m,name='my_order.html')
    
    download(m)

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('credit')

  def label_1_show(self, **event_args):
    """This method is called when the Label is shown on the screen"""
    user = anvil.users.get_user()
    if user is not None:
      self.label_1.text = 'Welcome, '+ user['email']

  def button_8_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('printOrder')
    #print('print done!')
    alert(content=anvil.server.call('readFile'),large=True)

  def button_9_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.logout()
    open_form('Query')









