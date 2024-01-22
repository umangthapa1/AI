import sys
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import tkinter as tk
import os
import wikipedia
import pywhatkit

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
recognizer=sr.Recognizer()
engine.setProperty('rate', 180)

window = tk.Tk()
window.title("Voice Assistant")



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

    speak("I am Sahayogi. How may I assist you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Clearing Background Noises!")
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        print("Listening...")
        speak("Listening...")
        r.pause_threshold = 1
        recordedaudio=recognizer.listen(source)
    try:
        text=recognizer.recognize_google(recordedaudio,language='en_US')
        print("Recognizing...")
        speak("Recognizing...")
        query = r.recognize_google(recordedaudio)
        print(f"User Said: {query}\n")
        if 'bye bye' in query.lower():
            speak("Goodbye! See you soon!")
            window.destroy()  
            sys.exit()
            
    except Exception as e:
        print("Say that again please...")
        return "None"

    return query

def open_website(url):
    webbrowser.open(url)

def handle_command(query):
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
        speak(f"Sir, the time is {strTime}")

    elif 'thanks' in query:
        speak("It's my pleasure, sir!")

    elif "who made you" in query:
        speak("I was made by an student of Mokshada school, Who is studying in grade 9, Named Umang.")

    elif "what is your name" in query:
        speak("My name is Sahayogi.")

    elif "hello" in query:
        speak("Hi")

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


    else:
        speak("I'm sorry, I didn't understand that command. Can you please repeat?")
        start_listening

def process_command():
    query = takeCommand()
    handle_command(query)

def create_gui():
    label = tk.Label(window, text="Jarvis", font=("Arial", 24))
    label.pack(pady=20)

    text_box = tk.Text(window, height=10, width=40)
    text_box.pack(pady=10)

    def display_text(text):
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, text)

    def process_command_with_display():
        query = takeCommand()
        display_text("User Said: " + query + "\n")
        handle_command(query)

    def start_listening(event):
        process_command_with_display()

    
    window.bind("<space>", start_listening)

    window.mainloop()

if __name__ == "__main__":
    wishMe()
    create_gui()