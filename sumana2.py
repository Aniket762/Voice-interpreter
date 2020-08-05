import pyttsx3  # pip install
import datetime
import speech_recognition as sr # pip  install
import wikipedia  # pip install
import webbrowser
import os
import smtplib

# if using python>3.8 then pyaudio won't work use this
# pip install pipwin
# pipwin install pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    #speak("This is in very basic stage I will work on this ignore the errors this has minimum functionality and lot of errors I will work on this")
    speak("Hi Babe! I am Sumana I love you a lot. How may I help you? ")



# microphone input from user and returns string output
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising... ")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please..")
        print("None")
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your@email.com', 'your password')
    server.sendmail('youremail', to, content)
    server.close()


if __name__ == "__main__":
    # speak("Aniket is a good boy")
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')


        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
            music_dir ="C:\\Users\\NITD\\Downloads\\songs"  # directory ka address
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))  # random bana na hai

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is:{strTime}")

        elif ' quit ' in query:
            exit()

        elif 'open Pycharm' in query:
            Path = "D:\\Assignment\\assignment\\PyCharm Community Edition 2019.3\\bin"
            os.startfile(Path)

        elif 'email to sumana' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = 'sumana.basu2001@gmail.com'
                sendEmail(to, content)
                speak("Email has been sent")

            except Exception as e:
                print(e)
                speak("sorry can't be send")


