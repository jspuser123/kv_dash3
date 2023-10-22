from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
import numpy as np
from matplotlib import pyplot as plt
from kivy.clock import Clock
#import kivymd_extensions.akivymd
#from matplotlib import animation
#from matplotlib.animation import FuncAnimation
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

class dash(Screen):
      Builder.load_file('dash.kv')
      #########################################table
      def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.c = 0
            self.d = 0

            data_tables = MDDataTable(
                  pos_hint={"center_x": .5, "center_y": .5},
                  background_color_header="#65275d",
                  background_color_cell="#451938",
                  background_color_selected_cell="e4514f",
                  # background_color="teal",

                  # size_hint=(0.4, 0.35),
                  use_pagination=True,
                  column_data=[
                        ("No.", dp(30)),
                        ("Column 1", dp(30)),
                        ("Column 2", dp(30)),
                        ("Column 3", dp(30)),
                        ("Column 4", dp(30)),
                        ("Column 5", dp(30)),
                  ],
                  row_data=[
                        (f"{i + 1}", "1", "2", "3", "4", "5") for i in range(50)
                  ],
            )
            self.ids.tap1.add_widget(data_tables)

            ########################bar chart
            x = np.array(["A", "B", "c", "D"])
            x5 = np.array(["x", "y", "z", "m"])
            y = np.array([3, 8, 1, 10])

            fig = plt.figure()
            fig.set_facecolor("#e91e63")

            fig = plt.bar(x, y, color="hotpink")
            fig = plt.bar(x5, y, color="purple")

            # ani = FuncAnimation(fig, animate, interval=100)
            #ani = FuncAnimation(fig, animate, interval=100)


            self.ids.bar.add_widget(FigureCanvasKivyAgg(plt.gcf()))
            ############################wave
            x = np.linspace(0, 20, 201)
            y = np.sin(x)
            fig1 = plt.figure(figsize=(5, 5))
            fig1.set_facecolor("#311b92")
            fig1 = plt.plot(x, y, 'b')

            self.ids.wave.add_widget(FigureCanvasKivyAgg(plt.gcf()))
            ############################################graph
            x = range(1, 7)
            y = [1, 3, 4, 6, 8, 5]
            fig2 = plt.figure()

            fig2 = plt.figure(facecolor="#64b5f6")
            fig2=plt.fill_between(x, y)
            self.ids.graph.add_widget(FigureCanvasKivyAgg(plt.gcf()))

            ###########################circule
            y3 = np.array([35, 25, 25, 15])

            fig3 = plt.figure(facecolor='teal')
            fig3 = plt.pie(y3)
            fig3 = plt.ylabel("This is MY Y Axis")
            fig3 = plt.xlabel("X Axis")

            self.ids.circle.add_widget(FigureCanvasKivyAgg(plt.gcf()))

      def clk(self):
            self.c = 0
            self.d = 0
            Clock.schedule_interval(self.increment, .05)

            self.increment(0)

      def increment(self, interval):
            self.c += 1
            self.d += 1
            print("increment number", self.c)
            print("increment number", self.d)
            self.ids.cpu.val = self.c
            self.ids.cpu.text = f'{self.c}%'
            self.ids.ram.val1 = self.d
            self.ids.ram.text = f'{self.d}%'

            if self.c == 360:
                  Clock.unschedule(self.increment)
                  self.clk()


class navi(BoxLayout):
      pass

