from googletrans import Translator
import pyttsx3

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def speak(translated_text):
    engine.say(translated_text)
    engine.runAndWait()

def translate_to_nepali(text):
    translator = Translator()
    translation = translator.translate(text, dest='ne')
    return translation.text

if __name__ == "__main__":
    print("Welcome to English to Nepali Translator!")
    print("Enter 'quit' to exit.")

    while True:
        text = input("Enter text to translate: ")
        
        if text.lower() == 'quit':
            print("Exiting...")
            break
        
        translated_text = translate_to_nepali(text)
        print("Translated text:", translated_text)
        speak("text" + translated_text)