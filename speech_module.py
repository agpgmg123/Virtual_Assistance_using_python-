#step 1
#this module is responsible for speech recognition and speech synthesis.
#it also uses the date time module to get the current time.

#importing necessary libraries

import pyttsx3 #--->convert text to speech conversion library
import speech_recognition as sr # speech recognition library, it converts speech to text
import datetime # library to get the current date and time

engine = pyttsx3.init() # intializin the pyttsx3 engine

class SpeechModule:
    # the__init__method intializes the pyttsx3 engine and the sets the voice properly.
    def __init__(self):
        self.engine = pyttsx3.init('sapi5') # sapi5 is a microsoft speech API
        voices = self.engine.getProperty('voices') # getting the voices
        self.engine.setProperty('voice', voices[0].id) # setting the voice


    # the speaks method takes audio as string as input and speaks it using the pyttsx3 engine.
    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()
    
    def wish_me(self):
        hour = int(datetime.datetime.now().hour)
        if 0 <= hour < 12:
            greeting = "Good Morning!"
        elif 12 <= hour < 18:
            greeting = "Good Afternoon!"
        else:
            greeting = "Good Evening!"
        print(greeting)
        self.speak(greeting)
        self.speak("I am your assistant. Please tell me how can i help you")

    def take_command(self):
        recoginizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            recoginizer.pause_threshold = 1
            audio = recoginizer.listen(source)
        try:
            print("Recognizing...")
            query = recoginizer.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query.lower()
        except Exception as e:
            print("Say that again please...")

            return "None"
        
#_name_ is a built-in variable which evaluates to the name of the current module.
if __name__ == "__main__":
    sp = SpeechModule()
    sp.speak("Hello Aashi")
    sp.wish_me()
    sp.take_command()

# python -m venv virtualenvironment_name---->python -m venv myenv
#myenv\scripts\activate



