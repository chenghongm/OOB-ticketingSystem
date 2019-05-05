from anvil import *
import anvil.server
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import pagestack
from RowTemplate9 import RowTemplate9

class placeorder(placeorderTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.items = app_tables.order_tmp2.search()
    
    
    # Any code you write here will run when the form opens.

 
  def form_show(self, **event_args):
    """This method is called when the column panel is shown on the screen"""
    pagestack.pageL.append('placeorder')
    print(pagestack.pageL)
    if pagestack.pageL[len(pagestack.pageL)-2]=="placeorder":
       pagestack.pageL.pop()
        
  def update_penal(self):
    self.repeating_panel_1.items = app_tables.order_tmp2.search()

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('userAccount')

  def button_back_click(self, **event_args):
    """This method is called when the button is clicked"""
    pagestack.pageL.pop()
    #print(pagestack.pageL)
    form = pagestack.pageL[len(pagestack.pageL)-1]
    open_form(form)

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    user = anvil.users.get_user()
    items = pagestack.payOrder
    user['Credit'] = user['Credit']+len(items)
   
    print('credit added!')
    RowTemplate9().storeData(items)
    app_tables.order_tmp2.delete_all_rows()
    self.repeating_panel_1.items = app_tables.order_tmp2.search()
    RowTemplate9().drop_down_1.items = []
    alert('Thanks for ticketing with us!')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.logout()
    pagestack.clear()
    app_tables.order_tmp2.delete_all_rows()
    self.repeating_panel_1.items = app_tables.order_tmp2.search()
    open_form('Query')

  def label_1_show(self, **event_args):
    """This method is called when the Label is shown on the screen"""
    user = anvil.users.get_user()
    self.label_1.text = 'Welcome, ' + user['email']
   

  


  