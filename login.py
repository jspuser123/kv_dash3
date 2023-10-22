from kivymd.app import MDApp
from kivy.uix.screenmanager import  Screen
from kivy.lang import Builder
import sqlite3



class login(Screen):
      Builder.load_file('login.kv')

      def __init__(self, **kwargs):
            super().__init__(**kwargs)



      def loginck(self):

            user = self.ids.user.text
            pass1 = self.ids.passwd.text
            conn = sqlite3.connect('main1.db')

            print("Opened database successfully")

            y = conn.execute('SELECT username,password from user WHERE username="%s" AND password="%s"' % (user, pass1))

            z = y.fetchone()

            print(z)
            self.ids.user.text = ''
            self.ids.passwd.text = ''

            if z is not None:
                  print('Welcome')
                  x = conn.execute('select * from user')
                  s = x.fetchall()
                  print(s)
                  self.manager.current = 'dash1'
                  self.manager.transition.direction = 'right'

            else:
                  print('Login failed')
                  x = conn.execute('select * from user')
                  s = x.fetchall()
                  print(s)
                  self.manager.current = 'faild'
                  self.manager.transition.direction = 'left'

            conn.commit()
            print("Records close successfully")
            conn.close()



