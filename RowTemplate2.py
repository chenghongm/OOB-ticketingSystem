from anvil import *
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RowTemplate2(RowTemplate2Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def check_box_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    pass

  def check_box_1_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    
    
    trip = self.label_date.text +' | '+self.label_train.text+' | '+self.label_fstation.text+' | '+self.label_tstation.text+' | '+self.label_stime.text+' | '+self.label_etime.text + ' | '+self.label_duration.text
    row = app_tables.order_tmp.get(Trip=trip)
    if event_args['sender'].checked:
        if row is None :
          app_tables.order_tmp.add_row(Trip=trip)
    else:
        if row is not None:
          row.delete()
        
    
       
        
    
    

  def form_refreshing_data_bindings(self, **event_args):
    """This method is called when refreshing_data_bindings is called"""
    pass

  def button_add_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass




