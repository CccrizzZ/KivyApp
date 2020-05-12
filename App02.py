import kivy
from kivy.app import App
from kivy.uix.widget import Widget


class GridComponent(Widget):
    pass


class Myapp(App):
    def build(self):
        return GridComponent()


if __name__ == "__main__":
    Myapp().run()


