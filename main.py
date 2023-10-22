from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
#from kivy.properties import ObjectProperty
import login
import register
import forgot
import faild
import dash

colors = {
    "Teal": {
        "200": "#34acbc",
        "500": "#34acbc",
        "700": "#34acbc",
    },
    "Red": {
        "200": "#C25554",
        "500": "#C25554",
        "700": "#C25554",
        "A700": "#C25554",
    },
    "Light": {
        "StatusBar": "E0E0E0",
        "AppBar": "#202020",
        "Background": "#2E3032",
        "CardsDialogs": "#FFFFFF",
        "FlatButtonDown": "#CCCCCC",
       # "MDTextField":  "#CCCCCC",

    },
}







sm = ScreenManager()


class TestApp(MDApp):

      def build(self):
          sm.add_widget(login.login(name="log"))
          sm.add_widget(register.register(name="reg"))
          sm.add_widget(forgot.forgot(name="forgot1"))
          sm.add_widget(faild.faild(name="faild"))
          sm.add_widget(dash.dash(name="dash1"))
          self.theme_cls.primary_palette = "Teal"
          self.theme_cls.colors = colors
          self.theme_cls.accent_palette = "Red"


          return sm



TestApp().run()

