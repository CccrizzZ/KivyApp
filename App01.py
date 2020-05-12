import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput



# App components
class GridComponent(GridLayout):
    def __init__(self, **kwargs):
        super(GridComponent, self).__init__(**kwargs)
        
        # Set column number
        self.cols = 2

        # Add Label
        self.add_widget(Label(text = "Name: "))
        
        # Add Input
        self.NameInput = TextInput(multiline=True)
        self.add_widget(self.NameInput)





# App definition
class MyApp(App):
    def build(self):
        return GridComponent()



# Run the app
MyApp().run()