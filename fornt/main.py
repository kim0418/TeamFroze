from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle

fontName = 'NanumGothicBold.ttf'

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.padding = 10
        self.spacing = 10

        self.cols = 1
        self.img=Image(source="fridge.png",size=(200,200))
        self.add_widget(self.img)
        
        self.inside=GridLayout()
        self.inside.cols=2
        self.inside.add_widget(Label(text='ID', 
            font_name=fontName,
            font_size=20))
        self.username = TextInput(multiline=False)
        self.inside.add_widget(self.username)
        
        self.inside.add_widget(Label(text='Password',
            font_name=fontName,
            font_size=20))
        self.password = TextInput(password=True, multiline=False)
        self.inside.add_widget(self.password)
        
        self.add_widget(self.inside)
        
        self.submit=Button(text='Login',font_name=fontName,font_size=20)
        
        self.add_widget(self.submit)
        

class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run() 
