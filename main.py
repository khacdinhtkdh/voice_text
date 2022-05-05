import asyncio
import os

import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import weather

friday = pyttsx3.init()
voice = friday.getProperty('voices')
friday.setProperty('voice', voice[1].id)


def speak(audio):
    print('FRIDAY: ' + audio)
    friday.say(audio)
    friday.runAndWait()


def get_time():
    time = datetime.datetime.now().strftime('%I:%M:%p')
    speak(time)


def welcome():
    hour = datetime.datetime.now().hour
    if 6 <= hour <= 12:
        speak('Good morning sir')
    elif 12 < hour <= 18:
        speak('Good afternoon sir')
    else:
        speak('good night sir')
    speak('How can I help you?')


def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold = 1
        audio = c.listen(source)
    try:
        query = c.recognize_google(audio, language='en')
        print('Dinh: ' + query)
    except sr.UnknownValueError:
        print("Please repeat or typing the command")
        query = str(input('Your order is: '))
    return query


if __name__ == '__main__':
    welcome()
    while True:
        query = command().lower()
        if 'google' in query:
            speak('What should I search?')
            search = command().lower()
            url = f"https://www.google.com/search?q={search}"
            webbrowser.get().open(url)
            speak(f'Here is your {search} on google')

        elif 'youtube' in query:
            speak('What should I search?')
            search = command().lower()
            url = f"https://www.youtube.com/search?q={search}"
            webbrowser.get().open(url)
            speak(f'Here is your {search} on youtube')

        elif 'time' in query:
            get_time()

        elif 'quit' in query:
            speak('Bye')
            quit()

        elif 'weather' in query:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(weather.getweather())
