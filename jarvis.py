import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import time
import pyautogui
import random
from googlesearch import search
import requests




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("hey!")
        speak("  Good Morning Neel")

    elif hour >= 12 and hour < 18:
        speak("hey!")
        speak("  Good Afternoon Neel")

    else:
        speak("hey!")
        speak("  Good Evening Neel")

    speak("I am Jarvis , your personal voice assistant. Please tell me how may i help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query




jokes = ["Why did the tomato turn red?,, Because it saw the salad dressing!",          "Why was the math book sad?,, Because it had too many problems.",          "What do you get when you cross a snowman and a shark? ,,Frostbite!",         "Why did the scarecrow win an award?,, Because he was outstanding in his field.",
         "What did the janitor say when he jumped out of the closet? ,,Supplies!",     "Why did the chicken cross the playground? ,,To get to the other slide.",  "How do you catch a squirrel?,, Climb up a tree and act like a nut!" ,        "What do you call a fake noodle? ,,An impasta.",          "Why don't scientists trust atoms? ,,Because they make up everything.",
         "Why did the cookie go to the doctor? Because he felt crumbly."      ]

def tellJoke():
    joke = random.choice(jokes)
    speak(joke)
    print(joke)




compliments = ["You are amazing!",                "You have a great smile.",                "You are a fantastic listener.",                "You are so talented.",                "You have a wonderful sense of humor.",   "You are a natural leader and inspire others with your actions.",      "Your dedication and hard work are truly impressive.",      "You have a contagious positive attitude that makes others feel good.",         "You have a beautiful mind and unique perspective on the world.",
               "Your creativity and imagination are inspiring.",               "You are a great listener and always make others feel heard and valued.",               "You have a wonderful sense of humor that brings joy to those around you.",         "Your determination and persistence are admirable.",                 "You have a kind heart and always go out of your way to help others.",              "You are an incredible problem solver and have a knack for finding solutions to complex issues."]

def giveCompliment():
    compliment = random.choice(compliments)
    speak(compliment)
    print(compliment)




coin = ["heads" ,       
                   "tails"]

def flipcoin():
    coins = random.choice(coin)
    speak(f"woohooo! its {coins}")
    print(f"woohooo! its {coins}")


def googleSearch(query):
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")

    try:
        speak("Here's what I found on Google")
        for j in search(query, num_results=1):
            webbrowser.open(j)
            return "Success"
    except:
        return "Failed to open web browser"




def getNews():
    apiKey = 'abb29ebc2706432ba103a7ae9fbb7d73' 
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={apiKey}"
    response = requests.get(url)
    news = response.json()
    return news

def showNews():
    speak("Here are the top headlines from India")
    news = getNews()
    articles = news['articles']
    for article in articles:
        speak(article['title'])
        time.sleep(1)










if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results.encode('utf-8'))
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open chat gpt' in query:
            webbrowser.open("https://chat.openai.com/")

        elif 'open netflix' in query:
            webbrowser.open("Netflix.com")

        elif 'open prime video' in query:
            webbrowser.open("primevideo.com")

        elif 'open amazon' in query:
            webbrowser.open("amazon.in")

        elif 'open email' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")



        elif 'open spotify' in query:
            os.system('spotify')
        elif 'play spotify' in query:
            os.system('spotify')
            time.sleep(5)
            pyautogui.hotkey('ctrl', '2')
            time.sleep(3)
            pyautogui.press('space')




        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,  The time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\neels\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        

        elif 'tell me a joke' in query:
            tellJoke()


        elif 'what is my name' in query:
            speak("your name is neel . you are a wonderful human being, and i am your voice assistant jarvis.")

        elif 'dumb' in query:
            speak("seems like i didn't understand you. sorry about that! ")

        elif 'no' in query:
            speak("seems like i didn't understand you. sorry about that!")

        elif 'not' in query:
            speak("seems like i didn't understand you. sorry about that! ")

        elif 'good' in query:
            speak("thank you , happy to help.")

        elif 'nice' in query:
            speak("thank you , happy to help.")

        elif 'awesome' in query:
            speak("thank you , happy to help.")



        elif 'give me a compliment' in query:
            giveCompliment()

        elif 'flip a coin' in query:
            flipcoin()


        elif 'who are you' in query:
            speak("i am jarvis. a voice assistant. I am here to help your and provide assistance in various things.")



        elif 'search for' in query:
            googleSearch(query)
            
        elif 'news' in query:
            getNews()
            showNews()

        else:
            speak("here's what i found on web")
            googleSearch(query)
            
