import speech_recognition as sr
import pyaudio
import pyttsx3
import wikipedia
import datetime

listener = sr.Recognizer()
alexa=pyttsx3.init()
voices=alexa.getProperty('voices')
alexa.setProperty('voice',voices[1].id)

def talk(text):
    alexa.say(text)
    alexa.runAndWait()

def take_command():
    try:
        with sr.Microphone(device_index=0) as source:
            print('Listening...')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')
    except:
        pass
    return command
# take_command()
print(take_command())