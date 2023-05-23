import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import requests
import json
import subprocess
import platform

listener = sr.Recognizer()
alexa = pyttsx3.init()

# Set female voice
voices =alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)
alexa.setProperty('rate', 150)

def talk(text):
    alexa.say(text)
    alexa.runAndWait()

def get_command_from_microphone():
    try:
        with sr.Microphone(device_index=0) as source:
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
# def open_website(website_url):
#     system = platform.system()
#     try:
#         if system == 'Windows':
#             subprocess.Popen(['start', '', website_url], shell=True)
#         elif system == 'Darwin':  # macOS
#             subprocess.Popen(['open', website_url])
#         else:  # Linux
#             subprocess.Popen(['xdg-open', website_url])
#         talk(f"Opening website: {website_url}")
#     except OSError:
#         talk(f"Sorry, I couldn't open the website.")


current_hour = datetime.datetime.now().hour
if current_hour < 12:
    greeting = "Good morning"
elif current_hour < 18:
        greeting = "Good afternoon"
else:
    greeting = "Good evening"
talk(greeting + " I'm alexa. How can I help you today?")

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
        talk(pyjokes.get_joke())
    elif 'name' in command:
        talk('I am alexa. How can I help you today?')
    elif 'weather' in command:
        city = command.replace('weather', '').strip()
        weather_report = get_weather(city)
        talk(weather_report)
    elif 'who is' in command:
        person = command.replace('who is', '').strip()
        info=wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'what is' in command:
        thing = command.replace('what is', '').strip()
        pywhatkit.info(thing, 1)
    elif 'where is' in command:
        place = command.replace('where is', '').strip()
        pywhatkit.info(place, 1)
    elif 'how to' in command:
        task = command.replace('how to', '').strip()
        pywhatkit.info(task, 1)
    elif 'search' in command:
        query = command.replace('search', '').strip()
        pywhatkit.search(query)
    # elif 'open' in command:
    #     website = command.replace('open website', '').strip()
    #     open_website(website)
    elif 'thank you' in command:
        talk('You are welcome')
    elif 'exit' in command:
        talk('Thank you for using alexa. Have a nice day.')
        exit()
    else:
        talk('Sorry, I cannot understand but i can search it for you')
        pywhatkit.search(command)

while True:
    play_alexa()
