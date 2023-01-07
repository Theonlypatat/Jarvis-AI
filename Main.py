import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine =  pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 

def wishMe():
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Jarvis here, How may I help You?")   

def takeCommand():
    # It takes Microphone input from the User and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")  
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception  as e:
    # print(e) 
       print("Say that again please...")
       return "None"
    return query

if __name__ == "__main__":
    wishMe()
    # while True:
    if 1:
        query = takeCommand().lower()

        # Login For executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open wikipedia' in query:
            webbrowser.open("Wikipedia.com")
            speak('Opening wikipedia...')
            print('Opening wikipedia...')

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak('Opening youtube...')
            print('Opening youtube...')
            
        elif 'open spotify' in query:
            webbrowser.open("spotify.com")
            speak('Opening spotify...')  
            print('Opening spotify...') 

        elif 'open reddit' in query:
            webbrowser.open("reddit.com")
            speak('Opening reddit...')
            print('Opening reddit...')

        elif 'open discord' in query:
            webbrowser.open("discord.com/app")
            speak('Opening discord...')
            print('Opening discord...')

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak('Opening google...')
            print('Opening google...')

        elif 'open gmail' in query:
            webbrowser.open("mail.google.com")   
            speak('Opening gmail...')   
            print('Opening gmail...')       

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"The time is {strTime}")  

        elif 'open code' in query:
            codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)            
