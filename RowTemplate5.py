from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from RowTemplate4 import RowTemplate4
import pagestack

class RowTemplate5(RowTemplate5Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run when the form opens.

  
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    RowTemplate4().killTask()
    
    print('killed')
    
    trip = self.label_2.text
    for item in pagestack.orderL:
            itemL = list(item)
            if itemL[0] ==trip:
               itemL[1] = int(itemL[1])+1
              
    if int(self.label_amount.text)>1:
      row_hold = app_tables.hold_order.get(Trip=trip)
      #print(self.label_amount.text)
      self.label_amount.text= str(int(self.label_amount.text)-1 )
      row_hold['index'] =self.label_amount.text
      #print(self.label_amount.text)
      get_open_form().update_penal2()  
      #print(row_hold['intex'])
      row = app_tables.order_tmp.get(Trip=trip)
      if row:
        row = app_tables.order_tmp.get(Trip=trip)
        row_index= int( app_tables.order_tmp.get(Trip=trip)['index'])+1 
        row['index'] = str(row_index)
        print(row['intex'])
        get_open_form().update_penal()
         
       
      else:
        
        app_tables.order_tmp.add_row(Trip=trip,index='1')
        get_open_form().update_penal()
      
        
    elif int(self.label_amount.text)==1:
      row_hold = app_tables.hold_order.get(Trip=trip)
      row_hold.delete()
      get_open_form().update_penal2()
      row = app_tables.order_tmp.get(Trip=self.label_2.text)
      if row:
        row = app_tables.order_tmp.get(Trip=self.label_2.text)
        row_index= int( app_tables.order_tmp.get(Trip=trip)['index'])+1 
        row['index'] = str(row_index)
        print(row['index'])
        get_open_form().update_penal()
      else:
       
        app_tables.order_tmp.add_row(Trip=trip,index='1')
        get_open_form().update_penal()
        
       
        
       
      
    
    
    

  def form_show(self, **event_args):
    """This method is called when the data row panel is shown on the screen"""
    pass 


