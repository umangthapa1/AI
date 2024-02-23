import sys
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import pywhatkit
import random 
import pyjokes
import threading
import requests
from bs4 import BeautifulSoup
import json
import google.generativeai as genai
import google.ai.generativelanguage as glm
import pyautogui
import time
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1146, 641)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Downloads/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("background-color: bacl\n"
        "")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 140, 361, 311))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../Downloads/R.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(680, 360, 461, 271))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../../Downloads/cyberpunk-retro-futuristic-hud-animation-for-live-streaming-display-overlay-and-copy-space-in-neon-light-color-free-video.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(340, 10, 551, 91))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../../Downloads/text-1706882966116 (1).png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 510, 51, 41))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../../../Downloads/discord-logo-2-1.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(86, 502, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("color: white\n"
        "")
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 560, 71, 61))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../../../Downloads/R (1).png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(86, 562, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: white\n"
        "")
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(710, 160, 361, 171))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("../../../Downloads/e8c5b61a18d49c20c48f0fe6d4839def4a96d970r1-444-250_00.gif"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(340, 220, 371, 301))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("../../../Downloads/R (1).gif"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.terminalOutputBox = QtWidgets.QPlainTextEdit(Dialog)
        self.terminalOutputBox.setGeometry(QtCore.QRect(730, 440, 361, 101))
        self.terminalOutputBox.setStyleSheet("color: rgb(19, 192, 235)")
        self.terminalOutputBox.setObjectName("terminalOutputBox")
        self.terminalOutputBox.setReadOnly(True)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "S.A.H.A.Y.O.G.I"))
        self.label_5.setText(_translate("Dialog", "dsc.gg/coders-hub"))
        self.label_7.setText(_translate("Dialog", "github.com/umangthapa1"))

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
recognizer=sr.Recognizer()
engine.setProperty('rate', 180)

genai.configure(api_key='AIzaSyCx4XlSXC26HjkPp4pZIcfNetxCDe72PjE')
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat()

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

