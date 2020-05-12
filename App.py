import kivy
from kivy.app import App
from kivy.uix.button import Button


# App definition
class MyApp(App):
    def build(self):
        return Button(text = "Hello World")



# Run the app
MyApp().run()