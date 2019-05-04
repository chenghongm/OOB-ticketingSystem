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
def inserData2(dataSet):
    app_tables.search_result_re.delete_all_rows()
    for item in dataSet:
    #print(item, '\n')
        itemSet = item.split('|')
        #print(len(itemSet),'\n')
        train = itemSet[3]
                
        date = itemSet[13]
        
        from_station = itemSet[4]
       
        to_station = itemSet[5]
        
        start_time = itemSet[8]
        
        end_time = itemSet[9]
        
        duration = itemSet[10]
        app_tables.search_result_re.add_row(Train=train,Date=date,From_Station=from_station,To_Station=to_station,Start_time=start_time,End_time=end_time,Duration=duration)
        
    print('Inserted-2!')
