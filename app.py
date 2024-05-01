import pyttsx3 
from decouple import config
from datetime import datetime
import speech_recognition as sr
from random import choice
from conv import random_text
# from pynput import keyboard
import keyboard
import os
# import subprocess as sp
from online import find_my_ip, search_on_google, search_on_wikipedia, youtube, get_news, chatgpt
import time
from vscode import createfile



engine = pyttsx3.init("nsss")
# engine.say("how are you?")
# engine.runAndWait()
engine.setProperty("rate", 200)
engine.setProperty("volume", 1.5)

# voices :

# voices = engine.getProperty("voices")

# # engine.setProperty("voice", voices[0].id) ##changing index, changes voices. o for male
# engine.setProperty("voice", voices[1].id) ##changing index, changes voices. 1 for female

USER = config("USER")
HOSTNAME = config("BOT")

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    
    with sr.Microphone() as source :
        print("Listening...")
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)
    
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language = "en-in")
        print(query)

        if "exit" in query or "stop" in query:
            hour = datetime.now().hour

            if (hour >= 21) and (hour < 6):
                speak("Good Night Sir, Take Care")
            else :
                speak("Have a goodday sir") 
            
            exit()
        
        else :
           speak(choice(random_text))
    except Exception:
        speak("Sorry I couldn't understand. Can you please repeat?")
        query = "None"
    return query


# listening = False

# def start_listening():
#     global listening
#     listening = True
#     print("Started Listening...")


# def pause_listening():
#     global listening
#     listening = False
#     print("Stopped Listening...")






def greetme():
    hour = datetime.now().hour

    if (hour >= 6) and (hour <= 12) :
        speak(f"Good Morning {USER}")
    elif (hour >= 12) and (hour <= 16):
        speak(f"Good Afternoon {USER}")
    elif (hour >= 16) and (hour <= 20):
        speak(f"Good Evening {USER}")
    speak(f"Hi I'm {HOSTNAME}. How may I assist you?")

if __name__ == "__main__":
    # speak("Hi I'm Your virtual assistant")
    greetme()

    while True:

        query = take_command().lower()

        if "how are you" in query:
            speak("I'm absolutely fine sir")
        
        elif "open terminal" in query:
            speak("opening terminal")
            os.system("open /System/Applications/Utilities/Terminal.app")
            exit()
        elif "open whatsapp" in query:
            speak("opening whatsapp")
            os.system("open /Applications/WhatsApp.app")
            exit()
        elif "open facetime" in query:
            speak("opening facetime")
            os.system("open /System/Applications/FaceTime.app")
            exit()
            
        elif "open asphalt 8" in query:
            speak("opening asphalt 8")
            os.system("open /Applications/Asphalt8.app")
            exit()

        elif "open v s code" in query:
            speak("opening asphalt 8")
            os.system("open /Applications/Code.app")
            exit()
        
        elif "open discord" in query:
            speak("opening discord")
            os.system("open /Applications/Discord.app")
            exit()
        elif "ip address" in query or "ip" in query:
            ip_address = find_my_ip()
            speak(
                f"your ip address is {ip_address}"
            )
            print(f"your IP address is {ip_address}")
            exit()

        elif "youtube" in query:
            speak("what video you want to play?")
            video = take_command().lower()
            youtube(video)
            time.sleep(3)
        
        elif "open google" in query:
            speak("what you want to search on google?")
            q = take_command().lower()
            search_on_google(q)
            exit()
        
        elif "wikipedia" in query:
            speak("what you want to search on wikipedia?")
            q = take_command().lower()
            search_on_wikipedia(q)
            exit()

        elif "give me news" in query:
            speak("I'm reading out the latest news of today")
            speak(get_news())
            print(*get_news(), sep="\n")


        elif "create" in query:
            createfile(query)
        

      