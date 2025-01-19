from kivy.app import App
from kivy.uix.label import Label

class HelloApp(App):
   def build(self):
    l1 = Label(text="Hello World", font_size=100)
    return l1

app = HelloApp()
app.run()
