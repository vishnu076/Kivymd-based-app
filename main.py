from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
import json
import random
import re
import requests
import pyrebase
firebaseConfig = {
    'apiKey': "AIzaSyCtSEBJsSuVAR8mvH4ExZqIj4SjjBIiKy4",
    'authDomain': "oceanic-student-278809.firebaseapp.com",
    'databaseURL': "https://oceanic-student-278809-default-rtdb.asia-southeast1.firebasedatabase.app",
    'projectId': "oceanic-student-278809",
    'storageBucket': "oceanic-student-278809.appspot.com",
    'messagingSenderId': "903599690112",
    'appId': "1:903599690112:web:ff3619cf2b12fb5d7eb165",
    'measurementId': "G-WTX66TGB5R"}
firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()

Window.size=(450,500)

Login="""
ScreenManager:
   LoginScreen:
   SignupScreen:
   MainScreen:
   ProductScreen:
<LoginScreen>:
   name:"login"
   MDFloatLayout
      MDLabel:
         markup:True
         text:"[b]Login[/b]"
         pos_hint:{"center_y":.85}
         halign:"center"
         font_size:40
      MDTextField:
         id:email
         mode:"rectangle"
         hint_text:"Enter email address"
         pos_hint:{"center_x":.5,"center_y":0.6}
         size_hint_x:0.8
         current_hint_color:0,0,0,1
         icon_right:"mail"
         
      MDTextField:
         id:j
         hint_text:"Enter password"
         mode:"rectangle"
         pos_hint:{"center_x":.5,"center_y":0.5}
         height:"30dp"
         width:5
         size_hint_x:0.8
         current_hint_color:0,0,0,1
         password:True
    
         
      MDIconButton:
         icon:"eye-off"
         pos_hint:{"center_x":0.851,"center_y":0.5}
         on_press:
            self.icon="eye" if self.icon=="eye-off" else "eye-off"
            j.password=False if self.icon=="eye" else True
        
     
      MDLabel:
         markup:True
         text:("Dont have an account?[ref=Sign][color=ff0000]Sign up[/color][/ref]")
         pos_hint:{"center_x":.6,"center_y":0.4}
         
         on_ref_press:root.manager.current="product"
      MDRaisedButton:
         text:"Log in"
         pos_hint:{"center_x":0.5,"center_y":0.3}
         size_hint_x:.5
         on_press:root.get("onj")
<SignupScreen>:
   name:"sign"
   MDFloatLayout
      MDLabel:
         markup:True
         text:"[b]Sign up[/b]"
         pos_hint:{"center_y":.85}
         halign:"center"
         font_size:40
      MDTextField:
         #:set a "^[a-z0-9]+[\._]?[a-z0=9]+[@}\w+[.]\w{2,3}$"
         
         hint_text:"Enter email address"
         id:email
         helper_text:"This feild is required"
         helper_text_mode:"on_focus"
         required:True
         error:False
         pos_hint:{"center_x":.5,"center_y":0.6}
         size_hint_x:0.8
         current_hint_color:0,0,0,1
         required:True
      MDTextField:
         id:passw
         
         hint_text:"Enter password"
         helper_text:"Password must be at least 7 with Uppercase and a special character"
         helper_text_mode:"on_focus"
         pos_hint:{"center_x":.5,"center_y":0.5}
         size_hint_x:0.8
         
         current_hint_color:0,0,0,1
         password:True
         required:True
      MDTextField:
         id:passw1
         hint_text:"Confirm password"
         helper_text:""
         helper_text:"persistant"
         pos_hint:{"center_x":.5,"center_y":0.4}
         size_hint_x:0.8
         current_hint_color:0,0,0,1
         password:True
         required:True
         
      
      MDLabel:
         markup:True
         text:("Already have an account?[ref=log][color=ff0000]Log in[/color][/ref]")
         pos_hint:{"center_x":.6,"center_y":0.3}
         on_ref_press:root.manager.current="login"
      MDRaisedButton:
         text:"Sign up"
         pos_hint:{"center_x":0.5,"center_y":0.2}
         size_hint_x:.5
         on_press:root.check("obK")
<MainScreen>
   name:"main"
   BoxLayout:
      orientation:"vertical"
      MDToolbar:
         title:"Inventory"
         left_action_items:[["menu",lambda x:nav_drawer.toggle_nav_drawer()]]
         elevation:8
      MDLabel:
         markup:True
         text:"[b]Suppliers[/b]"
         pos_hint:{"center_y":.85}
         valign:"top"
         halign:"center"
         font_size:40
         height:self.texture_size[1]
      MDTextField:
         hint_text:"Enter Supplier Name"
         id:supplier
         helper_text:"This feild is required"
         helper_text_mode:"on_focus"
         required:True
         
         error:False
         pos_hint:{"center_x":0.5,"center_y":60}
         size_hint_x:0.8
         current_hint_color:0,0,0,1
         required:True
    
      MDRaisedButton:
         text:"ADD"
         pos_hint:{"center_x":0.5,"center_y":0.2}
         size_hint_x:.5
         on_press:root.post("jj")
      MDLabel:
         text:""
       
   MDNavigationDrawer:
      id:nav_drawer
      orientation: "vertical"
      padding: "8dp"
      spacing: "8dp"
      AnchorLayout:
         anchor_x: "left"
         size_hint_y: None
         height: avatar.height
         Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "j.jpg"
      MDLabel:
         text: "KivyMD library"
         font_style: "Button"
         size_hint_y: None
         height: self.texture_size[1]

      MDLabel:
         id:email
         text:
         font_style: "Caption"
         size_hint_y: None
         height: self.texture_size[1]
      ScrollView:
         MDList:
            OneLineIconListItem:
               text:"Suppliers"
               IconLeftWidget:
                  icon:'store'
            OneLineIconListItem:
               text:"Stock"
               on_release:root.manager.current="product"
               IconLeftWidget:
                  icon:'warehouse'
            OneLineIconListItem:
               text:"Issue"
               IconLeftWidget:
                  icon:'human-greeting'
            OneLineIconListItem:
               text:"History"
               IconLeftWidget:
                  icon:'history'

<ProductScreen>
   name:"product"
   BoxLayout:
      orientation:"vertical"
      MDToolbar:
         title:"Inventory"
         left_action_items:[["menu",lambda x:nav_drawer.toggle_nav_drawer()]]
         elevation:8
      MDLabel:
      MDLabel:
      MDLabel:
         markup:True
         text:"[b]Products[/b]"
         pos_hint:{"center_y":.85}
         valign:"top"
         halign:"center"
         font_size:40
         height:self.texture_size[1]
      MDTextField:
         hint_text:"Enter Product code"
         id:supplier
         helper_text:"This feild is required"
         helper_text_mode:"on_focus"
         required:True
         error:False
         pos_hint:{"center_x":0.5,"center_y":60}
         size_hint_x:0.8
         current_hint_color:0,0,0,1
         required:True
      MDTextField:
         hint_text:"Enter Product name"
         id:supplier
         helper_text:"This feild is required"
         helper_text_mode:"on_focus"
         required:True
         error:False
         pos_hint:{"center_x":0.5,"center_y":60}
         size_hint_x:0.8
         current_hint_color:0,0,0,1
         required:True
      MDTextField:
         hint_text:"Enter Price"
         id:supplier
         helper_text:"This feild is required"
         helper_text_mode:"on_focus"
         required:True
         error:False
         pos_hint:{"center_x":0.5,"center_y":60}
         size_hint_x:0.8
         current_hint_color:0,0,0,1
         required:True

      MDTextField:
         hint_text:"Enter quantity"
         id:supplier
         helper_text:"This feild is required"
         helper_text_mode:"on_focus"
         required:True
         error:False
         pos_hint:{"center_x":0.5,"center_y":60}
         size_hint_x:0.8
         current_hint_color:0,0,0,1
         required:True
      
      MDTextField:
         hint_text:"Enter Supplier"
         id:supplier
         helper_text:"This feild is required"
         helper_text_mode:"on_focus"
         required:True
         error:False
         size_hint:(None,None)
         width:120
         pos_hint:{"x":0.1,"y":20}
         current_hint_color:0,0,0,1
         required:True 
         MDIconButton:
            icon:"arrow-down-drop-circle"
            
            size_hint:(None,None)
         
    
      MDRaisedButton:
         text:"ADD"
         pos_hint:{"center_x":0.5,"center_y":0.2}
         size_hint_x:.5
         on_press:root.post("jj")
      MDLabel:
         text:""
       
   MDNavigationDrawer:
      id:nav_drawer
      orientation: "vertical"
      padding: "8dp"
      spacing: "8dp"
      AnchorLayout:
         anchor_x: "left"
         size_hint_y: None
         height: avatar.height
         Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "j.jpg"
      MDLabel:
         text: "KivyMD library"
         font_style: "Button"
         size_hint_y: None
         height: self.texture_size[1]

      MDLabel:
         id:email
         text:
         font_style: "Caption"
         size_hint_y: None
         height: self.texture_size[1]
      ScrollView:
         MDList:
            OneLineIconListItem:
               text:"Suppliers"
               on_release:root.manager.current="main"
               IconLeftWidget:
                  icon:'store'
            OneLineIconListItem:
               text:"Stock"
               IconLeftWidget:
                  icon:'warehouse'
            OneLineIconListItem:
               text:"Issue"
               IconLeftWidget:
                  icon:'human-greeting'
            OneLineIconListItem:
               text:"History"
               IconLeftWidget:
                  icon:'history'
 
"""
class LoginScreen(Screen):
    global k
    def get(self,obj):
     d=0
     c=0
     k=self.ids.email.text
     b=self.ids.j.text
     url="https://oceanic-student-278809-default-rtdb.asia-southeast1.firebasedatabase.app/users/.json"
     res=requests.get(url=url)
     a=res.json()
     print(a.values())
     for keys,vales in a.items():
         if vales["email"]==k:
              if vales["password"]==b:
                  c=3
                  
                  break
              else:
                  d=5
         else:
              c=1
     if c==3:
         #dialog=MDDialog(text="logined scussefully",size_hint=(0.5,1))
         #dialog.open()
         self.manager.current="main"
         self.manager.get_screen("main").ids.email.text=k
       
     if d==5:
         dialog=MDDialog(text="incorrect password",size_hint=(0.5,1))
         dialog.open()
        
     elif c==1:
         
         dialog=MDDialog(text="user not found ,register",size_hint=(0.5,1))
         dialog.open()
