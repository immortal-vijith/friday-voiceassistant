from tkinter import *
import bs4
from cv2 import cv2
import PIL.Image, PIL.ImageTk
import emoji
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
from os import *
from pyautogui import *
import random
import smtplib
import psutil
import roman
import keyboard
from PIL import Image
from time import sleep
import pyautogui
from pywikihow import search_wikihow
from bs4 import BeautifulSoup
import sys
import time
from PyDictionary import PyDictionary as dict
import wolframalpha
import pywhatkit
import requests
from keyboard import *
from keyboard import press_and_release
from idlist import my_gmail, password, destination
p=password
g=my_gmail
d=destination

assistant = pyttsx3.init('sapi5')
client = wolframalpha.Client('V2H2Q6-82GHRHRQQW')
voices = assistant.getProperty('voices')
assistant.setProperty('voice', voices[2].id)
assistant.setProperty('rate',250)
window = Tk()

global var
global var1

var = StringVar()
var1 = StringVar()
def speak(Audio):
    print("   ")
    print(f": {Audio}")
    assistant.say(Audio)
    assistant.runAndWait()
def wishme():
    time= datetime.datetime.now().strftime('%H:%M:%S %p')
    search ="temperature"
    url = f"http://www.google.com/search?q={search}"
    r= requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temp=data.find("div", class_="BNeawe").text
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        var.set("Good Morning !")
        window.update()
        speak("Good Morning !")
        var.set('The time is'+ ' ' + time)
        window.update()
        speak('The time is '+ ' '+time)
        var.set(f"sir the current {search} in your locality is {temp}")
        window.update()
        speak(f"And  the current {search} in your locality is {temp}")
    elif hour>18 and hour<0:
        var.set("Good Evening !")
        window.update()
        speak("Good Evening !")
        var.set('The time is '+ ' ' + time)
        window.update()
        speak('The time is '+ ' ' + time)
        var.set(f"And the current {search} in your locality is {temp}")
        window.update()
        speak(f"And the current {search} in your locality is {temp}")
    elif hour<18 and hour>12:
        var.set("Good Afternoon!")
        window.update()
        speak("Good Afternoon!")
        var.set('The time is '+' ' + time)
        window.update()
        speak('The time is  '+' ' + time)
        var.set(f"And the current {search} in your locality is {temp}")
        window.update()
        speak(f"And the current {search} in your locality is {temp}")
    var.set("Myself FRIDAY your personal A.I Assistant how may I help you?")
    window.update()
    speak("Myself FRIDAY your personal A.I Assistant how may I help you?")
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        window.update()
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source,0,5)

    try:
        var.set("Recognizing...")
        window.update()
        print("Recognizing...")

        query = r.recognize_google(audio, language='en-in')
        print(f"Your Command :  {query}\n")
    except sr.RequestError:
        var.set("Network error")
        window.update()
        speak('Sorry the server is down')

    except Exception:
        # print(e)
        var.set("Press speak to execute commands")
        print("Say that again please...")
        return "None"
    var1.set(query)
    window.update()
    return query

def Dict():
    speak("activated dictionary")
    speak("Tell me the problem!")
    prob1 = takecommand()
    if 'meaning' in prob1:
        prob1 = prob1.replace("what is", "")
        prob1 = prob1.replace("the","")
        prob1 = prob1.replace("of", "")
        prob1 = prob1.replace("meaning", "")
        prob1 = prob1.replace("friday", "")
        result = dict.meaning(prob1)
        speak(f"the meaning for {prob1} is {result}")
    elif 'synonym' in prob1:
        prob1 = prob1.replace("what is", "")
        prob1 = prob1.replace("of", "")
        prob1 = prob1.replace("the", "")
        prob1 = prob1.replace("synonym", "")
        prob1 = prob1.replace("friday", "")
        result = dict.synonym(prob1)
        speak(f"the synonym for {prob1} is {result}")
    elif 'antonym' in prob1:
        prob1 = prob1.replace("what is", "")
        prob1 = prob1.replace("of", "")
        prob1 = prob1.replace("the", "")
        prob1 = prob1.replace("antonym", "")
        prob1 = prob1.replace("for","")
        prob1 = prob1.replace("friday", "")
        result = dict.antonym(prob1)
        speak(f"the antonym for {prob1} is {result}")
    speak("Exited Dictionary!")

