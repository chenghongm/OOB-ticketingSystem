from anvil import *
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import pagestack

class Order(OrderTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    
    self.init_components(**properties)
    self.repeating_panel_1.items = app_tables.order_tmp.search()
    
    print('order-tmp ready')
    app_tables.hold_order.delete_all_rows()
    self.repeating_panel_2.items = app_tables.hold_order.search()
    
  def radio_button_2_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    pass

  def logoutB_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.logout()
    pagestack.clear()
    open_form('Query')

  def update_penal(self):
    self.repeating_panel_1.items = app_tables.order_tmp.search()
    
 
  def button_placeorder_click(self, **event_args):
    """This method is called when the button is clicked"""
    app_tables.order_tmp.delete_all_rows()
   
    items = pagestack.orderL
    #userL = list(app_tables.users.search())
    #userID = anvil.server.call('get_userID',userL)
    user = anvil.users.get_user()
    userID = user['UserID']
    print(userID)
    for item in items:
       trip = item[0]
       uID = userID
       orderID = anvil.server.call('gen_orderID',userID)
       app_tables.order_tmp2.add_row(OrderID=orderID,Trip=trip,UserID=uID)
    
    open_form('placeorder')

  def button_hold_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
  def update_penal2(self):
    self.repeating_panel_2.items = app_tables.hold_order.search()
    
    

  def button_4_copy_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('userAccount')

  def form_show(self, **event_args):
    """This method is called when the column panel is shown on the screen"""
    user = anvil.users.get_user()    
    self.label_status.text = 'Welcome, '+user['email']
    
    pagestack.pageL.append('Order')
    print(pagestack.pageL)
    if pagestack.pageL[len(pagestack.pageL)-2]=='Order':
      pagestack.pageL.pop()
    print(len(pagestack.pageL))
    
  def label_status_show(self, **event_args):
    """This method is called when the Label is shown on the screen"""
    user = anvil.users.get_user()
    if user is None:
      self.label_loginstatus.text = 'Welcome,Tourist!'
      self.link_go2useraccount.visible = False
      
    else:
      self.label_status.text = 'Welcome, '+ user['email']
      self.link_go2useraccount.visible = True
     

  def link_go2useraccount_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('userAccount')

  def button_back_click(self, **event_args):
    """This method is called when the button is clicked"""
    pagestack.pageL.pop()
    print(pagestack.pageL)
    form = pagestack.pageL[len(pagestack.pageL)-1]
    open_form(form)

  
 







