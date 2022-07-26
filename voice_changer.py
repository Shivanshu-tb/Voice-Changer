from regex import E
import speech_recognition as sr
from win32com.client import Dispatch
import pyttsx3
class VoiceChanger:
    def man_speech():
        r = sr.Recognizer()
            
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration = 1)
            audio = r.listen(source)
        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            speak = Dispatch('SAPI.SpVoice')
            speak.Speak(query)

        except Exception as e:
            print(e)
            print('Sorry I didn\'t get that')
    def female_speech():
        r = sr.Recognizer()
            
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration = 1)
            audio = r.listen(source)
        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language='en-in')
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            engine.say(query)
            engine.runAndWait()
        except Exception as e:
            print(e)
            print('Sorry I didn\'t get that')

if __name__=='__main__':
    user = input('1. Male \n2. Female\n')
    if user=='1':
        VoiceChanger.man_speech()
    elif user=='2':
        VoiceChanger.female_speech()
    else:
        print('Enter a valid input!')
