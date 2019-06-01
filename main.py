import kivy

from kivy.app import App

from kivy.uix.label import Label

from kivy.uix.gridlayout import GridLayout

from kivy.uix.button import Button



class stuff(GridLayout):

    def __init__(self):

        super().__init__()

        self.cols = 1



        self.words = GridLayout()

        self.words.cols = 4



        t = 0





        self.add_widget(Label(text=str(t), halign="left"))



        self.add_widget(self.words)

        self.words.add_widget(Button(text="9"))

        self.words.add_widget(Button(text="8"))

        self.words.add_widget(Button(text="7"))

        self.words.add_widget(Button(text="x"))

        self.words.add_widget(Button(text="6"))

        self.words.add_widget(Button(text="5"))

        self.words.add_widget(Button(text="4"))

        self.words.add_widget(Button(text="÷"))

        self.words.add_widget(Button(text="3"))

        self.words.add_widget(Button(text="2"))

        self.words.add_widget(Button(text="1"))

        self.words.add_widget(Button(text="+"))

        self.words.add_widget(Button(text="(-)"))

        self.words.add_widget(Button(text="0"))

        self.words.add_widget(Button(text="C"))

        self.words.add_widget(Button(text="-"))





class Calculator(App):

    def build(self):

        self.icon = "c03428568.jpg"

        return stuff()



if __name__ == "__main__":

    Calculator().run()