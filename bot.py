from tkinter import *
from tkinter import ttk
from gtts import gTTS
import speech_recognition
import playsound

def listener():
    record = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as source :
        print("I'm listening")
        audio = record.listen(source,phrase_time_limit=5)

    try :
        text = record.recognize_google(audio,language="en-US")
        return text
    
    except :
        print("Sorry , i can't recognize what you are saying :)")
        return 0    

def speaker(text,file):
    tts = gTTS(text=text,lang="en")
    file_name = "%s.mp3"%file
    tts.save(file_name) 
    playsound.playsound(file_name)

def contact():
    text_returned = listener()
    if text_returned == "hello" :
        speaker("Hi Who are you","d")
        phrase = listener()
        name= phrase.split()[-1]
        speaker("You're welcome %s"%name,"p")
    if text_returned == "are you a robot" :
        speaker("It's not of your business","t")

root = Tk()

root.title("Bot")
root.geometry("200x300")
root.resizable(False,False)
pic = PhotoImage(file="bot.png")
Label(root,image=pic).place(x=0,y=0)
ttk.Button(root,text = "START",command=lambda:contact()).grid()
root.mainloop() 