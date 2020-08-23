import pyttsx3  # text-to-speech conversion module in Python
import datetime #return date time related info
import speech_recognition as sr  # pip install speechRecognition
import wikipedia #search data from wikipedia
import webbrowser # for open browser 
import os
import random
import smtplib #for sending mail

engine = pyttsx3.init('sapi5')  # initialize Text-to-speech engine
# print(engine)

"""VOICE"""
voices = engine.getProperty('voices')  # get details of all voices available

# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
# engine.setProperty('voice', voices[1].id)  #changing index, changes voices. 1 for female


def speak(audio):
    engine.say(audio)
    engine.runAndWait()  # it processes the voice commands.


def wishMe():
    hour = int(datetime.datetime.now().hour)
    # print(hour)
    if hour > 0 and hour < 12:
        speak("Good Morning Sir!")
        print("Good Morning sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir!")
        print("Good Afternoon sir!")
    else:
        speak("Good Evening sir!")
        print("Good Evening sir!")

    speak("I am cortana sir, plz tell me How can I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    # speak("hello sir how can i help you")
    wishMe()

    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            try:
                speak("searching wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)

            except Exception as e:
                print(e)

        elif 'stop cortana' in query:
            speak("cortana is shutting down")
            exit()

        elif "who is your father cortana" in query:
            speak("Mr Prasad Is my father")

        elif "open facebook" in query:
            webbrowser.open("facebook.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open w3school" in query:
            webbrowser.open("w3schools.com")

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open whatsapp" in query:
            webbrowser.open("web.whatsapp.com")

        elif "play music" in query:
            music_dir = "F:\\Songs 2018"
            songs = os.listdir(music_dir)
            # print(songs)
            print("please wait...")
            os.startfile(os.path.join(music_dir, songs[random.randint(0, 27)]))

        elif "the time" in query:
            currentTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The Time is = {currentTime}")
            print(f"The Time is = {currentTime}")

        elif "open code" in query:
            codepath="C:\\Users\\Prasad\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif "open my pc" in query:
            pcpath="Y:\\"
            os.startfile(pcpath)
            
        elif "play uri movie" in query:
            uripath="F:\\Movies\\Bollywood\\URI.mkv"
            os.startfile(uripath)
        
       
