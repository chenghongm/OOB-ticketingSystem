from anvil import *
import anvil.server
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Passenger(PassengerTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.items = app_tables.passenger.search()
    # Any code you write here will run when the form opens.
    
  def update_penal(self):
    self.repeating_panel_1.items = app_tables.passenger.search()
    # Any code you write here will run when the form opens.
    
  def button_add_click(self, **event_args):
    """This method is called when the button is clicked"""
    if len(self.box_f.text)==0 or len(self.box_l.text)==0 or len(self.box_email.text)==0 or len(self.file_loader_1.file.name)==0:
       alert('All fileds are required!')
    else:
        user = anvil.users.get_user()
        userID = user['UserID']
        f_name = self.box_f.text
        l_name = self.box_l.text
        email = self.box_email.text
        doc = self.file_loader_1.file
        app_tables.passenger.add_row(email=email,
                                    first_name=f_name,
                                    last_name=l_name,
                                    valid_document=doc,from_user=userID)
        get_open_form().update_penal()
        self.box_f.text = ''
        self.box_l.text = ''
        self.box_email.text = ''
        self.file_loader_1.clear()
  

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('userAccount')

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('orderhistory')

  def button_6_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('contact')

  def button_8_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.check_box_1.checked is False:
      alert('You have to check the field of "I was noticed"!')
    elif len(list(app_tables.passenger.search()))==0:
      choice = alert(content = 'You did not add any passenger yet, are you going to quit?',buttons=[('Yes','Yes'),('No','No')])
      if choice == 'Yes':
        open_form('Query')
      else:
        get_open_form()
    else:
      alert('Passengers added successfully! Now you can buy tickets for them!')
      open_form('Query')

  def form_show(self, **event_args):
    """This method is called when the column panel is shown on the screen"""
    user = anvil.users.get_user()
   
    self.label_11.text = 'Welcome! ' + user['email']

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('credit')

  def button_query_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Query')



  