class ProductScreen(Screen):
    pass
class SignupScreen(Screen):
    global a
    url1="https://oceanic-student-278809-default-rtdb.asia-southeast1.firebasedatabase.app/suppliers/.json"
    url="https://oceanic-student-278809-default-rtdb.asia-southeast1.firebasedatabase.app/users/.json"
    def check(self,obj):
        e=[]
        a=self.ids.email.text
        regex="^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$"
        if a=="":
            self.ids.email.helper_text="This feild is required"
        elif re.search(regex,a)==None:
            
            self.ids.email.helper_text="Enter valid gmail "
            self.ids.email.helper_text_mode="on_error"
            self.ids.email.error=True
        else:
            
            self.ids.email.error=False
            e=e+[0]
        b=self.ids.passw.text
        if b=="":
            pass
            
        elif not(len(b)>=7 and b.isalnum()==False and b.islower()==False):
            print(self.ids.passw.text)
            
            self.ids.passw.helper_text="Must contain a Upper case,7 letters,special character "
            self.ids.passw.helper_text_mode="on_error"
            self.ids.passw.error=True
        else:
            self.ids.passw.error=False
            
            e=e+[0]
        c=self.ids.passw1.text
        if c=="":
            pass
        elif c!=b:
            self.ids.passw1.helper_text="Passwords not matching"
            self.ids.passw1.helper_text_mode="on_error"
            self.ids.passw1.error=True
        else:
            e=e+[0]
            self.ids.passw1.error=False
        if e==[0,0,0]:
            user=auth.create_user_with_email_and_password(a,c)
            data={"email":a,"password":b}
            
            data1={"email":a}
            #to_data=json.dumps(data)
            #to_data1=json.dumps(data1)
            self.manager.current="main"
            res=requests.post(url=self.url,json=data)
            print(res)
            res=requests.post(url=self.url1,json=data1)
            print(res)
            

