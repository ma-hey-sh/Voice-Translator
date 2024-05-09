import speech_recognition as sr
from google_trans_new import google_translator
import pyttsx3
from deep_translator import GoogleTranslator

recognizer = sr.Recognizer()
engine=pyttsx3.init()

# Speech recognizer
with sr.Microphone() as source:
    print('Clearing the backgroung noises')
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print('Waiting for your message')
    audio=recognizer.listen(source, timeout=3)
    print('Done recording')
try:
    print('Recognizing')
    result=recognizer.recognize_google(audio, language='en')
except Exception as ex:
    print("Couldn't detect, try again.", ex)

#Translate function
def trans():
    langinput=input('Type the language code you want to translate: ')
    # translator=GoogleTranslator()
    translated = GoogleTranslator(source='en', target=langinput).translate(text=result)
    print(translated)
    engine.say(str(translated))
    engine.runAndWait()
trans()


