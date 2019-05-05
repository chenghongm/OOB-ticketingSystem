import anvil.stripe
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.email
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import random 
import string
import datetime

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
def get_userID(userList):
   now  = datetime.datetime.now()
   choiceL = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'   
   date = now.strftime("%Y%m%d")   
   letters = random.choice(choiceL)+random.choice(choiceL)+random.choice(choiceL)
   if len(userList)==0:
      count = 1
      nums = "{:06d}".format(count)
      userID = date+letters+nums
   else:
      lastUserID = userList[len(userList)-1]['UserID']
      count = int(lastUserID[-6:])+1
      nums = "{:06d}".format(count)
      userID = date+letters+nums
   return userID

@anvil.server.callable
def gen_orderID(userID):
      
      #userL = list(app_tables.users.search())
      orderL = list(app_tables.order_tmp2.search())
     # userID = anvil.server.call('get_userID',userL)
      now  = datetime.datetime.now()
      date = now.strftime("%Y%m%d")
      if len(orderL)==0:
        count = 1
        nums = "{:06d}".format(count)
        orderID = userID + date + nums
       
      else:
        lastOrderID = orderL[len(orderL)-1]['OrderID']
        count = int(lastOrderID[-6:])+1
        nums = "{:06d}".format(count)
        orderID = userID + date + nums
      return orderID
    
@anvil.server.callable    
def removeOrder(trip):
  row = app_tables.order_tmp.get(Trip=trip)
  row.delete()
  
      
      
      
      
      
      
      
      
      