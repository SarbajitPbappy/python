import speech_recognition as sr
import pyttsx3 as txt
import pywhatkit as pw
import datetime as dt
import wikipedia
import pyjokes
import webbrowser
import requests
import json

listener = sr.Recognizer()
Xaamp = txt.init()

# Set female voice
voices = Xaamp.getProperty('voices')
Xaamp.setProperty('voice', voices[1].id)
Xaamp.setProperty('rate', 150)

def talk(text):
    Xaamp.say(text)
    Xaamp.runAndWait()

def get_command_from_microphone():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Xaamp' in command:
                command = command.replace('Xaamp', '')
                print(command)
    except: 
        pass

def get_joke():
    try:
        response = requests.get('https://api.example.com/jokes')
        data = response.json()
        joke = data['joke']
        return joke
    except requests.exceptions.RequestException:
        return "Sorry, I couldn't fetch a joke at the moment."

def get_weather(city):
    try:
        api_key = '7d26c2401c1a64ba68ecd9699700cc4f'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        response = requests.get(url)
        data = response.json()
        if data['cod'] == 200:
            temperature = data['main']['temp']
            temperature = round(temperature - 273.15, 1)
            description = data['weather'][0]['description']
            weather_report = f"The current weather in {city} is {description}. The temperature is {temperature} degrees Celsius."
            return weather_report
        else:
            return "Sorry, I couldn't fetch the weather information."
    except requests.exceptions.RequestException:
        return "Sorry, I couldn't fetch the weather information."

def play_Xaamp():
    current_hour = dt.datetime.now().hour
    if current_hour < 12:
        greeting = "Good morning"
    elif current_hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    talk(greeting + " I'm Xaamp. How can I help you today?")

    command = get_command_from_microphone()
    print(command)

    if 'play' in command:
        talk('Playing')
        song = command.replace('play', '').strip()
        pw.playonyt(song)
    elif 'time' in command:
        current_time = dt.datetime.now().strftime('%I:%M %p')
        talk('The current time is ' + current_time)
    elif 'date' in command:
        current_date = dt.datetime.now().strftime('%d / %m / %Y')
        talk('Today is ' + current_date)
    elif 'are you single' in command:
        talk('No, I am in a relationship with WiFi')
    elif 'joke' in command:
        joke = get_joke()
        talk('Sure, here is a joke for you...')
        talk(joke)
    elif 'name' in command:
        talk('I am Xaamp. How can I help you today?')
    elif 'weather' in command:
        city = command.replace('weather', '').strip()
        weather_report = get_weather(city)
        talk(weather_report)
    elif 'who is' in command:
        person = command.replace('who is', '').strip()
        pw.info(person, 1)
    elif 'what is' in command:
        thing = command.replace('what is', '').strip()
        pw.info(thing, 1)
    elif 'where is' in command:
        place = command.replace('where is', '').strip()
        pw.info(place, 1)
    elif 'how to' in command:
        task = command.replace('how to', '').strip()
        pw.info(task, 1)
    elif 'search' in command:
        query = command.replace('search', '').strip()
        pw.search(query)
    elif 'open' in command:
        app = command.replace('open', '').strip()
        pw.playonyt(app)
    elif 'thank you' in command:
        talk('You are welcome')
    elif 'exit' in command:
        talk('Thank you for using Xaamp. Have a nice day.')
        exit()
    else:
        talk('Sorry, I cannot understand but i can search it for you')
        pw.search(command)

while True:
    play_Xaamp()
