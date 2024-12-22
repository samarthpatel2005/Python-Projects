# Pleace remove all comments before use

import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
# from openai import OpenAI
from gtts import gTTS
import pygame
import os


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "https://newsapi.org/v2/everything?q=apple&from=2024-12-11&to=2024-12-11&sortBy=popularity&apiKey=f5325d538bf24083a54f9e414114792a"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    pygame.mixer.init()

    pygame.mixer.music.load('temp.mp3')

    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 

def aiProcess(command):
    # client = OpenAI(api_key="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",
    # )

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
          
            data = r.json()
            
            
            articles = data.get('articles', [])
            
            
            for article in articles:
                speak(article['title'])

    else:
        
        output = aiProcess(c)
        speak(output) 





if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
       
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "alexa"):
                speak("Ya")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))
