import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class GridComponent(Widget):
    # parameters for .kv file
    name: ObjectProperty(None)
    style: ObjectProperty(None)

    # method for .kv file
    def btn(self):
        print("Name: ", self.name.text, "Style: ", self.style.text)
        self.name.text = ""
        self.style.text = ""




class Myapp(App):
    def build(self):
        return GridComponent()



if __name__ == "__main__":
    Myapp().run()


