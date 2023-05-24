import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
alexa = pyttsx3.init()

# Set female voice
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)
alexa.setProperty('rate', 150)


def talk(text):
    print(text)
    alexa.say(text)
    alexa.runAndWait()


def get_command_from_microphone():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
    except:
        pass
    return command


def get_joke():
    return pyjokes.get_joke()


def play_alexa():
    command = get_command_from_microphone()

    if 'play' in command:
        talk('Playing')
        song = command.replace('play', '')
        pywhatkit.playonyt(song)
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The current time is ' + current_time)
    elif 'date' in command:
        current_date = datetime.datetime.now().strftime('%d / %m / %Y')
        talk('Today is ' + current_date)
    elif 'are you single' in command:
        talk('No, I am in a relationship with WiFi')
    elif 'joke' in command:
        talk(get_joke())
    elif 'name' in command:
        talk('I am alexa. How can I help you today?')
    elif 'who is' in command:
        person = command.replace('who is', '').strip()
        info = wikipedia.summary(person, 1)
        talk(info)
    elif 'what is' in command:
        thing = command.replace('what is', '').strip()
        info = wikipedia.summary(thing, 1)
        print(info)
        talk(info)
    elif 'search' in command:
        query = command.replace('search', '').strip()
        pywhatkit.search(query)
    elif 'exit' in command:
        talk('Thank you for using Alexa. Have a nice day.')
        exit()
    else:
        talk("Sorry, I cannot understand but I can search it for you.")
        pywhatkit.search(command)


current_hour = datetime.datetime.now().hour
if current_hour < 12:
    greeting = "Good morning"
elif current_hour < 18:
    greeting = "Good afternoon"
else:
    greeting = "Good evening"
talk(greeting + " I'm Alexa. How can I help you today?")

while True:
    play_alexa()
