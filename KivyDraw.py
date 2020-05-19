from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics import Line



class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)


        # draw stuff on canvas
        with self.canvas:
            Color(0, 0, 1, 1)
            Line(points = (20, 30, 200, 100, 100, 50, 400, 100, 300, 50 ))
            Color(1, 0, 0, 1)
            self.rect = Rectangle( pos = (300, 300), size = (50,50) )
            print( self.rect)
            

    def on_touch_down(self, touch):
        print("Mouse Down", touch)
        self.rect.pos = touch.pos
        


        
    def on_touch_up(self, touch):
        print("Mouse Up", touch)

        
    def on_touch_move(self, touch):
        print("Mouse Move", touch)
        self.rect.pos = touch.pos



class Kivypaint(App):
    def build(self):
        return Touch()


if __name__ == "__main__":
    Kivypaint().run()
