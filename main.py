import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print("Initializing Jarvis")
MASTER = "Kousik"



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)



#Speak function will pronounce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()


#This function will wish you as per the current timne
def wishMe():
    hour = int(datetime.datetime.now().hour)
   

    if hour>=0 and hour <12:
        speak("Good Morning" + MASTER)

    elif hour>=12 and hour<18:
        speak("Good Afternoon" + MASTER)

    else:
        speak("Good Evening" + MASTER)


    #speak("I am Jarvis. How may I help you?")



#This function will take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")
    
    except Exception as e:
        print("Say that again please")
        query = None
    return query


#This function sends email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('firstproject94@gmail.com','firstproject#27') #sender email & password
    server.sendmail('firstproject94@gmail.com', to, content)
    server.close()


# Main Program starts here
def main():
    speak("Initializing Jarvis....")
    wishMe()
    query = takeCommand()

    # Logic for executing tasks as the per the query
    if 'wikipedia' in query.lower():
        speak('Searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences= 2)
        print(results)
        speak(results)

    elif 'open youtube' in query.lower():
        url1 = "youtube.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url1)

    elif 'open google' in query.lower():
        url1 = "google.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url1)

    elif 'music' in query.lower():
        songs_dir = "F:\Songs\Hindi" 
        songs = os.listdir(songs_dir) #put the directory where songs are
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif 'time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:S")
        speak(f"{MASTER} the time is {strTime}")

    elif 'send email' in query.lower():
        try:
            speak("What should I send")
            content = takeCommand()
            to = "kousikdasbabu2@gmail.com"
            sendEmail(to,content)
            speak("Email has been sent successfuly")
        except Exception as e:
            print(e)
main()