import speech_recognition as sr
import pyttsx3
import time as t
import datetime

#initializing voice engine
engine=pyttsx3.init()
engine.setProperty('rate',170)

def speak(text):
    engine=pyttsx3.init()
    engine.setProperty('rate',170)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source,duration=1)
        audio=r.listen(source)

    try:
        command=r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        return ""

speak("Hello there, I am Jarvis. How can I help you?")

while True:
    command = listen()
    if command=="":
        continue

    elif "hello" in command:
        speak("Hello! Nice to talk to you.")
        t.sleep(0.5)
        continue
    elif "time" in command:
        import datetime
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {current_time}")
        t.sleep(0.5)
        continue
    elif "stop" in command:
        speak("Goodbye!")
        break
    