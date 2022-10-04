from email.mime import audio
from socket import if_nametoindex
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import smtplib 
import os
import nltk
from nltk.chat.util import Chat, reflections


engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
# print( voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning!")
    elif hour >=12 and hour < 18:
        speak("Good Atrenoon!")
    else:
        speak("Good Evening!")

    speak("I am lela sir.")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('husban2006@gmail.com', 'husban s 123')
    server.sendmail('husbanshakeel2006@gmail.com', to, content)
    server.close()



def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query    



if __name__ == "__main__":
    wishMe()

while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)


        elif 'open youtube' in query:
            #   webbrowser.Chrome("https://www.youtube.com/")    
            #   webbrowser.UnixBrowser.name("google.com")
              webbrowser.open("youtube.com")  
        
        elif 'open chrome' in query:
            webbrowser.Chrome.open("chrome.com")    
        
        elif 'open google' in query:
            webbrowser.Chrome.open("google.com")       
        
        # elif 'tell me the  time' in query:
        #     strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        #     speak(f"Sir, the time is {strTime}")    


        elif 'open code' in query:
            codePath = "D:\install\vs code\Microsoft VS Code\Code.exe"
            os.startfile(codePath)    
         
        elif 'email to shakil' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "husban2006@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend husban . I am not able to send this email")     



        elif 'hello' in query:
            speak("hi")
        
        elif 'how are you' in query:
            speak("i m fine what about u? ")

        elif 'i am fine' in query:
            speak("how may i help you?")