class MainScreen(Screen):

    url="https://oceanic-student-278809-default-rtdb.asia-southeast1.firebasedatabase.app/suppliers/.json"
    def build(self):
       self.ids.email.text=a
       dialog=MDDialog(text=a+c,size_hint=(0.5,1))
       dialog.open()
    def post(self,obj):
        h=self.ids.supplier.text
        d=self.manager.get_screen("login").ids.email.text
        res=requests.get(url=self.url)
        
        a=res.json()
        for key,value in a.items():
            if value["email"]==d:
                g=list(value.keys())
                c=len(g)+1
                var="supplier"+str(c)
                ff=key
                data=value
                data[var]=h
        url3="https://oceanic-student-278809-default-rtdb.asia-southeast1.firebasedatabase.app/suppliers/"+key+"/.json"
        requests.delete(url=url3)
        requests.post(url=self.url,json=data)
        dialog=MDDialog(text="succesfully added",size_hint=(0.5,1))
        dialog.open()
        
           
        
        
        
        
class ContentNavigationDrawer(BoxLayout):
    pass

        
class Mainapp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Blue"
        login=Builder.load_string(Login)
        s=ScreenManager()
        s.add_widget(LoginScreen(name="login"))
        s.add_widget(SignupScreen(name="sign"))
        s.add_widget(MainScreen(name="main"))
        s.add_widget(ProductScreen(name="product"))
        return login
    
    def switch(self,obj):
        print("djfh")
Mainapp().run()
