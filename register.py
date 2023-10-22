from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import sqlite3






class register(Screen):
      Builder.load_file('register.kv')

      def __init__(self, **kwargs):
            super().__init__(**kwargs)

      def entry(self):
            a = self.ids.user1.text

            b = self.ids.passwd1.text

            c = self.ids.email.text

            print(a, b, c)

            conn = sqlite3.connect('main1.db')

            print("Opened database successfully")

            # conn.execute("create table user(username text,password char(50));")

            # print ("tables createded")

            # conn.execute("alter table user ADD email varchar(255);")

            # conn.execute("update user set email = 'jagan233@gmail.com' where username ='jagan';")
            # conn.execute("insert into user(username,password,email), values(?,?,?);",(a,b,c))

            sql = ("insert into user(username,password,email) values(?,?,?);")

            conn.execute(sql, (a, b, c))

            print("insert valeue successfully")

            x = conn.execute("select * from user")

            s = x.fetchall()

            print(s)

            self.ids.user1.text = ''

            self.ids.passwd1.text = ''

            self.ids.email.text = ''

            conn.commit()

            print("Records close successfully")
            conn.close()

            print("sucess fully resistor")
            self.manager.current = 'log'