def sendemail(to, content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login(g.p)
    server.sendmail(g,to,content)
    server.close()
def TaskExecution():
     btn0['state'] = 'normal'
     btn2['state'] = 'normal'
     btn3['state'] = 'normal'
     btn4['state'] = 'normal'
     btn5['state'] = 'normal'
     btn6['state'] = 'normal'

     btn0.configure(bg='orange')
     btn1.configure(bg='orange')
     btn2.configure(bg='orange')
     btn3.configure(bg='orange')
     btn4.configure(bg='orange')
     btn5.configure(bg='orange')
     btn6.configure(bg='orange')

     query = takecommand().lower()

     if 'exit' in query or 'bye' in query or 'goodbye' in query:
         var.set("Bye \U0001F44B Have a nice day")
         btn1.configure(bg='#5C85FB')
         btn2['state'] = 'normal'
         btn0['state'] = 'normal'
         window.update()
         speak("Bye , Have a nice day.")
         sys.exit()

#google
     elif 'search on google about' in query:
         var.set("This is what I found on google \U0001F50E")
         window.update()
         speak('This is what I found on google')
         query = query.replace("search on","")
         query = query.replace("google about", "")
         webbrowser.open_new_tab(f"https://www.google.com/search?q=" + query)
     elif 'google' in query:
         query = query.replace("friday", "")
         query = query.replace("google", "")
         query = query.replace("google search", "")
         query = query.replace("what is", "")
         query = query.replace("how to", "")
         query = query.replace("who is", "")
         query = query.replace("what do you mean by", "")
         Query = str(query)
         pywhatkit.search(Query)
         if 'how to' in Query:
             max_result = 1
             how_to_func = search_wikihow(query=Query, max_results=max_result)
             assert len(how_to_func) == 1
             how_to_func[0].print()
             speak(how_to_func[0].summary)
         else:

             search = wikipedia.summary(Query,0.5)
             var.set(f"According to Internet: {search}")
             window.update()
             speak(f"According to Internet : {search}")

#whatsapp call,message,calls
     elif 'whatsapp message' in query:
         name = query.replace("whatsapp message", "")
         name = name.replace("send", "")
         name = name.replace("to", "")
         Name = str(name)
         var.set("Alright what's the message")
         window.update()
         speak("Alright what's the message")
         message = takecommand()
         startfile("C:\\Users\\vijit\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
         sleep(3)
         click(x=498, y=129)
         sleep(1)
         write(name)
         sleep(1)
         click(x=366, y=293)
         sleep(2)
         click(x=1341, y=992)
         sleep(2)
         write(message)
         sleep(1)
         press('enter')

     elif 'voice' in query:
         name = query.replace("call", "")
         name = name.replace("voice", "")
         name = name.replace("friday", "")
         Name = str(name)
         startfile("C:\\Users\\vijit\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
         sleep(3)
         click(x=462, y=136)
         sleep(1)
         write(name)
         sleep(1)
         click(x=432, y=311)
         sleep(2)
         click(x=1344, y=982)
         sleep(2)
         click(x=1719, y=65)

     elif 'video' in query:

         name = query.replace("video", "")
         name = name.replace("video", "")
         name = name.replace("call", "")
         name = name.replace("friday", "")
         Name = str(name)
         startfile("C:\\Users\\vijit\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
         sleep(3)
         click(x=479, y=133)
         sleep(1)
         write(name)
         sleep(1)
         click(x=346, y=270)
         sleep(2)
         click(x=1340, y=986)
         sleep(2)
         click(x=1675, y=68)

#write a note
     elif "write a note" in query:
         var.set("What should I write sir")
         window.update()
         speak("What should I write sir")
         note = takecommand()
         file = open('D:\\Users\\vijit\\Documents\\youtube_friday\\important.txt', 'w')
         file.write(note)
#open written note
     elif "show me the note" in query:
         var.set("Showing Notes")
         window.update()
         speak("Showing Notes")
         file = open("D:\\Users\\vijit\\Documents\\youtube_friday\\important.txt", "r")
         print("Friday 2.0 : ", file.read())
         speak(file.read(6))
#open notepad
     elif 'open notepad' in query:
         var.set("Opening notepad")
         speak('opening notepad')
         path = "D:\\Windows.old\\Windows\\notepad.exe"
         os.startfile(path)
#open dictionary
     elif 'dict' in query or 'meaning' in query or 'dictionary' in query:
         Dict()
#open python
     elif 'code' in query:
         var.set("opening...")
         speak('Opening vs code')
         path = "C:\\Users\\vijit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
         os.startfile(path)

     elif 'type' in query:
         var.set("What should I type sir ?")
         window.update()
         speak("What should I type sir ?")
         query = query.replace("type", "")
         comm = takecommand()
         keyboard.write(comm)
#my location
     elif 'my location' in query or 'where am I' in query:

         var.set("Checking...")
         window.update()
         speak("Checking...")
         ip_address = requests.get('https://api.ipify.org').text
         url = 'https://get.geojs.io/v1/ip/geo/' + ip_address + '.json'
         geo_q = requests.get(url)
         geo_d = geo_q.json()
         city = geo_d['city']
         country = geo_d['country']
         var.set(f"You are now in {city, country} .")
         window.update()
         speak(f"you are now in {city, country} .")
         op = "https://www.google.com/maps/place/Methodist+Engineering+College+A-block/@17.3906906,78.4773528,17z/data=!4m12!1m6!3m5!1s0x3bcb99d73d86abaf:0x92b327b7d1dbf501!2sMethodist+Engineering+College+C-block!8m2!3d17.3906906!4d78.4794781!3m4!1s0x0:0x85c03d4d10bf5b62!8m2!3d17.3918031!4d78.4785407"
         webbrowser.open(op)

# Web browsing
     elif 'open website' in query:
         var.set("Tell me the name of the website you want to open \U0001F50E")
         window.update()
         speak("Tell me the name of the website you want to open")
         Website_name = takecommand().lower()
         Website_open = "https://www." + Website_name + '.com'
         webbrowser.open_new_tab(Website_open)
         var.set("Speak to execute lawde")
         window.update()
     elif 'open my mail' in query:
         var.set("Opening Mail")
         window.update()
         speak("Opening your mail Sir, you can check your new mails")
         url="https://mail.google.com/mail/u/0/#inbox"
         webbrowser.get().open(url)
     elif 'youtube search' in query or 'on youtube' in query or 'youtube' in query:
         query = query.replace("friday", "")
         query = query.replace(" on youtube", "")
         query = query.replace("youtube","")
         query = query.replace("search", "")
         query = query.replace("play","")
         result = 'https://www.youtube.com/results?search_query=' + query
         webbrowser.open(result)

         var.set("This is what I found on youtube")
         window.update()
         speak("This is what I found on youtube")

# computer
     elif 'battery' in query or 'check' in query:
         battery = psutil.sensors_battery()
         percentage = battery.percent
         var.set(f"Battery is at {percentage} percent")
         window.update()
         speak(f"Battery is at {percentage} percent")
         if percentage >= 75:
             statement1 = "We have enough battery to continue our work. No need of charging sir."
             var.set(statement1)
             window.update()
             speak(statement1)
         elif percentage >= 40 and percentage <= 75:
             statement2 = "We have enough battery to continue our work. But then also you should plug in the charger."
             var.set(statement2)
             window.update()
             speak(statement2)
         elif percentage >= 15 and percentage <= 39:
             statement3 = "We didn't have enough battery to continue our work. Please plug in the charger sir. "
             var.set(statement3)
             window.update()
             speak(statement3)
         elif percentage >= 0 and percentage <= 14:
             statement4 = "We have no battery to continue our work. Please connect your device to charger otherwise your system will shutdown."
             var.set(statement4)
             window.update()
             speak(statement4)

     elif 'screenshot' in query:
         img = pyautogui.screenshot()
         var.set("what do you want to save it as?")
         window.update()
         speak("what do you want to save it as?")
         filename = takecommand()
         img.save(filename + ".png")
         var.set("Do you want me to show it ?")
         window.update()
         speak("do you want me to show it ?")
         ans = takecommand()
         if "yes" in ans:
             os.startfile(filename + ".png")
         if "no" in ans:
             var.set("As you wish sir !")
             window.update()
             speak("As you wish sir !")

     elif 'website' in query:
         name = query.replace("open", "")
         name = query.replace("website","")
         NameA = str(name)

         if 'facebook' in NameA:
             webbrowser.open("https://www.facebook.com/")
         else:
             string = "https://www." + NameA + ".com"
             string_2 = string.replace(" ", "")
             webbrowser.open(string_2)

# Basic commands
     elif 'hello' in query or 'hi' in query:
         var.set('Hello \U0001F60E')
         window.update()
         speak("Hey, how can I help you?")
         var.set("Press speak ")
         window.update()

     elif 'the time' in query:
         strtime = datetime.datetime.now().strftime("%I:%M:%S %p")
         var.set("Sir the time is %s" % strtime)
         window.update()
         speak("Sir the time is %s" % strtime)

     elif 'the date' in query:
         strdate = datetime.datetime.today().strftime("%d %m %y")
         var.set("Sir today's date is %s" % strdate)
         window.update()
         speak("Sir today's date is %s" % strdate)

     elif 'thank you' in query:
         var.set("Welcome Sir \U0001F917")
         window.update()
         speak("Welcome Sir")
     elif 'say hello' in query:
         var.set('Hello Everyone! My self Friday')
         window.update()
         speak('Hello Everyone! My self Friday')
     elif 'volume up' in query or 'increase the volume' in query:
         print("Friday 2.0 : Increasing the volume")
         pyautogui.press("volumeup")
     elif 'volume down' in query or 'decrease the volume' in query:
         print("Friday 2.0 : Decreasing the volume")
         pyautogui.press("volumedown")
     elif 'volume mute' in query or 'mute' in query:
         print("Friday 2.0 : Muting the volume")
         pyautogui.press("volumemute")
     elif 'shutdown' in query:
         print(" Friday 2.0 : Do you really want to shutdown your Computer?")
         speak("Do you really want to shutdown Your Computer?")
         reply = takecommand().lower()
         if 'yes' in reply:
             print(" Friday 2.0 : Shutting Down System")
             speak("Shutting Down System")
             os.system('shutdown /s /t 1')  # HERE [1] means Second.
         else:
             print("Friday 2.0 : As you wish sir!")
             speak("As you wish sir!")
     elif 'restart' in query or 'reboot' in query or ' reboot the system' in query:
         print(" Friday 2.0 : Do you really want to reboot the system?")
         speak("Do you really want to reboot the system?")
         REPLY = takecommand().lower()
         if 'yes' in REPLY:
             print(" Friday 2.0 : Rebooting System...")
             speak(" Rebooting System")
             os.system("shutdown /r /t 1")
         if 'no' in REPLY:
             print("Friday 2.0 : As you wish sir! ")
             speak("As you wish sir!")
     elif 'calculate' in query:

         app = wolframalpha.Client("V2H2Q6-82GHRHRQQW")
         var.set("What should I calculate?")
         window.update()
         speak("What should I calculate?")
         ans = takecommand().lower()
         res = app.query(ans)
         var.set(f"Answer = {next(res.results).text}")
         speak(next(res.results).text)
         speak("Is the answer")
     elif 'click photo' in query:
         stream = cv2.VideoCapture(0)
         grabbed, frame = stream.read()
         if grabbed:
             cv2.imshow('picture', frame)
             cv2.imwrite('picture.jpg', frame)
         stream.release()

# game -- stone,paper,scissors
     elif 'play game' in query or 'play a game' in query:
         var.set("Choose among rock, paper, scissors")
         window.update()
         speak("Choose among rock, paper, scissors")
         var.set("listening")
         window.update()
         query=takecommand()
         if 'paper'in query or 'rock' in query or 'scissors' in query:
             moves=["rock","paper","scissor"]
             cmove=random.choice(moves)
             var.set("The computer chooses "+cmove)
             window.update()
             speak("The computer choose"+cmove)
             if query==cmove:
                 speak("The match is draw")
             elif query=="rock" and cmove=="paper":
                 speak("computer wins")
             elif query=="paper"and cmove=="scissor":
                 speak("computer wins")
             elif query=="scissor" and cmove=="paper":
                 speak("player wins")
             elif query=="paper" and cmove=="rock":
                 speak("player wins")
             elif query=="rock" and cmove=="scissor":
                 speak("player wins")
             elif query=="scissor" and cmove=="rock":
                 speak("computer wins")

# Corona Updates
     elif 'corona update' in query or 'update' in query or 'updates' in query:
         var.set("Tell me the name of country")
         window.update()
         speak("Tell me the name of country")
         country=takecommand()
         countries = str(country).replace(" ", "")
         url = f"https://www.worldometers.info/coronavirus/country/{countries}/"
         result = requests.get(url)
         soups = bs4.BeautifulSoup(result.text, 'lxml')
         corona = soups.find_all('div', class_='maincounter-number')
         data = []
         for case in corona:
             span = case.find('span')
             data.append(span.string)
         cases, death, recovered = data
         var.set(f"Cases : {cases}")
         window.update()
         speak(f"Cases : {cases}")
         var.set(f"Deaths: {death}")
         window.update()
         speak(f"Deaths: {death}")
         var.set(f"Recovered: {recovered}")
         window.update()
         speak(f"Recovered: {recovered}")

# email sending
     elif 'send mail' in query:
         try:
             speak("What should i send")
             var.set("What should i send")
             window.update()
             content= takecommand()
             to = d
             sendemail(to, content)
             var.set("Email has been sent")
             window.update()
         except Exception as e:
             print(e)
             var.set("Email has not been sent")
             window.update()





     elif 'what is' in query or 'who is' in query or 'how is' in query or 'how was' in query or 'when was' in query or 'temperature' in query or 'cases'in query or 'coronavirus' in query:
         query = query
         print("Searching...")
         query.replace('friday',"")
         try:
             try:
                 res = client.query(query)
                 results = next(res.results).text
                 var.set(results)
                 window.update()
                 speak('According to internet: ')
                 speak(results)
             except:
                 results = wikipedia.summary(query, 1)
                 var.set(results)
                 window.update()
                 speak('According to wikipedia :')
                 speak(results)
         except:
             webbrowser.open('www.google.com')




def update(ind):
     frame = frames[(ind) % 100]
     ind += 1
     label.configure(image=frame)
     window.after(100, update, ind)
def screenshot():
     img = pyautogui.screenshot()
     var.set("what do you want to save it as?")
     window.update()
     speak("what do you want to save it as?")
     filename = takecommand()
     img.save(filename + ".png")
     var.set("Do you want me to show it ?")
     window.update()
     speak("do you want me to show it ?")
     ans = takecommand()
     if "yes" in ans:
         os.startfile(filename + ".png")
     if "no" in ans:
         var.set("As you wish sir !")
         window.update()
         speak("As you wish sir !")


def ClickPhoto():
     stream = cv2.VideoCapture(0)
     grabbed, frame = stream.read()
     if grabbed:
         cv2.imshow('picture', frame)
         cv2.imwrite('picture.jpg', frame)
         stream.release()


def Time():
     strtime = datetime.datetime.now().strftime("%I:%M:%S %p")
     var.set(f"Its {strtime}")
     window.update()
     speak(f"Its {strtime}")


def Date():
     year = int(datetime.datetime.now().year)
     month = int(datetime.datetime.now().month)
     date = int(datetime.datetime.now().day)
     var.set(f"The current date is {date}:{month}:{year} ")
     window.update()
     speak("The current date is")
     speak(date)
     speak(month)
     speak(year)


def Type():
     # This function will type whatever you say
     var.set("What should I type sir ?")
     window.update()
     speak("What should I type sir ?")
     comm = takecommand()
     keyboard.write(comm)
     keyboard.press('enter')

#GUI******************************************************************

label2 = Label(window, textvariable=var1, bg='#FAB60C')
label2.config(font=("Courier", 20))
var1.set('F.R.I.D.A.Y')
label2.pack()

label1 = Label(window, textvariable=var, bg='#ADD8E6')
label1.config(font=("Courier", 16))
var.set('WELCOME SIR')
label1.pack()

frames = [PhotoImage(file='C:\\Users\\vijit\\Downloads\\Assistant.gif' ,format= 'gif -index %i' % (i)) for i in
          range(100)]
window.title('Friday Personal ')

label = Label(window, width=1000, height=500)
label.pack()
window.after(0, update, 0)

wishme()


btn0 = Button(text='SPEAK', width=20, command=TaskExecution, bg='#5C85FB')
btn0.config(font=("Courier", 12))
btn0.pack()


btn1 = Button(text='SCREENSHOT', width=20, command=screenshot, bg='#5C85FB')
btn1.config(font=("Courier", 12))
btn1.pack()

btn3 = Button(text='TAKE PHOTO', width=20, command=ClickPhoto, bg='#5C85FB')
btn3.config(font=("Courier", 12))
btn3.pack()

btn4 = Button(text='TIME', width=20, command=Time, bg='#5C85FB')
btn4.config(font=("Courier", 12))
btn4.pack()

btn5 = Button(text='DATE', width=20, command=Date, bg='#5C85FB')
btn5.config(font=("Courier", 12))
btn5.pack()

btn6 = Button(text='TYPE', width=20, command=Type, bg='#5C85FB')
btn6.config(font=("Courier", 12))
btn6.pack()

btn2 = Button(text='EXIT', width=20, command=sys.exit, bg='#5C85FB')
btn2.config(font=("Courier", 12))
btn2.pack()

window.mainloop()