def load_dataset(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    strTime = datetime.datetime.now().strftime("%I:%M %p")
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
        speak(f"The time is {strTime}")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
        speak(f"The time is {strTime}")
    else:
        speak("Good Evening!")
        speak(f"The time is {strTime}")
    speak("I am your personal Sahayogi. How may I assist you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        print("Listening...")
        speak("Listening...")
        recordedaudio = recognizer.listen(source,0,8)
    try:
        text = recognizer.recognize_google(recordedaudio, language='en_US')
        print("Recognizing...")
        speak("Recognizing...") 
        query = r.recognize_google(recordedaudio)
        print(f"User Said: {query}\n")
        if 'bye' in query.lower() or 'goodbye' in query.lower() or 'see you later' in query.lower() or 'farewell' in query.lower():
            speak("Goodbye! See you soon!")
            window.destroy()  
            sys.exit()
        return query
    except Exception as e:
        print("Say that again please...")
        return "None"

def open_website(url):
    webbrowser.open(url)

def handle_command(query, outputterminalBox):
    query = query.lower()

    for conversation in dataset:
        tag = conversation.get("tag", "")
        ques_list = conversation.get("ques", [])
        respo_list = conversation.get("respo", [])

        for ques in ques_list:
            if ques.lower() in query:
                respo = random.choice(respo_list)
                outputterminalBox.appendPlainText(respo)
                speak(respo)
                return

    if any(word in query for word in ['who', 'what', 'where', 'when', 'why', 'how', 'tell me about']):
        if 'temperature' in query:
            search = 'temperature in kathmandu'
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temperature = data.find("div", class_="BNeawe").text
            outputterminalBox.appendPlainText(f"The current temperature is {temperature}") 
            speak(f"The current temperature is {temperature}")
        elif ques.lower() in query:
            pass
        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            outputterminalBox.appendPlainText(f"The time is {strTime}")
            speak(f"The time is {strTime}")

        else:
            speak('Searching...')
            response = chat.send_message(query)
            cleaned_reply = clean_up_text(response.text)
            outputterminalBox.appendPlainText(cleaned_reply) 
            speak(cleaned_reply)

    elif 'open youtube' in query:
        outputterminalBox.appendPlainText("Opening Youtube...")
        speak("Opening YouTube...")
        open_website("https://www.youtube.com")

    elif 'open google' in query:
        outputterminalBox.appendPlainText("Opening Google...")
        speak("Opening Google...")
        open_website("https://www.google.com")

    elif 'open facebook' in query:
        outputterminalBox.appendPlainText("Opening Facebook...")
        speak("Opening Facebook...")
        open_website("https://www.facebook.com")

    elif 'what is the time' in query:
        strTime = datetime.datetime.now().strftime("%I:%M %p")
        outputterminalBox.appendPlainText(f"The time is {strTime}")
        speak(f"The time is {strTime}")

    elif 'open reddit' in query:
        speaoutputterminalBox.appendPlainText("Opening Reddit...")
        speak("Opening Reddit...")
        open_website("https://www.reddit.com")

    elif 'open instagram' in query:
        outputterminalBox.appendPlainText("Opening Instagram...")
        speak("Opening Instagram...")
        open_website("https://www.instagram.com/")

    elif 'open github' in query:
        outputterminalBox.appendPlainText("Opening GitHub...")
        speak("Opening GitHub...")
        open_website("https://www.github.com")

    elif 'open chat gpt' in query:
        outputterminalBox.appendPlainText("Opening ChatGPT...")
        speak("Opening ChatGPT...")
        open_website("https://chat.openai.com/")
    
    elif 'open messenger' in query:
        outputterminalBox.appendPlainText("Opening Messenger...")
        speak("Opening Messenger...")
        open_website("https://www.messenger.com/")

    elif 'show me my mails' in query:
        outputterminalBox.appendPlainText("Sure sir...")
        speak("Sure sir...")
        open_website("https://mail.google.com/")

    elif 'open twitter' in query:
        outputterminalBox.appendPlainText("Opening Twitter...")
        speak("Opening Twitter...")
        open_website("https://twitter.com")

    elif 'open visual studio code' in query:
        outputterminalBox.appendPlainText("Opening Visual Studio Code...")
        speak("Opening Visual Studio Code...")
        code_path = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
        os.startfile(code_path)
        
    elif 'open browser' in query:
        outputterminalBox.appendPlainText("Opening browser...")
        speak("Opening browser...")
        code_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
        os.startfile(code_path)

    elif 'shutdown' in query:
        outputterminalBox.appendPlainText("Shutting down the PC...")
        speak("Shutting down the PC...")
        os.system("shutdown /s /t 0")  

    elif 'restart' in query:
        outputterminalBox.appendPlainText("Restarting the PC...")
        speak("Restarting the PC...")
        os.system("shutdown /r /t 0") 

    elif 'sleep' in query:
        outputterminalBox.appendPlainText("Putting the PC to sleep...")
        speak("Putting the PC to sleep...")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

    elif 'watch a movie' in query or 'watch movie' in query:
        outputterminalBox.appendPlainText('Just give me a second!')
        speak('Just give me a second!')
        webbrowser.open('https://goojara.to')
        outputterminalBox.appendPlainText('here you can watch any movie you want')
        speak('here you can watch any movie you want')

    elif 'open task manager' in query:
        outputterminalBox.appendPlainText("Opening Task Manager...")
        speak("Opening Task Manager...")
        os.system("taskmgr")

    elif 'open control panel' in query:
        outputterminalBox.appendPlainText("Opening Control Panel...")
        speak("Opening Control Panel...")
        os.system("control")

    elif 'open command prompt' in query:
        outputterminalBox.appendPlainText("Opening Command Prompt...")
        speak("Opening Command Prompt...")
        os.system("cmd")

    elif 'open system settings' in query:
        outputterminalBox.appendPlainText("Opening System Settings...")
        speak("Opening System Settings...")
        os.system("ms-settings:")

    elif 'empty recycle bin' in query:
        outputterminalBox.appendPlainText("Emptying the Recycle Bin...")
        speak("Emptying the Recycle Bin...")
        os.system("cmd /c echo Y|PowerShell.exe -NoProfile -Command Clear-RecycleBin")

    elif 'tell me about your school' in query:
        outputterminalBox.appendPlainText('MOKSHADA SCHOOL welcomes all our dear students, parents, and well-wishers in the holy area of Pashupatinath. It is situated at Mokshada Nagar, Kumarigal, Kathmandu. Since 1997, the school has carried the legacy of progressive teaching-learning. Besides, the pedagogical approach has been transformed now and then with the need of time and learning scenarios. Moreover, the qualified teachers, learning culture, tech-friendly platform, and multi-dimensional trends of academics are the enhancing factors of the school. Acknowledging quality education to the learners has centred the major objective of the school. Henceforth, the motto of the school is “Read, Lead and Succeed”. Learners will merely get the feel of learning home here.')
        speak('MOKSHADA SCHOOL welcomes all our dear students, parents, and well-wishers in the holy area of Pashupatinath. It is situated at Mokshada Nagar, Kumarigal, Kathmandu. Since 1997, the school has carried the legacy of progressive teaching-learning. Besides, the pedagogical approach has been transformed now and then with the need of time and learning scenarios. Moreover, the qualified teachers, learning culture, tech-friendly platform, and multi-dimensional trends of academics are the enhancing factors of the school. Acknowledging quality education to the learners has centred the major objective of the school. Henceforth, the motto of the school is “Read, Lead and Succeed”. Learners will merely get the feel of learning home here.')
        speak('Thank you!')

    elif 'tell me a joke' in query:
        joke=pyjokes.get_joke()
        outputterminalBox.appendPlainText(joke)
        speak(joke)

    elif 'open a website' in query:
        outputterminalBox.appendPlainText('Sure! Please say the full URL of the website you want to open.')
        speak('Sure! Please say the full URL of the website you want to open.')
        url_query = takeCommand()
        cleaned_url = clean_up_url(url_query)
        outputterminalBox.appendPlainText(f'opening website {cleaned_url}')
        speak(f'opening website {cleaned_url}')
        webbrowser.open(cleaned_url)

    elif 'search about a topic'  in query or 'search about the topic' in query:
        outputterminalBox.appendPlainText('what do you want to search about?')
        speak('what do you want to search about?')
        topic = takeCommand()
        outputterminalBox.appendPlainText('Searching...')
        speak('Searching...')
        webbrowser.open(topic)

    elif 'open the portfolio of your creator' in query:
        outputterminalBox.appendPlainText('Opening the portfolio of my creator!')
        speak('Opening the portfolio of my creator!')
        webbrowser.open('https://umangthapa.netlify.app')

    elif 'play a song' in query:
        outputterminalBox.appendPlainText("Which song would you like to play?")
        speak("Which song would you like to play?")
        song = takeCommand()
        pywhatkit.playonyt(song)
        speak("Playing " + song + "on youtube")
        outputterminalBox.appendPlainText("Playing " + song + "on youtube")

    elif 'show me something in youtube' in query:
        outputterminalBox.appendPlainText('What do you want to see in YouTube?')
        speak('What do you want to see in YouTube?')
        video_query = takeCommand()
        pywhatkit.playonyt(video_query)
        speak('Playing' + video_query + "in youtube")
        outputterminalBox.appendPlainText('Playing' + video_query + "in youtube")

    elif 'volume up' in query:
        pyautogui.press("volumeup")
        time.sleep(0.50)
        pyautogui.press("volumeup")
        time.sleep(0.50)
        pyautogui.press("volumeup")
        time.sleep(0.50)
        pyautogui.press("volumeup")
        time.sleep(0.50)
        pyautogui.press("volumeup")
        time.sleep(0.50)

    elif 'volume down' in query:
        pyautogui.press("volumedown")
        time.sleep(0.50)
        pyautogui.press("volumedown")
        time.sleep(0.50)
        pyautogui.press("volumedown")
        time.sleep(0.50)
        pyautogui.press("volumedown")
        time.sleep(0.50)
        pyautogui.press("volumedown")
        time.sleep(0.50)

    elif 'volume mute' in query:
        pyautogui.press("volumemute")
        pyautogui.press("volumeunmute")

    else:
        outputterminalBox.appendPlainText("I'm sorry, I didn't understand that command. Can you please repeat?")
        speak("I'm sorry, I didn't understand that command. Can you please repeat?")
        return takeCommand()

def process_command():
    query = takeCommand()
    handle_command(query, ui.terminalOutputBox)

def clean_up_text(texts):
    cleaned_text = texts.replace('*', '.').replace('@', 'at').replace(':','.').replace('.','. ')
    return cleaned_text

def clean_up_url(texts):
    cleaned_url = texts.replace('dot', '.').replace('slash', '/')
    return cleaned_url

class ListenThread(QtCore.QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        wake_up_phrase = ("hey assistant", "wake up assistant")
        while True:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                print("...")
                audio = recognizer.listen(source)
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
                outputterminalBox.appendPlainText(f"Could not request results from Google Speech Recognition service; {e}")

def on_finished():
    sys.exit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)

    ui.movie= QtGui.QMovie("e8c5b61a18d49c20c48f0fe6d4839def4a96d970r1-444-250_00.gif")
    ui.label_8.setMovie(ui.movie)
    ui.movie.start()

    ui.movie2= QtGui.QMovie("R (1).gif")
    ui.label_9.setMovie(ui.movie2)
    ui.movie2.start()

    ui.movie3= QtGui.QMovie("R.gif")
    ui.label.setMovie(ui.movie3)
    ui.movie3.start()

    Dialog.show()

    wishMe()
    Dialog.finished.connect(on_finished)

    listen_thread = ListenThread()
    listen_thread.start()

    sys.exit(app.exec_())