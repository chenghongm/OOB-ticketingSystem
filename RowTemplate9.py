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


class RowTemplate9(RowTemplate9Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    user = anvil.users.get_user()
    self.drop_down_1.items = anvil.server.call('passengerItem',user['UserID'])
    # Any code you write here will run when the form opens.
    
  

  def passenger(self):
    passenger = str(self.drop_down_1.selected_value)
    return passenger
  
  def storeData(self,items):
    user = anvil.users.get_user()
    userID = user['UserID']
    passenger = self.passenger()
    print(passenger)
    for item in items:
        orderID = item[0]
        print(orderID)
        trip = item[1]
        print(trip)
        pg = item[2]
        print(pg)
        app_tables.order.add_row(OrderID=orderID,Trip=trip,UserID=userID,Passenger=pg)
    print('data stored!')

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    
    order = (self.label_p.text, self.label_trip.text ,str(self.drop_down_1.selected_value))
    #print(order[0],order[1],order[2])
    if len(pagestack.payOrder)==0:
        pagestack.payOrder.append(order)
    else:
       for item in pagestack.payOrder:
          if item[0]==order[0]:
            pagestack.payOrder.remove(item)
       pagestack.payOrder.append(order)
    
       
    #print(len(pagestack.payOrder),pagestack.payOrder)

  