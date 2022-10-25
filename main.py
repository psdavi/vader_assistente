import speech_recognition as sr
import pyttsx3
import datetime


r = sr.Recognizer()

with sr.Microphone() as source:
    while True:
        audio = r.listen(source)
        text = r.recognize_google(audio)
        if str(text).lower() == "Que horas são?":
            print(datetime.datetime.now().strftime("%H:%M:%S"))
            break





