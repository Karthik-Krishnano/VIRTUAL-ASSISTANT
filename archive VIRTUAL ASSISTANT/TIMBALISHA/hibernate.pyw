import pyttsx3
import os

eng=pyttsx3.init()
eng.say('Bro KARTHIK , You are suspending the computer. ')
eng.runAndWait()

os.system("shutdown.exe /h")
