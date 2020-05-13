import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class MyGrid(GridLayout):
    def __init__(self,**kwargs):
        super(MyGrid, self).__init__(**kwargs)
        
        # set column to 2
        self.cols = 1

        # create inside component
        self.inside = GridLayout()
        self.inside.cols = 2

        # add labels and input to inside component
        self.inside.add_widget(Label(text = "Name: "))
        self.name = TextInput(multiline = False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text = "Style"))
        self.style = TextInput(multiline = False)
        self.inside.add_widget(self.style)

        self.inside.add_widget(Label(text = "Flavor"))
        self.flavor = TextInput(multiline = False)
        self.inside.add_widget(self.flavor)

        # add component
        self.add_widget(self.inside)


        # button component
        self.submit = Button(
            text = "Submit",
            font_size = 20, 
            background_color = [2.5, 1, 0, 1],
        )

        # bind method
        self.submit.bind(on_press=self.OnPress)

        # add button to component
        self.add_widget(self.submit)



    # method for pressing button
    def OnPress(self, instance):
        name = self.name.text
        style = self.style.text
        flavor = self.flavor.text
        
        print("name: ", name, "style: ", style, "flavor: ", flavor)

        self.name.text = ""
        self.style.text = ""
        self.flavor.text = ""

            
        







class Myapp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    Myapp().run()


