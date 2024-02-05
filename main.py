import sys
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import tkinter as tk
import os
import pywhatkit
import random 
import pyjokes
from bardapi import BardCookies
import threading
import requests
from bs4 import BeautifulSoup
import json

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
recognizer=sr.Recognizer()
engine.setProperty('rate', 180)

cookie_dict={
    "__Secure-1PSID" : "fwiOW5DvLwNZHJ1RIWdpqCEgR3R8rDz2d2Le-DT3XpiiFG6G30OWzi9tuGd5TWnP5QonLA.",    
    "__Secure-1PSIDTS" : "sidts-CjIBPVxjSnU97U2zSnNp1S48jsXVy2VNQ4IwO4MwhGpcBnYD64XZkCX1KFy_LnH4cR8B-xAA",    
    "__Secure-1PSIDCC" : "ABTWhQHh1SdFU51tFukepelnkARQIH9UTompI_3rqIu8-RIEjxs95ZLsL0PlN4_UqHAYgh0LmN4"    
}

dataset=[
    {
        "tag": "greetings",
        "ques": [
            "hey",
            "hello",
            "what's up",
            "hola"
        ],
        "respo": [
            "Hi there! How can I help you?",
            "Greetings! What do you need today?"
        ]
    },
    {
        "tag": "care",
        "ques": [
            "how are you",
            "what's up"
        ],
        "respo": [
            "I am doing well, thank you."
        ]
    },
    {
        "tag": "farewell",
        "ques": [
            "goodbye",
            "see you later",
            "farewell"
        ],
        "respo": [
            "Goodbye! Take care.",
            "See you later! If you need anything, I'm here.",
            "Farewell! Have a great day!"
        ]
    },
    {
        "tag": "thanks",
        "ques": [
            "thank you",
            "thanks"
        ],
        "respo": [
            "You're welcome! Don't mention it.",
            "No problem! Thanks for your kind words.",
            "You're very welcome! Enjoy the rest of your day."
        ]
    },
    {
        "tag": "abt_questions",
        "ques": [
            "what are you",
            "what can you do"
        ],
        "respo": [
            "I am a Voice Assistant, Which will help you control your Computer using your own voice"
        ]
    },
    {
        "tag": "cre_questions",
        "ques": [
            "who made you",
            "who created you",
            "what is the name of your creator",
            "what is the name of your developer"
        ],
        "respo": [
            "I was developed by a ninth grader. My creator's name is Umang Thapa",
            "I was made by an student of Mokshada school, Who is studying in grade 9, Named Umang."
        ]
    },
    {
        "tag": "name_questions",
        "ques": [
            "what should i call you",
            "how should I address you",
            "what is your name"
        ],
        "respo": [
            "You can call me SAHAYOGI or simply ASSISTANT",
            "My name is SAHAYOGI"
        ]
    }
]

bard = BardCookies(cookie_dict=cookie_dict)

window = tk.Tk()
window.title("S.A.H.A.Y.O.G.I")

