# Jarvis Voice Assistant (AI-Powered)

A Python-based voice-controlled AI assistant inspired by Jarvis. It listens to user commands, processes them, and responds intelligently using speech recognition, text-to-speech, and a large language model (Google Gemini).

---

## Features

### Voice Recognition

* Listens to user input through the microphone
* Converts speech to text using SpeechRecognition

### Text-to-Speech

* Converts responses into speech using pyttsx3
* Provides real-time voice feedback

### AI Integration

* Uses Google Gemini API for intelligent responses
* Can handle:

  * General questions
  * Explanations
  * Conversations
  * Jokes

### Built-in Commands

* Tell the current time
* Respond to greetings
* Stop or exit the assistant

### Real-time Interaction

* Continuously listens for commands
* Responds dynamically based on input

### Secure API Handling

* API key stored in a .env file
* Protected using .gitignore

---

## Tech Stack

* Python
* SpeechRecognition
* PyAudio
* pyttsx3
* Google Generative AI (Gemini)
* python-dotenv

---

## Project Structure

Jarvis/
│── jarvis.py
│── .env (not uploaded)
│── .gitignore
│── README.md
│── .venv/

---

## Installation

### 1. Clone the repository

git clone https://github.com/your-username/jarvis.git
cd jarvis

---

### 2. Create virtual environment

python -m venv .venv

Activate it:

Windows:
.venv\Scripts\activate

---

### 3. Install dependencies

pip install -r requirements.txt

Or install manually:
pip install pyttsx3 SpeechRecognition pyaudio google-generativeai python-dotenv

---

### 4. Add your API key

Create a file named .env and add:
GEMINI_API_KEY=your_api_key_here

---

### 5. Run the program

python jarvis.py

---

## Example Commands

* Hello
* What is the time
* Explain artificial intelligence
* Tell me a joke
* Stop

---

## Future Improvements

* Add conversation memory
* Add wake word activation
* Open applications and browser
* Play music or YouTube
* Add graphical user interface
* Improve response speed

---

## Notes

* Ensure microphone is properly connected
* Internet connection is required for AI responses
* Do not upload the .env file to GitHub

---


