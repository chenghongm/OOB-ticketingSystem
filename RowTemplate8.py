from anvil import *
import anvil.server
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RowTemplate8(RowTemplate8Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

 
    

  def button_1_show(self, **event_args):
    """This method is called when the Button is shown on the screen"""
    row = app_tables.order.get(OrderID=self.label_1.text)
    
    date =row['Trip'][:8]
    #print(date)
    date_ticket = date[:4]+'-'+date[5:6]+'-'+date[6:8]
    #print(date_ticket)
    #print(date_ticket)
    expired = anvil.server.call('check_date_expired',date_ticket)
    if expired is True:
      self.button_1.enabled = False
      self.button_2.enabled = False
    else:
      self.button_1.enabled = True
    

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    row = app_tables.order.get(OrderID=self.label_1.text)
    ticket = str(row['OrderID']+row['Passenger']+row['Trip']+row['UserID'])
    media = anvil.server.call('make_qr_code', ticket)
    user =anvil.users.get_user()
    to_adr = user['email']
    anvil.server.call('sendTicket',media,to_adr)
    
    alert(Image(source=media,spacing_above=10,spacing_below=10),title='Ticket')
    download(media)

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    user = anvil.users.get_user()
    to = user['email']
    choice = confirm('Are you going to cancel this ticket?',buttons=[('Yes','Yes'),('No','No')])
    if choice == 'Yes':
      self.button_1.enabled = False
      self.button_2.enabled  = False
      anvil.server.call('refundEmail',to)
      alert('You will get partial refund, please check your email!')
         
    
    



