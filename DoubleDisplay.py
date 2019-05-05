from anvil import *
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import pagestack
class DoubleDisplay(DoubleDisplayTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_d.items =anvil.server.call('get_data')
    print('d-Done')
    
    self.repeating_panel_re.items =anvil.server.call('get_data_re')
    print('re-done')
    
    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
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
          get_open_form().label_status_show()
       else:
          open_form('Register')
         
    elif user['enabled']==False:
       alert('Please wait for Admin enable your account!')
    else:
       open_form('Order')

  def button_2_goquery_click(self, **event_args):
    """This method is called when the button is clicked"""
    pagestack.pageL.pop()
    open_form(pagestack.pageL[len(pagestack.pageL)-1])

  def button_signup_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Register')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.login_with_form()
    user = anvil.users.get_user()
    if user is not None:
      self.label_status.text = 'Welcome, '+user['email']
      self.link_1.visible = True
      self.button_signup.visible = False
      self.button_signin.visible = False
    else:
      self.label_status.text = 'Welcome! Tourist!'
      self.button_signup.visible = True
      self.button_signin.visible = True
      self.link_1.visible = False
  
    

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('userAccount')

  def form_show(self, **event_args):
    """This method is called when the column panel is shown on the screen"""
    pagestack.pageL.append('DoubleDisplay')
    print(pagestack.pageL)
    if pagestack.pageL[len(pagestack.pageL)-2]=="DoubleDisplay":
       pagestack.pageL.pop()
    
       

  def button_logout_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.logout()
    pagestack.clear()
    open_form('Query')

  def label_status_show(self, **event_args):
    """This method is called when the Label is shown on the screen"""
    user = anvil.users.get_user()
    if user is not None:
      self.label_loginstatus.text = 'Welcome, '+user['email']
      self.link_go2useraccount.visible = True
      self.button_signup.visible = False
      self.button_signin.visible = False
    else:
      self.label_status.text = 'Welcome! Tourist!'
      self.button_signup.visible = True
      self.button_signin.visible = True
      self.link_1.visible = False





