from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import ScreenManager
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.properties import StringProperty, NumericProperty
Window.size = (350, 550)



class Command(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_size = 16

class Response(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_size = 15

class ResponseImage(Image):
    source = StringProperty()


class ChatBot(MDApp):

    def change_screen(self, name):
        screen_manager.current = name
    
    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("splash.kv"))
        screen_manager.add_widget(Builder.load_file("main.kv"))
        screen_manager.add_widget(Builder.load_file("chat.kv"))
        return screen_manager
    
    def on_start(self):
        Clock.schedule_once(self.main, 10)
        

    def main(self, *args):
        screen_manager.current = "main"

    def bot_name(self):
        if screen_manager.get_screen('main').bot_name.text != "":
            screen_manager.get_screen('chats').bot_name.text = screen_manager.get_screen('main').bot_name.text
            screen_manager.current = "chats"

    def response(self, *args):
        response = ""
        if value == "Hello" or value == "hello":
            response = f"Hello. I am your Personal Assistant, {screen_manager.get_screen('chats').bot_name.text}."

        elif value == "How are you?" or value == "how are you?" or value == "How are you" or value == "how are you":
            response = "I'am doing well, Thanks!"

        elif value == "Are you a male or female?":
            response = "LOL, I am not gender specific."

        elif value == "Classify the Job Sections":
            response = "1. Software Engineering\n2. Digital Marketing\n3. Airtificial Intelligence\n4. UI/UX Designing\n5. Web Development and Designing\n\nNOTE: All with a minimum of one year experience."

        elif value == "What is your main purpose?":
            response = "To provide jobs to individuals who are having a hard time finding a profitable job and to reduce the level of unemplpyment all over the world."

        elif value == "How many jobs are available?":
            response = "3"
    
        elif value == "List the jobs under Software Engineering":
            response = "1. Python Programmer\n2. Java Programmer\n3. Website Developer"
            
        elif value == "How do I register?" or value == "What do I do?":
            response = "Here is the name of the website to visit\nAIIJCjobfinder.com\n\nOr, you can register for it on this app, if you want it, type REGISTER"

        elif value == "REGISTER":
            response = "Alright\n\nLOADING..."
            # response = "Loading Timeout!!!"

        elif value == "Later" or value == "Bye" or value == "Bye bye" or value == "Good Bye":
            response = "Bye, Expecting you soon\n\nPlease kindly close the app, Thanks."

        elif value == "OK, Thank you" or value == "Alright, Thank you" or value == "thank you" or value == "Thank you":
            response = "You are welcome."
        
        elif value == "Sorry":
            response = "No problem."

        elif value == "ok" or value == "OK" or value == "Ok":
            response = "Yeah!!!"

        elif value == "Images":
             screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source = "Emmalex5-05.jpg"))

        elif value == "Images1":
            screen_manager.get_screen('chats').chat_list.add_widget(ResponseImage(source = "Emmalex5-05.jpg"))

        else:
            response = "Sorry, could you repeat that again?"
        screen_manager.get_screen('chats').chat_list.add_widget(Response(text = response, size_hint_x = .68))


    def send(self):
        global size, halign, value
        if screen_manager.get_screen('chats').text_input != "":
            value = screen_manager.get_screen('chats').text_input.text
            if len(value) < 6:
                size = .22
                halign = "center"
            elif len(value) < 11:
                size = .32
                halign = "center"
            elif len(value) < 16:
                size = .45
                halign = "center"
            elif len(value) < 21:
                size = .58
                halign = "center"
            elif len(value) < 26:
                size = .71
                halign = "center"
            else:
                size = .77
                halign = "left"
            screen_manager.get_screen('chats').chat_list.add_widget(Command(text = value, size_hint_x = size, halign = halign))
            Clock.schedule_once(self.response, 2)
            screen_manager.get_screen('chats').text_input.text = ""

    def read_first(self):
        pass


if __name__=="__main__":
    ChatBot().run()
        