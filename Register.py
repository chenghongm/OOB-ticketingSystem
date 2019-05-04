from anvil import *
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from Query import Query
import login_flow


class Register(RegisterTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    pass 
  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def text_box_10_show(self, **event_args):
    """This method is called when the TextBox is shown on the screen"""
    pass

  def CreateAccount_click(self, **event_args):
    """This method is called when the button is clicked"""
    emailL = []
    items = app_tables.users.search()
    for item in items:
      emailL.append(item['email'])
      
    
    if len(self.f_name.text)==0:
      
       alert("First Name is required!")
       print('f_n')
    elif len(self.l_name.text) ==0:
       alert("Last Name is required!")
       print('l_n') 
    elif len(self.password.text) ==0 or len(self.password.text)<8:
      alert("Password is required and no less than 8 characters!")
      print('pass')
    elif len(self.text_box_repass.text)==0:
      alert('Please confirm your password')
    elif self.password.text != self.text_box_repass.text:
        alert('Password not matched!,try again!')
        self.password.text = ''
        self.text_box_repass.text = ''
    elif len(self.email.text) ==0:
      alert("Email is required!")
      
   
      print('email')
    elif len(self.phone.text) ==0:
      alert("Phone is required!")
      print('phone')
    elif self.file_loader_1.file.length == 0:
      alert("Valid document is required!")
      
      print('file')
    elif self.password.text == self.text_box_repass.text:
       case = anvil.server.call('checkpassword',self.password.text)
       if case == 1:
         alert('Please have at least one capital letter in your password!')
       elif case ==2:
         alert('Please have at least one special chracter in your password!')
       else:
          print('password done.')
          if self.email.text in emailL:
            alert('You are in record,please sign in!')
            anvil.users.login_with_form()
            open_form('Query')

          else:
            
            userL = list(app_tables.users.search())
            userID = anvil.server.call('get_userID',userL)
            app_tables.users.add_row(First_Name=self.f_name.text,
                                     Last_Name=self.l_name.text,
                                     password_hash=anvil.server.call('encrypt',self.password.text),
                                     email=self.email.text,
                                     Phone=self.phone.text, 
                                     Valid_Document=self.file_loader_1.file,
                                     Credit=0,enabled=False,UserID=userID)
            anvil.server.call('_send_email_confirm_link', self.email.text)
            anvil.alert("A new confirmation email has been sent to %s.Please wait Administrator varifying. " % self.email.text)
            #anvil.server.call('_send_email_confirm_link',self.email.text)
            #alert('Account created, please confirm email address and wait for Administrator verify! It will take up to 24 hours!')
            
            
          
          open_form('Query')
    

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.login_with_form()
    open_form('Query')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Query')



  

  


