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

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', id)
recognizer=sr.Recognizer()
engine.setProperty('rate', 180)
id ="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"

cookie_dict={
    "__Secure-1PSID" : "fwiOW5DvLwNZHJ1RIWdpqCEgR3R8rDz2d2Le-DT3XpiiFG6G30OWzi9tuGd5TWnP5QonLA.",    
    "__Secure-1PSIDTS" : "sidts-CjIBPVxjSnU97U2zSnNp1S48jsXVy2VNQ4IwO4MwhGpcBnYD64XZkCX1KFy_LnH4cR8B-xAA",    
    "__Secure-1PSIDCC" : "ABTWhQHh1SdFU51tFukepelnkARQIH9UTompI_3rqIu8-RIEjxs95ZLsL0PlN4_UqHAYgh0LmN4"    
}

bard = BardCookies(cookie_dict=cookie_dict)

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

    return query

def open_website(url):
    webbrowser.open(url)

def handle_command(query, window):
    query = query.lower()

    if 'open youtube' in query:
        speak("Opening YouTube...")
        open_website("https://www.youtube.com")

    elif 'open google' in query:
        speak("Opening Google...")
        open_website("https://www.google.com")

    elif 'open facebook' in query:
        speak("Opening Facebook...")
        open_website("https://www.facebook.com")

    elif 'what\'s the time' in query:
        strTime = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {strTime}")

    elif 'thanks' in query:
        speak("It's my pleasure, sir!")

    elif "who made you" in query:
        speak("I was made by an student of Mokshada school, Who is studying in grade 9, Named Umang.")

    elif "what is your name" in query:
        speak("My name is Sahayogi.")

    elif 'hello' in query:
        speak("Hi there, how can I assist you?")

    elif 'open reddit' in query:
        speak("Opening Reddit...")
        open_website("https://www.reddit.com")

    elif 'open instagram' in query:
        speak("Opening Insta gram...")
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

    elif 'play some english songs' in query:
        en_songs  = [ 'MAIN\\English songs\\Counting Stars.mp3' ,'MAIN\\English songs\\Gone gone gone.mp3','MAIN\\English songs\\Toxic.mp3']
        en_random_songs = random.choice(en_songs)
        if en_random_songs == 'MAIN\\English songs\\Counting Stars.mp3':
            speak('Playing Counting Stars!')
        if en_random_songs == 'MAIN\\English songs\\Gone gone gone.mp3':
            speak('Playing Gone Gone Gone!')
        if en_random_songs == 'MAIN\\English songs\\Toxic.mp3':
            speak('Playing Toxic!')
        os.startfile(en_random_songs)
    
    elif 'play some nepali songs' in query:
        np_songs = ['MAIN\\Nepali songs\\Buddha Was Born In Nepal  .mp3','MAIN\\Nepali songs\\Gauchha Geet Nepali.mp3','MAIN\\Nepali songs\\Karke Nazar.mp3','MAIN\\Nepali songs\\Man Magan.mp3','MAIN\\Nepali songs\\Oye Timro chha ki cchaina koi.mp3','MAIN\\Nepali songs\\Pashina ko jaalale.mp3','MAIN\\Nepali songs\\Rato ra Chandra surjye.mp3','MAIN\\Nepali songs\\Yo nepali shir Uchali.mp3']
        np_random_songs = random.choice(np_songs)
        if np_random_songs == 'MAIN\\Nepali songs\\Buddha Was Born In Nepal  .mp3':
            speak('Playing Buddha was born in Nepal')
        if np_random_songs == 'MAIN\\Nepali songs\\Gauchha Geet Nepali.mp3':
            speak('Playing Gauchha Geet Nepali')
        if np_random_songs == 'MAIN\\Nepali songs\\karke Nazar.mp3':
            speak('Playing Karke Nazar')
        if np_random_songs == 'MAIN\\Nepali songs\\Man Magan.mp3':
            speak('Playing Man Magan')
        if np_random_songs == 'MAIN\\Nepali song\\/Oye Timro chha ki cchaina koi.mp3':
            speak('Playing Oye Timro Chha Ki Chhaina Koi')
        if np_random_songs == 'MAIN\\Nepali songs\\Pashina ko jaalale.mp3':
            speak('Playing Pashina Ko Jaalale')
        if np_random_songs == 'MAIN\\Nepali songs\\Rato ra Chandra surjye.mp3':
            speak('Playing Rato Ra Chandra Surjye')
        if np_random_songs == 'MAIN\\Nepali songs\\Yo nepali shir Uchali.mp3':
            speak('Playing Yo Nepali Shir Uchali')

        os.startfile(np_random_songs)

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

    elif 'what are you' in query:
        speak('I am a Voice Assistant, Which will help you control your Computer using your own voice')

    else:
        speak("I'm sorry, I didn't understand that command. Can you please repeat?")
        return takeCommand()

def process_command():
    query = takeCommand()
    handle_command(query)

def clean_up_text(text):
    cleaned_text = text.replace('*', '.').replace('@', 'at').replace(':','.').replace('.','. ')
    return cleaned_text

def clean_up_url(text):
    cleaned_url = text.replace('dot', '.').replace('slash', '/')
    return cleaned_url
 
def create_gui():
    window = tk.Tk()
    window.title("Sahayogi")

    window.geometry("400x300+300+150")

    label = tk.Label(window, text="Sahayogi", font=("Monaco", 24))
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

    window.mainloop()


if __name__ == "__main__":

    wishMe()
    create_gui()
