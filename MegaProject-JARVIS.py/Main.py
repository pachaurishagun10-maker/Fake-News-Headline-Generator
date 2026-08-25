import speech_recognition as sr
import webbrowser
import pyttsx3
import MusicLibrary
import requests
import os
from dotenv import load_dotenv
from groq import Groq 

recognizer=sr.Recognizer()
engine=pyttsx3.init()
NEWS_API_KEY="39d0c5dcc136403b8c20772e1287b4fe"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    c= c.lower()
    if "open google" in c:
        speak("Opening Google...")
        webbrowser.open("https://www.Google.com")
            
    elif "open youtube" in c:
        speak("Opening Youtube...")
        webbrowser.open("https://www.Youtube.com")
            
    elif "open github" in c:
        speak("Opening Github...")
        webbrowser.open("https://www.Github.com")
            
    elif "open chatgpt" in c:
        speak("Opening Chatgpt ...")
        webbrowser.open("https://www.chat.openai.com") 

    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=MusicLibrary.Music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}")
        if r.status_code == 200:
            data=r.json()                         #Parse the JSON response

            articles=data.get('articles',[])      #Extract the articles

            for article in articles:
                speak(article['title'])          
    


if __name__ == "__main__":
    speak("Activating Jarvis")

    r = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as source:
                print("Recognizing...")
                r.adjust_for_ambient_noise(source, duration=0.8)
                audio = r.listen(source, timeout=7,phrase_time_limit=3)

            print("Processing...")
            word = r.recognize_google(audio)
            print(f"Heard: {word}")

            if "jarvis" in word.lower():
                remaining = word.lower().replace("jarvis", "").strip()

                if remaining:
                    print(f"Command: {remaining}")
                    processCommand(remaining)

                else:
                    speak("Yes")

                    # Listen for command
                    try:
                        with sr.Microphone() as source:
                            print("Listening...")
                            r.adjust_for_ambient_noise(source,duration=0.5)
                            audio = r.listen(source,timeout=7,phrase_time_limit=5)

                        command = r.recognize_google(audio)
                        print(f"Command: {command}")
                        processCommand(command)

                    except sr.WaitTimeoutError:
                        print("Timeout - Can't hear")

                    except sr.UnknownValueError:
                        print("Didn't get what you said")

                    except Exception as e:
                        print(f"Error: {e}")

        except sr.WaitTimeoutError:
            print("Timeout - Can't hear")

        except sr.UnknownValueError:
            print("Didn't get what you said")

        except Exception as e:
            print(f"Error: {e}")