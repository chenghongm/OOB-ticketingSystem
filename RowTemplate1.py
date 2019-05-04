from anvil import *
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RowTemplate1(RowTemplate1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def check_box_1_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    trip = self.label_date.text +' | '+self.label_train.text+' | '+self.label_from.text+' | '+self.label_to.text+' | '+self.label_start.text+' | '+self.label_end.text + ' | '+self.label_duration.text
    row = app_tables.order_tmp.get(Trip=trip)
    if event_args['sender'].checked:
        if row is None :
          app_tables.order_tmp.add_row(Trip=trip)
    else:
        if row is not None:
          row.delete()
