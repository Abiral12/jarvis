import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit
from datetime import datetime
import webbrowser
import subprocess
import os



def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}\n")
        except sr.UnknownValueError:
            print("Sorry sir, but I did not understand that. Can you say that again please.")
            return ""
        except sr.RequestError:
            print("Could not request results; check your network connection.")
            return ""
    return command.lower()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def handle_command(command):
    if 'wikipedia' in command:
        search_query = command.replace('wikipedia', '').strip()
        try:
            results = wikipedia.summary(search_query, sentences=2)
            print(results)
            speak(results)
        except wikipedia.exceptions.DisambiguationError as e:
            speak("There are multiple results. Please be more specific.")
        except wikipedia.exceptions.PageError:
            speak("Sorry, I could not find any results.")

    elif 'play' in command:
        song = command.replace('play', '').strip()
        speak(f'Playing {song}')
        pywhatkit.playonyt(song)

    elif 'hello' in command:
        speak('Hello sir! How are you?')

    elif 'how are you' in command:
        speak('I am doing great sir, thanks for asking. What can i do for you, sir?')

    elif 'time' in command:
        now = datetime.now().strftime('%H:%M')
        speak(f'The current time is {now}')

    elif "where is" in command:
        data = command.split(" ")
        location = data[2]
        speak(f"Hold on sir, I will show you where {location} is.")
        webbrowser.open(f"https://www.google.com/maps/place/{location}/")

    elif "what is your name" in command:
        speak("My name is jarvis and I am a virtual assistant")

    elif "youtube" in command:
        speak("Opening youtube")
        webbrowser.open("https://www.youtube.com/")

    elif "facebook" in command:
        speak("Opening facebook")
        webbrowser.open("https://www.facebook.com/")

    elif "monkey" in command:
        speak("Opening monkey type")
        webbrowser.open("https://monkeytype.com/")

    elif "chat gpt" in command:
        speak("Opening chatgpt")
        webbrowser.open("https://chat.openai.com/")

    elif "calculator" in command:
        speak("Opening calculator")
        subprocess.run(['calc.exe'])

    elif "notepad" in command:
        speak("Opening notepad")
        subprocess.run(['notepad.exe'])

    elif "who is" in command:
        speak("gathering the data of dipson rimal.")
        speak("Behold dipson is the greatest human ever stepped on planet earth, without his existence even jesus would not have been formed. He is a god in hunans form, a gigachad, batman who saves the city at night")


    else:
        speak("Sorry sir, but I did not understand that. Can you say that again please?")

def main():
    def greet_user():
        hour = datetime.now().hour
        if (hour >= 6) and (hour < 12):
            speak(f"Good Morning sir")
            speak(f"I am JARVIS . How may I assist you today?")
        elif (hour >= 12) and (hour < 16):
            speak(f"Good afternoon sir")
            speak(f"I am JARVIS . How may I assist you today?")
        elif (hour >= 16) and (hour < 24):
            speak(f"Good Evening sir")
            speak(f"I am JARVIS . How may I assist you today?")
    greet_user()
    while True:
        command = listen()
        if 'exit' in command or 'leave' in command:
            speak("Goodbye sir, Have a great day!")
            break
        handle_command(command)

if __name__ == "__main__":
    main()
