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
#from RowTemplate5 import RowTemplate5

class RowTemplate4(RowTemplate4Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    trip = self.label_2.text 
    anvil.server.call('removeOrder',trip)
    get_open_form().update_penal()
    
  
    
  def killTask(self):
    anvil.server.call('endHoldtime')

  def check_box_hold_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    
    
    if event_args['sender'].checked:
      
      if len(str(self.text_box_1.text)) !=0:
          
          trip = self.label_2.text
          for item in pagestack.orderL:
            itemL = list(item)
            if itemL[0] ==trip:
               itemL[1] = int(itemL[1])-1
          tmp_order = app_tables.order_tmp.get(Trip=trip)
          if int(self.text_box_1.text) >1:
              self.text_box_1.text = int(self.text_box_1.text)-1
              tmp_order['index'] = self.text_box_1.text
              get_open_form().update_penal()
              print('update')
              self.check_box_hold.enabled = True
              print('enabled')
              
              
              row = app_tables.hold_order.get(Trip=trip)
              if row:
                  hold_index = int(app_tables.hold_order.get(Trip=trip)['index'])+1
                  print('hold index is: ',app_tables.hold_order.get(Trip=trip)['index'])
                  row['index']=str(hold_index)
                  get_open_form().update_penal2()
                  label = self.label_2.text
                  task = anvil.server.call('holdtime',label, trip)
              else:
                 app_tables.hold_order.add_row(Trip=trip,index='1')
                 get_open_form().update_penal2()
                 #anvil.server.call('removeOrder',trip)#delete data from order_tmp
                 #get_open_form().update_penal()
                 label = self.label_2.text
                 task = anvil.server.call('holdtime',label, trip)
              
              
              
          elif int(self.text_box_1.text)==1:
              self.text_box_1.text = int(self.text_box_1.text)-1
              tmp_order['index'] = self.text_box_1.text
              get_open_form().update_penal()
              
              self.check_box_hold.enabled = False   
              row = app_tables.hold_order.get(Trip=trip)
              if row:
                  hold_index = int(app_tables.hold_order.get(Trip=trip)['index'])+1
                  print('hold index is: ',app_tables.hold_order.get(Trip=trip)['index'])
                  row['index']=str(hold_index)
                  get_open_form().update_penal2()
                  anvil.server.call('removeOrder',trip)#delete data from order_tmp
                  get_open_form().update_penal()
              
                  label = self.label_2.text
                  task = anvil.server.call('holdtime',label, trip)
              else:
                  app_tables.hold_order.add_row(Trip=trip,index='1')
                  get_open_form().update_penal2()
                  anvil.server.call('removeOrder',trip)#delete data from order_tmp
                  get_open_form().update_penal()
                  
                  label = self.label_2.text
                  task = anvil.server.call('holdtime',label, trip)
      else:
        alert('Amount is requried!')
        self.check_box_hold.enabled = False
          
      
          
          
      
      
     
      
  
      #get_open_form().update_penal2()

  

  def text_box_1_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    
    if len(str(self.text_box_1.text)) !=0 and int(self.text_box_1.text)>0:
        self.check_box_hold.enabled = True
        if int(self.text_box_1.text)<=5:
          for i in range(int(self.text_box_1.text)):
              order = (self.label_2.text,self.text_box_1.text)
              pagestack.orderL.append(order)
        else:
           alert('The maximum is 5!')
           for item in pagestack.orderL:
              if item[0]==self.label_2.text:
                 pagestack.orderL.remove(item)
           
           self.check_box_hold.enabled = False
           self.text_box_1.text = ''
      
            
        print('amount',len(pagestack.orderL))

 
  def check_box_hold_show(self, **event_args):
    """This method is called when the CheckBox is shown on the screen"""
    if len(self.text_box_1.text)==0:
      self.check_box_hold .enabled = False
    
      
    
       

 

  


  

 

  

  


 

  

  

 
  




  

