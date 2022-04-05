# pyttsx3- python text to speech
import pyttsx3 as p

# we cannot directly get speech_recognition package....
# so 1st pip install pipwin
# then 2nd pipwin install pyaudio

import speech_recognition as sr

from selenium_web import infow
from yt_vid import music
from news import *
import randfacts
#from jokes import *
from weather import *
from spofy import *
import datetime

engine = p.init()

# to set the rate of voice (slow/fast)
rate=engine.getProperty('rate')# not needed
engine.setProperty('rate', 150)

# set tone of voice(male/Female)
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        return ("Good morning")
    elif hour>=12 and hour<16:
        return("Good afternoon")
    else:
        return("Good Evening")

today_date = datetime.datetime.now()
r=sr.Recognizer()# helps to retrive audio from our microphone

speak("Hello ," + wishme() + " i'm your voice assistant.")
speak("today is " + today_date.strftime("%d") + " of " + today_date.strftime("%B") + ", And its currently " + (today_date.strftime("%I")) + (today_date.strftime("%M")) + (today_date.strftime("%p")))
speak("Temparature in Saangli is " + str(temp()) + "degree celsius , " + "and with " + str(des()))


speak("What can i do for you ?")

# speech recognition through microphone by machine & storing to variable audio
with sr.Microphone() as source:
    r.energy_threshold=10000# to capture low voices
    r.adjust_for_ambient_noise(source,1.2)# to remove background noise
    print("Listening....")
    audio=r.listen(source)
    text2=r.recognize_google(audio)# sending audio which will convert audio into text
    print(text2 )



if "information" in text2:
    speak("which topic?")

    with sr.Microphone() as source:
        r.energy_threshold = 10000  # to capture low voices
        r.adjust_for_ambient_noise(source, 1.2)  # to remove background noise
        print("Listening....")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
        print(infor)

    speak("searching {} in wikipedia".format(infor))
    assist = infow()
    assist.get_info(infor)

elif "play" and "video" in text2:
    speak("you want to play me which video??")
    with sr.Microphone() as source:
        r.energy_threshold = 10000  # to capture low voices
        r.adjust_for_ambient_noise(source, 1.2)  # to remove background noise
        print("Listening....")
        audio = r.listen(source)
        vid = r.recognize_google(audio)
        print(vid)

    speak("playing {} on youtube".format(vid))
    assist = music()
    assist.play(vid)

elif "news" in text2:
    print("Sure..")
    speak("Sure.")
    arr=news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])

elif "fact" in text2:
    speak("Sure.")
    x=randfacts.get_fact()
    print(x)
    speak("Did you know that, "+x)

elif "play" and "music" in text2:
    speak("you want to play me which music??")
    with sr.Microphone() as source:
        r.energy_threshold = 10000  # to capture low voices
        r.adjust_for_ambient_noise(source, 1.2)  # to remove background noise
        print("Listening....")
        audio = r.listen(source)
        sng = r.recognize_google(audio)
        print(sng)

    speak("playing {} on spotify".format(sng))
    assist = song()
    assist.sing(sng)

elif "joke" in text2:
    speak("sure man..")
    ar=joke()
    print(ar[0])
    speak(ar[0])
    print(ar[1])
    speak(ar[1])

else:
    speak("I cannot recognize you. Sorry!")


