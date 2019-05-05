from anvil import *
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from RowTemplate2 import RowTemplate2
import login_flow
import pagestack

class Display(DisplayTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    
    self.init_components(**properties)
    self.repeating_panel_1.items =anvil.server.call('get_data')
    # Any code you write here will run when the form opens.
    app_tables.order_tmp.delete_all_rows()
    print('table clean')
  def form_show(self, **event_args):
    """This method is called when the column panel is shown on the screen"""
    pagestack.pageL.append('Display')
    print(pagestack.pageL)
    if pagestack.pageL[len(pagestack.pageL)-2]=="Display":
       pagestack.pageL.pop()
    
    
    

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    #anvil.server.call('readStation_data')
    
    #print('code in!')
    
    
    user = anvil.users.get_user()
    if user is None:  
       choice = alert(content="If you have an account, please sign in! Otherwise, please sign up!",
               title="An important choice",
               large=True,
               buttons=[
                 ("SignIn","SignIn"),
                 ("SignUp","SignUp")
                                ])
       if choice =='SignIn':
          login_flow.login_with_form()
          get_open_form().label_loginstatus_show()
       else:
          open_form('Register')
         
    elif user['enabled']==False:
       alert('Please wait for Admin enable your account!')
    else:
       open_form('Order')
       
       

  def button_signup_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Register')

  def button_go_query(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Query')

  

  def button_go_query_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Query')

  def label_loginstatus_show(self, **event_args):
    """This method is called when the Label is shown on the screen"""
    user = anvil.users.get_user()
    if user is None:
      self.label_loginstatus.text = 'Welcome,Tourist!'
      self.link_go2useraccount.visible = False
      self.button_signup.visible = True
      self.button_signin.visible = True
    else:
      self.label_loginstatus.text = 'Welcome, '+ user['email']
      self.link_go2useraccount.visible = True
      self.button_signup.visible = False
      self.button_signin.visible = False

  def button_signin_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.login_with_form()
    get_open_form().label_loginstatus_show()

  def button_logout_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.logout()
    pagestack.clear()
    open_form('Query')

 

  def button_back_click(self, **event_args):
    """This method is called when the button is clicked"""
    pagestack.pageL.pop()
    open_form(pagestack.pageL[len(pagestack.pageL)-1])

  def link_go2useraccount_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('userAccount')


 





