from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from random import random

# inherited from widget
class Touch(Widget):
    btn = ObjectProperty(None)



    def on_touch_down(self, touch):
        print("Mouse Down", touch)
        self.btn.opacity = 0.5

    def on_touch_up(self, touch):    
        print("Mouse Up", touch)
        self.btn.opacity = 1


    def on_touch_move(self, touch):
        print("Mouse Move", touch)
        self.btn.background_color = random(), random(), random(), 1



# inherited from App
class Toucheventapp(App):
    def build(self):
        return Touch()




if __name__ == "__main__":
    Toucheventapp().run()