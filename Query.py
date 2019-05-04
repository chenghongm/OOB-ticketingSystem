from anvil import *
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.http
import login_flow
from LoginDialog import LoginDialog
import pagestack



class Query(QueryTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run when the form opens.
    userL = list(app_tables.users.search())
    
    #print(userL[len(user)-1]['UserID'])
    
  def drop_down_2_show(self, **event_args):
    """This method is called when the DropDown is shown on the screen"""
    pass

  def drop_down_2_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def button_1_show(self, **event_args):
    """This method is called when the Button is shown on the screen"""
    print("Click me!")
  
  def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        
        dateStr = str(self.startDate.date)
        dateReStr = str(self.returnDate.date)
        date = dateStr[0:10]
        dateRe = dateReStr[0:10]
        from_station = str(self.drop_down_from.selected_value)[:3]
        to_station = str(self.drop_down_to.selected_value)[:3]
        pType = self.ADULT.text[0:5].upper()
        
        if self.radio_Round.selected == True:
            if len(str(self.startDate.date))==0 or len(str(self.returnDate.date))==0 or len(str(self.drop_down_from.selected_value))==0 or len(str(self.drop_down_to.selected_value))==0 :
              alert("all field are required!")
              
            elif int(str(self.startDate.date).replace('-',''))> int(str(self.returnDate.date).replace('-','')):
              alert("Invalid Return date!")
            
            else:
              myUrl = anvil.server.call("Url",date,from_station,to_station,pType)
              html = anvil.server.call('parseUrl',myUrl)
              anvil.server.call('inserData1',html)
              #myUrl = anvil.server.call("Url",date,from_station,to_station,pType)
              myUrlRe = anvil.server.call('Url',dateRe,to_station,from_station,pType)
              #html = anvil.server.call('parseUrl',myUrl)
              html_re = anvil.server.call('parseUrl',myUrlRe)
              #anvil.server.call('inserData1',html)
              anvil.server.call('inserData2',html_re)
              open_form('DoubleDisplay')  
              
        else:
              myUrl = anvil.server.call("Url",date,from_station,to_station,pType)
              html = anvil.server.call('parseUrl',myUrl)
              anvil.server.call('inserData1',html)
              open_form('Display') 
               
                
                
           
        
          

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def label_6_hide(self, **event_args):
    """This method is called when the Label is removed from the screen"""
    pass

  def retrunDate_hide(self, **event_args):
    """This method is called when the DatePicker is removed from the screen"""
    pass

  def oneway_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    self.returnLabel.visible = False
    self.returnDate.visible = False

  

  def button_signup_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    
    open_form('Register')
    
  def update_login_status(self):
     user = anvil.users.get_user()
     if user is None:
         alert('You are not logged in!')
     else:
         alert('Now you are logged in as ' + user['email'])
    
  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    anvil.users.login_with_form(show_signup_option=False,allow_cancel=True)
    user = anvil.users.get_user()
    if user is not None:
      self.label_loginstatus.text = 'Welcome, '+ user['email']
      #self.label_loginstatus.text = 'Welcome, '+ user['email']
      self.link_go2useraccount.visible = True
      self.button_signup.visible = False
      self.button_signin.visible = False
      
      
    
  def radio_Round_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    self.returnLabel.visible = True
    self.returnDate.visible = True

  def radio_Oneway_show(self, **event_args):
    """This method is called when the radio button is shown on the screen"""
    self.returnLabel.visible = False
    self.returnDate.visible = False

  def form_show(self, **event_args):
    """This method is called when the column panel is shown on the screen"""
    
    login_flow.do_email_confirm_or_reset()
    #anvil.users.login_with_form(allow_cancel=True,show_signup_option=False)
    #self.update_login_status()
    pagestack.pageL.append('Query')
    print(pagestack.pageL)
    
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
    


    

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    user = anvil.users.get_user()
    if user is not None:
        userE = user['email']
        adminE = app_tables.admins.get(Email=userE)
        if adminE:
          open_form('Admin')
        else:
        
          d=LoginDialog()
          choice= alert(d,title='Admin Login',dismissible=True,buttons=[('Login','Login'),('Cancel','Cancel')])
          if choice =='Login':
            if LoginDialog().email_box.text == adminE['Email'] and LoginDialog().password_box.text == adminE['Password']:
                open_form('Admin')
            elif LoginDialog().email_box.text != adminE['Email'] or LoginDialog().password_box.text != adminE['Password']:
               alert('Email and Password are not valid!This link only for Admin!')
               open_form('Query')
    

  def link_go2useraccount_click(self, **event_args):
    """This method is called when the link is clicked"""
    
    open_form('userAccount')

  def button_logout_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.logout()
    pagestack.clear()
    open_form('Query')

  


  
  
 






  










  





