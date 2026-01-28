
import speech_recognition as sr
import pyttsx3
import time
import datetime
import os
from google import genai 

api_key = os.getenv("GEMINI_API_KEY")
if api_key is None:
    print("Error: GEMINI_API_KEY not found. Make sure you set it in environment variables.")
    exit()
client=genai.Client(api_key=api_key)
def ai_brain(question):
    try:
        response=client.generate(
            model="gemini-pro",
            prompt=question,
            temprature=0.3,
            max_output_tokens=256
        )
        return response.output_text
    except Exception as e:
        print("AI ERROR:", e)
        return "Sorry, I am having trouble thinking right now."

def speak(text):

    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    del engine
    time.sleep(0.3)  


def listen():
    """Listen to user voice and return as text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.6)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        return ""


def ai_brain(question):
    """Fallback AI brain using Gemini API"""
    try:
        response = model.generate_content(question)
        return response.text
    except:
        return "Sorry, I am having trouble thinking right now."

#  MAIN PROGRAM 
speak("Hello there, I am Jarvis. How can I help you?")

while True:
    command = listen()
    
    # ignore very short or empty commands
    if command == "" or len(command.split()) < 2:
        continue

    
    if "hello" in command:
        speak("Hello! Nice to talk to you.")

    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {now}")

    elif "stop" in command or "exit" in command:
        speak("Goodbye!")
        break

    # a AI brain for anything else
    else:
        answer = ai_brain(command)
        speak(answer)
import os
print(os.getenv("GEMINI_API_KEY"))
