import speech_recognition as sr
import pyttsx3, datetime, wikipedia, webbrowser, os

task_lst = ["dummy task - 1", "dummy task - 2", "dummy task - 3", "more dummy tasks"]
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 1000
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')

    except Exception as e:
        print("Say that again please...")
        query = "can you please say that again"
        return query
    return query

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning Mr. Gohel, You may have so many tasks to complete today, would you like to take a look?")
        ans = takeCommand().lower()
        if "yes" in ans:
            for items in task_lst:
                print(f'{task_lst.index(items)+1}: {items}')

    elif hour>=12 and hour<18:
        speak("Good Afternoon Mr. Gohel, How may I help you?")

    else:
        speak("Good Evening Mr. Gohel, How may I help you?")



wishMe()

while True:
    cmd = takeCommand().lower()
    if "open google" in cmd:
        webbrowser.open("www.google.com")

    elif "open youtube" in cmd:
        webbrowser.open("www.youtube.com")

    elif "open facebook" in cmd:
        webbrowser.open("www.facebook.com")

    elif "wikipedia" in cmd:
        speak("Searching Wikipedia...")
        cmd = cmd.replace("wikipedia", "")
        results = wikipedia.summary(cmd, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif "task" in cmd:
        for item in task_lst:
            print(f'{task_lst.index(item)+1}: {item}')
    elif "tasks" in cmd:
        for item in task_lst:
            print(f'{task_lst.index(item)+1}: {item}')
    elif "to do list" in cmd:
        for item in task_lst:
            print(f'{task_lst.index(item) + 1}: {item}')
    elif "reminders" in cmd:
        for item in task_lst:
            print(f'{task_lst.index(item) + 1}: {item}')
    elif "reminder" in cmd:
        for item in task_lst:
            print(f'{task_lst.index(item) + 1}: {item}')
    elif "play music" in cmd:
        music_dir = 'C:\\Users\\Vishal Gohel\\Music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))
    if ("add" in cmd) and ("task" in cmd):
        speak("What task do you want to add?")
        tsk = takeCommand().lower()
        task_lst.append(tsk)
        speak("Task added successfully")

