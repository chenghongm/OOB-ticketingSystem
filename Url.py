import anvil.stripe
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.email
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

import anvil.server

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
def Url(date, fromStation,toStation, Ptype):
      #global myUrl
      myUrl = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date='+ date + '&leftTicketDTO.from_station=' + fromStation+'&leftTicketDTO.to_station='+ toStation+ '&purpose_codes='+ Ptype
      print(myUrl)
      return myUrl