import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
#import smtplib
import time
import glob
import pyjokes
#import selenium as s

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.setProperty('rate',175)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")  
    else:
        speak("Good Evening!")  
    speak("I am Jarvis Sir. Please tell me how may I help you") 
    
def takeCommand():
   
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
           
        print("Say that again please...")  
        return "None"
    return query
if __name__ == "__main__":
    wishMe()
    while True:
   
        query = takeCommand().lower()

       
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print({strTime})
        elif 'the news'in query:
            webbrowser.open("https://www.thenews.com.pk/")
        elif 'the weather' in query:
            webbrowser.open("https://weather.com/en-IN/weather/today/l/12.92,80.25?par=google")
        elif 'Calculator' in query:
            webbrowser.open("https://www.tcsion.com/OnlineAssessment/ScientificCalculator/Calculator.html")
        elif 'play music' in query:
            music_dir = 'D:\\ai pr'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'open downloads' in query:
            downloads=r"C:\Users\lokel\Downloads"
            os.startfile(os.path.join(downloads))
        elif 'open history' in query:
            webbrowser.open("chrome://history/")
        elif 'jokes' in query:
            a=pyjokes.get_joke('en','all')
            speak(a)
            print(a)
            
        elif 'translator' in query:
            webbrowser.open("https://translate.google.co.in/")

        elif 'recent files' in query:
            list_of_files = glob.glob('C:\\Users\\user\\Recent')
            latest_file = max(list_of_files, key=os.path.getctime)
            os.startfile(os.path.join(latest_file))
            
        elif 'google' in query:
            webbrowser.open("https://www.google.co.in/")
            
        elif 'exit' in query:
            speak('Thank you , please call me when you need')
            break
