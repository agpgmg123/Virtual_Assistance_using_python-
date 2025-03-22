import wikipedia
import webbrowser
import os
import smtplib # it is used to send mail
import random
from dotenv import load_dotenv

#load environment variables
load_dotenv()

Email = os.getenv("Email")
password = os.getenv("Password")

class Taskmodule:
    def __init__(self, speech_module):
        self.speech_module = speech_module
    
    def open_website(self, site):
        webbrowser.open(site)

    def open_code(self, path):
        os.startfile(path)

    def tell_time(self):
        from datetime import datetime
        str_time = datetime.now().strftime("%H:%M:%S")
        self.speech_module.speak(f"Sir, the time is {str_time}")

    def search_wikipedia(self, query):
        try:
            result = wikipedia.summary(query, sentences=2)
            self.speech_module.speak("According to wikipedia : "+ result)
            print(result)
        except Exception as e:
            print(e)
            self.speech_module.speak("Soory, I could not find any information on wikipedia")
    def play_music(self, music_dir):
        if os.path.exists(music_dir):
            songs = [song for song in os.listdir(music_dir) if song.endswith("mp3")]
            if songs:
                song_to_play = random.choice(songs)
                os.startfile(os.path.join(music_dir, song_to_play))
            else:
                print("No music files found in the directory")
        else:
            print("Directory does not exist")
    def send_email(self, to, content):
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo() # this encrypts our connection
            server.strattls() # this is used to send data between server and client
            server.login(Email, to, content)
            self.speech_module.speak("Email has been sent successfully")
        except Exception as e:
            print(e)
            self.speech_module.speak("Sorry, I could not send the email")
if __name__=="__main__":
    class DummySpeechModule:
        def speak(self,text):
            print("Speak :", text)
    obj = DummySpeechModule()
    test_obj = Taskmodule(obj)

    # testing the open website method

    #uncomment this line to make the wikipedia facility available--->open_website("https://www.google.com")

    # testing the open_code method
    #test_obj.open_code("D:\\Python_Class\\python\\loops.ipynb")

    #test_obj.open_code("D:\\Python_Class\\Python Project\\mymusic.mp3")

    #test_obj.tell_time()

    test_obj.search_wikipedia("python programming")
    test_obj.search_wikipedia("virat kohli")
    test_obj.send_email("202401070197@mitaoe.ac.in","prakashKumarg2427@gmail.com")