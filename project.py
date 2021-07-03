import speech_recognition as sr
import pyttsx3
import requests
import subprocess
import os
import wikipedia


def saveFile(Fname, cmd):
    completeName = os.environ["HOMEPATH"] + "\\Desktop\\" + Fname + ".txt"
    f = open(completeName, "a+")
    f.write(cmd + '\r\n')
    f.close()
    print('saved')
    SpeakText('saved')


def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


def speechToText():
    # Initialize the recognizer
    r = sr.Recognizer()

    MyText = ''
    # Exception handling to handle
    # exceptions at the runtime
    while MyText == '' or MyText is None:

        try:

            # use the microphone as source for input.
            with sr.Microphone() as source2:
                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                r.adjust_for_ambient_noise(source2, duration=5)

                # listens for the user's input
                audio2 = r.listen(source2)

                # Using google to recognize audio
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()

                if MyText != '' or MyText is not None:
                    print(MyText)
                    SpeakText(MyText)
                    return MyText



        except sr.RequestError:
            print("Sorry, the service is down")
            SpeakText("Sorry, the service is down")
        except sr.UnknownValueError:
            print('sorry i didnt understand do you wanna add this command?(y/n)')
            SpeakText('sorry i didnt understand do you wanna add this command?(y/n)')
            inp = input()
            if inp == 'y':
                saveFile('command', MyText)
            else:
                print('say your command again')
                SpeakText('say your command again')


def greeting(txt):
    if 'hello' in txt:
        print('hi')
        SpeakText('hi')
    if 'how are you' in txt:
        print('im fine thank you.')
        SpeakText('im fine thank you.')


def weather(city):
    # base URL
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    # City Name
    CITY = city
    # API key
    API_KEY = 'aadda1b351cf4a2c78ad672630606ef8'
    # upadting the URL
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    # HTTP request
    response = requests.get(URL)
    # checking the status code of the request
    if response.status_code == 200:
        # getting data in the json format
        data = response.json()
        # getting the main dict block
        main = data['main']
        # getting temperature
        temperature = main['temp']
        # getting the humidity
        humidity = main['humidity']
        # getting the pressure
        pressure = main['pressure']
        # weather report
        report = data['weather']
        print(f"{CITY:-^30}")
        print(f"Temperature: {temperature} K")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hpa")
        print(f"Weather Report: {report[0]['description']}")
    else:
        # showing the error message
        print("Error in the HTTP request")
        print(response.status_code)

    print('press any button to continue')
    SpeakText('press any button to continue')
    input()


def openProgram(cmd):
    if 'firefox' in cmd:
        subprocess.Popen('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
    else:
        subprocess.Popen('C:\\Program Files\\JetBrains\\PyCharm 2018.3.5\\bin\\pycharm64.exe')

    print('press any button to continue')
    SpeakText('press any button to continue')
    input()


def playMusic():
    os.startfile(os.path.join('01. Love Poem.mp3'))
    print('press any button to continue')
    SpeakText('press any button to continue')
    input()


def wiki(txt):
    while True:
        try:
            url = wikipedia.page(wikipedia.suggest(txt)).url
            research = wikipedia.page(wikipedia.suggest(txt)).content
            print(url)
            print(research)
            print('press any button to continue')
            SpeakText('press any button to continue')
            input()
            break
        except Exception as e:
            print('your search have many results please search better :)')
            print('some options you can use:')
            SpeakText('your search have many results please search better :)')
            SpeakText('some options you can use:')
            print(str(e))
            print('do you wanna search again?(y/n)')
            SpeakText('do you wanna search again?(y/n)')
            inp = input()
            if inp == 'y':
                print('what you wanna search about?')
                SpeakText('what you wanna search about?')
                txt = speechToText()
            else:
                break


# starting the program

print('hello my name is genie! i can help you out. you can say me these commands:')
SpeakText('hello my name is genie! i can help you out. you can say me these commands:')

while True:

    print('1. hello/how are you?\n2. weather\n3. open IDE/firefox\n4. play music\n'
          '5. take note\n6. search on wikipedia\n7. goodbye')
    SpeakText('1. hello or how are you?')
    SpeakText('2. weather')
    SpeakText('3. open IDE or firefox')
    SpeakText('4. play music')
    SpeakText('5. take note')
    SpeakText('6. search on wikipedia')
    SpeakText('7. goodbye')
    print('\nwhat is your command?')
    SpeakText('what is your command?')
    cmd = speechToText()

    # exiting
    if 'goodbye' in cmd:
        print('bye bye!')
        SpeakText('bye bye!')
        break

    # greeting
    elif 'hello' in cmd or 'how are you' in cmd:
        greeting(cmd)

    # weather
    elif 'weather' in cmd:
        print('say your city:')
        SpeakText('say your city:')
        city = speechToText()
        weather(city)

    # opening a program
    elif 'open' in cmd:
        openProgram(cmd)

    # playing a music
    elif 'play' in cmd:
        playMusic()

    # adding note
    elif 'note' in cmd:
        print('say your note:')
        SpeakText('say your note:')
        text = speechToText()
        saveFile('note', text)

    # searching in wiki
    elif 'wikipedia' in cmd:
        print('what you wanna search about?')
        SpeakText('what you wanna search about?')
        search = speechToText()
        wiki(search)

    else:
        print('sorry i didnt understand do you wanna add this command?(y/n)')
        SpeakText('sorry i didnt understand do you wanna add this command?(y/n)')
        inp = input()
        if inp == 'y':
            saveFile('command', cmd)
