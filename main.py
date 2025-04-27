import speech_recognition as sr
import webbrowser # it help to open browser 
import pyttsx3  #it is for convering text to speech
import musiclibrary
import requests
from openai import OpenAI
import pyjokes

 
recognizer =sr.Recognizer()# it is an class which help to take speech recognizer function
engine = pyttsx3.init()#it iniatialize pyttsx3
newsapi="add your api"

def aiprocess(command):
    client = OpenAI(
        api_key="add your api"
    )

    completion = client.chat.completions.create(
      model="gpt-4o-mini",
      store=True,
      messages=[
        {"role": "system", "content": "You are a virtual assistant name jarvis."},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content


def speak(text):
    engine.say(text)
    engine.runAndWait()
def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        parts = c.lower().split(" ")
        if len(parts) > 1:
            song = parts[1]
            link = musiclibrary.music.get(song)  # Use .get() to avoid KeyError if song does not exist
            if link:  # Check if the link exists in your music library
                webbrowser.open(link)
            else:
                print(f"Song '{song}' not found in library.")
        else:
            print("Please specify a song to play.")
 
    elif "news" in c.lower(): 
        r=requests.get("add your api")
        if r.status_code ==200:
            #parse the JSON response
            data =r.json()

            #Extract the articles
            articles = data.fet("articles",[])

            #print the headlines
            for articles in articles:
                speak(articles["title"])
    #this will search any think from google             
    elif "search" in c.lower():
        speak("what do you want to search")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening your request...")
            audio = r.listen(source)

        try:
            query = r.recognize_google(audio)
            print(f"You said: {query}")
            search_url = f"https://www.google.com/search?q={query}"
            webbrowser.open(search_url)
            print("Searching on Google...")
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")  
    #for jokes
    elif "Tell me a joke" in c.lower():
        joke = pyjokes.get_joke()
        speak(joke)        

    else:
        #let openai handle the request
        output =aiprocess(c)
        speak(output)
        pass    


if __name__ == "__main__":
    speak("Initializing jarvis......")
    while True:
    #lsiten for the wake word jarvis
    #obtain audio from microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source,timeout=0,phrase_time_limit=0)
        print("recognizing.......")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source)
            word = r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("ya")
                #listen for text
                with sr.Microphone() as source:
                    print("jarvis active....")
                    audio = r.listen(source)
                    command=r.recognize_google(audio)
                    processcommand(command)
        #return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        #return "Error: Could not understand audio"
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        #return "Error: Could not request results"


