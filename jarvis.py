import speech_recognition as sr
import pyttsx3
import time 
import datetime
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

#initializing voice engine
engine=pyttsx3.init()
engine.setProperty('rate',170)

def speak(text):
    
    print("Jarvis:", text)
    engine = pyttsx3.init('sapi5')   # force Windows driver
    engine.setProperty('rate', 170)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    time.sleep(0.3)

def listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source,duration=0.5)
        try:
            audio=r.listen(source,timeout=5,phrase_time_limit=5)
        except:
            print("Sorry, I did not hear you.")
            return ""

    try:
        command=r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""



speak("Hello there, I am Jarvis. How can I help you?")

while True:
    command = listen()
    if command=="":
        continue
    print("command received:", command)

    if "hello" in command:
        speak("Hello! Nice to talk to you.")
        time.sleep(0.5)
        continue
    elif "time" in command:
        
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {current_time}")
        time.sleep(0.5)
        continue
    elif "jarvis" in command:
        speak("Yes, I am here.")
    elif "stop" in command:
        speak("Goodbye!")
        break

    else:
        speak("Sorry, I don't know how to respond to that yet.")