def load_dataset(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

""" dataset_file = 'Finals/dataset.json'
dataset = load_dataset(dataset_file) """

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am your personal Sahayogi. How may I assist you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...")
        speak("Listening...")
        r.pause_threshold = 1 
        recordedaudio = recognizer.listen(source,0,8)
    try:
        text = recognizer.recognize_google(recordedaudio, language='en_US')
        print("Recognizing...")
        speak("Recognizing...") 
        query = r.recognize_google(recordedaudio)
        print(f"User Said: {query}\n")
        if 'bye' in query.lower():
            speak("Goodbye! See you soon!")
            window.destroy()  
            sys.exit()
        return query
    except Exception as e:
        print("Say that again please...")
        return "None"

def open_website(url):
    webbrowser.open(url)

def handle_command(query, window):
    query = query.lower()

    for conversation in dataset:
        tag = conversation.get("tag", "")
        ques_list = conversation.get("ques", [])
        respo_list = conversation.get("respo", [])

        for ques in ques_list:
            if ques.lower() in query:
                respo = random.choice(respo_list)
                speak(respo)
                return

    if 'open youtube' in query:
        speak("Opening YouTube...")
        open_website("https://www.youtube.com")

    elif 'open google' in query:
        speak("Opening Google...")
        open_website("https://www.google.com")

    elif 'open facebook' in query:
        speak("Opening Facebook...")
        open_website("https://www.facebook.com")

    elif 'what is the time' in query:
        strTime = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {strTime}")

    elif 'open reddit' in query:
        speak("Opening Reddit...")
        open_website("https://www.reddit.com")

    elif 'open instagram' in query:
        speak("Opening Instagram...")
        open_website("https://www.instagram.com/")

    elif 'open github' in query:
        speak("Opening GitHub...")
        open_website("https://www.github.com")

    elif 'open chat gpt' in query:
        speak("Opening ChatGPT...")
        open_website("https://chat.openai.com/")
    
    elif 'open messenger' in query:
        speak("Opening Messenger...")
        open_website("https://www.messenger.com/")

    elif 'show me my mails' in query:
        speak("Sure sir...")
        open_website("https://mail.google.com/")

    elif 'open twitter' in query:
        speak("Sure sir...")
        open_website("https://twitter.com")

    elif 'open visual studio code' in query:
        speak("Opening Visual Studio Code...")
        code_path = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
        os.startfile(code_path)
        
    elif 'open browser' in query:
        speak("Opening browser...")
        code_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
        os.startfile(code_path)

    elif 'shut down' in query:
        speak("Shutting down the PC...")
        os.system("shutdown /s /t 0")  

    elif 'restart' in query:
        speak("Restarting the PC...")
        os.system("shutdown /r /t 0") 

    elif 'sleep' in query:
        speak("Putting the PC to sleep...")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

    elif 'open task manager' in query:
        speak("Opening Task Manager...")
        os.system("taskmgr")

    elif 'open control panel' in query:
        speak("Opening Control Panel...")
        os.system("control")

    elif 'open command prompt' in query:
        speak("Opening Command Prompt...")
        os.system("cmd")

    elif 'open system settings' in query:
        speak("Opening System Settings...")
        os.system("ms-settings:")

    elif 'empty recycle bin' in query:
        speak("Emptying the Recycle Bin...")
        os.system("cmd /c echo Y|PowerShell.exe -NoProfile -Command Clear-RecycleBin")

    elif 'tell me about your school' in query:
        speak('MOKSHADA SCHOOL welcomes all our dear students, parents, and well-wishers in the holy area of Pashupatinath. It is situated at Mokshada Nagar, Kumarigal, Kathmandu. Since 1997, the school has carried the legacy of progressive teaching-learning. Besides, the pedagogical approach has been transformed now and then with the need of time and learning scenarios. Moreover, the qualified teachers, learning culture, tech-friendly platform, and multi-dimensional trends of academics are the enhancing factors of the school. Acknowledging quality education to the learners has centred the major objective of the school. Henceforth, the motto of the school is “Read, Lead and Succeed”. Learners will merely get the feel of learning home here.')
        speak('Thank you!')

    elif 'tell me a joke' in query:
        joke=pyjokes.get_joke()
        speak(joke)
        print(joke)

    elif 'open a website' in query:
        speak('Sure! Please say the full URL of the website you want to open.')
        url_query = takeCommand()
        cleaned_url = clean_up_url(url_query)
        speak(f'opening website {cleaned_url}')
        webbrowser.open(cleaned_url)

    elif 'let me ask you something' in query:
        speak('Sure! ask me anything')
        topic = takeCommand()
        speak('Searching...')
        Reply = bard.get_answer(topic)['content']
        cleaned_reply = clean_up_text(Reply)
        speak(cleaned_reply)

    elif 'open the portfolio of your creator' in query:
        speak('Opening the portfolio of my creator!')
        webbrowser.open('https://umangthapa.netlify.app')

    elif 'play a song' in query:
        speak("Which song would you like to play?")
        song = takeCommand()
        pywhatkit.playonyt(song)
        speak("Playing " + song + "on youtube")

    elif 'temperature'  in query:
        search = 'temperature in kathmandu'
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temperature = data.find("div", class_="BNeawe").text
        speak(f"The current temperature is {temperature}")

    elif 'show me something in youtube' in query:
        speak('What do you want to see in YouTube?')
        video_query = takeCommand()
        pywhatkit.playonyt(video_query)
        speak('Playing' + video_query + "in youtube")

    else:
        speak("I'm sorry, I didn't understand that command. Can you please repeat?")
        return takeCommand()

def process_command():
    query = takeCommand()
    handle_command(query, window)

def clean_up_text(text):
    cleaned_text = text.replace('*', '.').replace('@', 'at').replace(':','.').replace('.','. ')
    return cleaned_text

def clean_up_url(text):
    cleaned_url = text.replace('dot', '.').replace('slash', '/')
    return cleaned_url

wake_up_phrase = ("hey assistant", "wake up assitant")

def listen_for_wake_up():
    while True:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            print("Listening for Wake Up Command...")
            audio = recognizer.listen(source, 0, 5)

        try:
            text = recognizer.recognize_google(audio, language='en_US').lower()
            if any(phrase in text for phrase in wake_up_phrase):
                print("Wake Up Command Detected!")
                speak("Yes, how can I assist you?")
                process_command()
        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

def create_gui():

    window.geometry("400x300+300+150")

    label = tk.Label(window, text="S.A.H.A.Y.O.G.I", font=("Monaco", 24))
    label.pack(pady=20)

    text_box = tk.Text(window, height=8, width=40)
    text_box.pack(pady=10)

    def display_text(text):
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, text)

    def process_command_with_display():
        query = takeCommand()
        display_text("User Said: " + query + "\n")
        handle_command(query, window)

    def start_listening(event):
         threading.Thread(target=process_command_with_display).start()

    window.bind("<space>", start_listening)
    threading.Thread(target=listen_for_wake_up).start()

    window.mainloop()

if __name__ == "__main__":
    wishMe()
    create_gui()
