import speech_recognition as sr
import time
import os
from time import ctime
from gtts import gTTS
import requests, json

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as scource:
        print("listening sir..")
        audio = r.listen(scource)
    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said:" +data)
    except sr.UnknownValueError:
        print("Google speech recognition didnot understand the speech")
    except sr.RequestError:
        print("RequestError")
    return data
def respond(audioString):
    print(audioString)
    tts = gTTS(text = audioString, lang ='en')
    tts.save("speech.mp3")
    os.system("mpg321 speech.mp3")
def my_attendant(data):
    if "Hello how are you" in data:
        listening = True
        respond("I am good")
    if "what time is it" in data:
        listening = True
        respond(ctime())
    if "stop listening" in data:
        listening = False
        print("shutting down")
        return listening
    return listening
time.sleep(2)
respond("Hi Akshat, i am an assistant.")
listen()
listening = True
while listening == True:
    data = listen()
    listening = my_attendant(data)
