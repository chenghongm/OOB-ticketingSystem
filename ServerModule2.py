import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.email
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from anvil import *
import anvil.stripe
import time
from datetime import date
import hashlib
#from anvil.google.drive import app_files
import qrcode
import pandas
import qrcode.image.svg
from io import BytesIO

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
def checkpassword(password):
    allCaps = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'
    allSpecs = '!~@#$%^&*()'
    capital_letters = 0
    specical_characters = 0
    for i in password:
      if i in allCaps:
        capital_letters +=1
      elif i in allSpecs:
        specical_characters +=1
      else:
        continue
    if capital_letters ==0:
       return 1
    elif specical_characters ==0:
       return 2
    else:
       return 3
      
@anvil.server.background_task       
def autodel_timeup(userID,trip):
    print('start')             # without printing?
    time.sleep(30)   
    
    row = app_tables.order_tmp.get(Trip==trip) # time up, mark deleted the order,to benefit data traning
    row.delete()   # row was deleted!
    user = app_tables.users.get(UserID=userID)
    user['Credit'] = user['Credit']-1 
    print('End')  # without printing?
  
@anvil.server.background_task    
def killTask():
    anvil.server.launch_background_task('autodel_timeup').kill()
    
    
@anvil.server.callable
def endHoldtime():
    task = anvil.server.launch_background_task('killTask')
    return task

@anvil.server.callable  
def holdtime(label, trip):
    
    task = anvil.server.launch_background_task('autodel_timeup',label,trip)
    print('I am in!')
    
    return task
    
   # print('time out!')
    
@anvil.email.handle_message
def new_message(msg):
  app_tables.message.add_row(
    from_address= msg.envelope.from_address,
    to_address = msg.envelope.recipient,
    subject=msg.subject,
    content=msg.text,
    when=str(date.today())
  )
  
@anvil.server.callable  
def noticeEmail(to_adr):
  anvil.email.send(from_name="Admin", 
                 to=to_adr, 
                 subject="Welcome",
                 text="Welcome to TicketingCSF!")
@anvil.server.callable  
def replyEmail(to_adr,reply_message):
  anvil.email.send(from_name="Admin", 
                 to=to_adr, 
                 subject="No-Reply",
                 text=reply_message)
  
@anvil.server.callable  
def refundEmail(to_adr):
  anvil.email.send(from_name="Admin", 
                 to=to_adr, 
                 subject="No-Reply",
                 text='You will get partial refund according to your credit, please check your email 3-5 days. \n Thanks being with TicketingCSF ')

@anvil.server.callable
def sendTicket(media, to_adr):
    anvil.email.send(from_name="TicketingCSF", 
                 to=to_adr, 
                 subject="Ticket",
                 text='Thank you be with us, enjoy your trip. \n Thanks being with TicketingCSF ',
                 attachments=media)

   

@anvil.server.callable  
def passengerItem(userID):
  passengerL = []
  passengerL.append('')
  items = app_tables.passenger.search(from_user=userID)
  for item in items:
        passenger = item['first_name']+' '+item['last_name']
        passengerL.append(passenger)
  return passengerL
      
@anvil.server.callable  
def encrypt(text):
  password_hash = hashlib.sha256(text.encode()).hexdigest()
  return password_hash

@anvil.server.callable 
def check_date_expired(date_ticket):
   y1,m1,day1 = [int(i) for i in str(date.today()).split('-')]
   y2,m2,day2 = [int(i) for i in str(date_ticket).split('-')]
   date1 = date(y1,m1,day1)
  
   date2 = date(y2,m2,day2)
   if date1>date2:
      return True
   else:
      return False

  
@anvil.server.callable
@anvil.server.http_endpoint("/qrcode")
def make_qr_code(qr_code_data, **params):
    qr_code_obj = qrcode.make(qr_code_data, 
                              image_factory=qrcode.image.svg.SvgPathImage, 
                              error_correction=qrcode.constants.ERROR_CORRECT_Q,
                              box_size=25, version=2)
    data = BytesIO()
    qr_code_obj.save(data)
    data.seek(0)
    svg_text = data.read()
    return BlobMedia("image/svg+xml", svg_text, name="qrcode.svg")
  
@anvil.server.callable
def printOrder():
    items = app_tables.order.search()
    file = open('/tmp/order.csv','w')
    file.write('OrderID                                                         Passenger        UserID\n')
    file.write('--------------------------------------------------------------------------------------------------\n')
    for item in items:
       orderID = item['OrderID']
       passenger = item['Passenger']
       userID = item['UserID']
       file.write(orderID+'     '+passenger+'     '+userID +'\n')
    
      
@anvil.server.callable
def readFile():
  file = open('/tmp/order.csv','r')
  t = file.read()
  return t

@anvil.server.callable
def downloadOrder(items):
  
  # Get an iterable object with all the rows in my_table
  #items = app_tables.order.search()
  # For each row, pull out only the data we want to put into pandas
  dicts = [{'Trip': r['Trip'], 'OrderID': r['OrderID'],'Passenger':r['Passenger']}
         for r in items]

  df = pandas.DataFrame.from_dict(dicts)
  html = df.to_html()
  return html
    
'''      
 
def checkValidTrip(trip1,trip2,passenger1,passenger2):
   if passenger1 == passenger2:
      if trip1[0:8]==trip[0:8]:
        if 
'''   
  
  
