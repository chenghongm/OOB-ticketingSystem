import anvil.stripe
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.email
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import requests as re
from anvil.tables import app_tables

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
def inserData1(dataSet):
    app_tables.search_result.delete_all_rows()
    for item in dataSet:
    #print(item, '\n')
        itemSet = item.split('|')
        #print(len(itemSet),'\n')
        train = itemSet[3]
        #app_tables.search_result.add_row(Train=train)
        #trainList.append(train)
        
        date = itemSet[13]
        #app_tables.search_result.add_row(Date=date)
        #dateList.append(date)
        
        from_station = itemSet[4]
                
        to_station = itemSet[5]
        #app_tables.search_result.add_row(To_Station=to_station)
        #to_stationList.append(to_station)
        
        start_time = itemSet[8]
        #app_tables.search_result.add_row(Start_time=start_time)
        #start_timeList.append(start_time)
        
        end_time = itemSet[9]
        #app_tables.search_result.add_row(End_time=end_time)
        #end_timeList.append(end_time)
        
        duration = itemSet[10]
        app_tables.search_result.add_row(Train=train,Date=date,From_Station=from_station,To_Station=to_station,Start_time=start_time,End_time=end_time,Duration=duration)
        
    print('Inserted!')
