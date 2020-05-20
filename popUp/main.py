from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup

# popup class
class P(FloatLayout):
    pass


# main window
class MainWindow(Widget):
    show = P()

    PopUpWindow = Popup(
        title = "Pop up",
        content = show,
        size_hint = (None, 0.2),
        size = (400, 400)
    )

    def btn(self):
        self.PopUpWindow.open()

    def close(self):
        self.PopUpWindow.close()

    

class popupapp(App):
    def build(self):
        return MainWindow()






if __name__ == "__main__":
    popupapp().run()
