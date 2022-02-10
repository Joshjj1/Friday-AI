
import datetime
#import imp 
import speech_recognition as sr               #pip install speech_recognition
#from json.tool import main
import pyttsx3                                #pip install pyttsx3
import wikipedia                              #pip install wikipedia
import webbrowser 
import os

engine= pyttsx3.init('sapi5')                    #setting voices
voices=engine.getProperty('voices')
#print(voices[1].id) 
engine.setProperty('voice',voices[1].id)          # voices[0].id = male voice, voices[1].id=female voice

def speak(audio):                             # defining function for speak 
    engine.say(audio)                          # for   
    engine.runAndWait()

def wishMe():                                   # function to wish the user
    hour=int(datetime.datetime.now().hour) 
    if hour>=0 and hour< 12:                     #conditions for time of the day
        speak(" Good Morning , boss !")
    elif hour>=12 and hour<18 : 
        speak(" Good Afternoon , boss !")
    else:
        speak(" Good evening , boss !") 
    
    speak(" I am Friday, your personalized AI. How may i help you ?")


def takeCommand():                                  # function takes input from user as speech from mic and return string
    r= sr.Recognizer()                    
    with sr.Microphone() as source : 
        r.adjust_for_ambient_noise(source,duration=2)
        print("Listening...")  
        speak("Listening")
        r.pause_threshold=1
        audio=r.listen(source)
    
    try:                                                                       #using try except , error may occur if Ai isnt able to recognize
        print("Recognizing...")
        speak("Recognizing...")                                                #user is talking 
        query=r.recognize_google(audio)                                         # coverting input to string through google
        print(f"user said : {query}\n")
   
    except Exception as e:                                                     #if error occurs
        #print(e)
        speak("Sorry, could you say that again please ?")                      #Repeat the input
        return "None"
    return query                                                               #if understood by AI , returning the input as string


if __name__=="__main__": 
    speak(" Welcome back , JOSH ")
    speak(" All Systems online")
    speak("updating")
     
    wishMe()  
    while True:
        query=takeCommand().lower()             
        
         #logic for executing tasks based on query 
        if 'wikipedia' in query :                                                  # wikipedia
            speak("Searching wikipedia...") 
            query=query.replace("wikipedia","") 
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'youtube' in query :                                                 #youtubee
            speak("Opening youtube...") 
            webbrowser.open("youtube.com")

        elif 'google' in query :                                                   #google
            speak("Opening google...") 
            webbrowser.open("google.com")
 
        elif 'play music' in query:                                                      #playing music from file
            speak("Playing No time by KSI(feat. Lil Durk)") 
            music_dir="C:\\Users\\joshj\\Desktop\\python 2\\No Time (feat. Lil Durk).mp3" 
           # songs=os.listdir(music_dir)
           # print(songs)
            os.startfile(music_dir)

        elif 'time' in query :                                                                   #time
            strTime=datetime.datetime.now().strftime("%H : %M : %S")
            speak(f"Boss,the time is {strTime} ") 

        elif 'date' in query :                                                                   #date
            strTime=datetime.datetime.now().strftime("%D : %M : %Y")
            speak(f"Boss,the date is {strTime} ") 

        elif 'stremio' in query:                                                                      #opening streamio
            speak("Opening streamio...") 
            streamioPath="C:\\Users\\joshj\\AppData\\Local\\Programs\\LNV\\Stremio-4\\stremio.exe"
            os.startfile(streamioPath)
        
        elif 'ms teams' in query: 
           try:
               teamsPath="C:\\Users\\joshj\\AppData\\Local\\Microsoft\\Teams\\Update.exe --processStart 'Teams.exe' "
               os.startfile(teamsPath) 

           except Exception as e: 
                speak("Some error has occured")

        elif 'gmail' in query :                                                                                 #opening gmail
            speak("Opening gmail...") 
            webbrowser.open("mail.google.com") 

        elif 'quit' in query:  
            speak("Goodbye boss , Have a great day !") 
            quit() 

