import pyttsx3
import speech_recognition as sr
import music
import browser
from flask import Flask, render_template, Response, request
import cv2
import datetime, time
import os, sys
import numpy as np
from  threading import Thread

r=sr.Recognizer()
engine=pyttsx3.init()
engine.say("Hi sir,I'm your assistant.")
engine.runAndWait()

global capture,rec_frame, grey, switch, neg, face, rec, out 
capture=0
grey=0
neg=0
face=0
switch=1
rec=0

#instatiate flask app  
app = Flask(__name__, template_folder='./templates')


camera = cv2.VideoCapture(0)

def gen_frames():  # generate frame by frame from camera
    global out, capture,rec_frame
    while True:
        success, frame = camera.read() 
        if success:
            if(face):                
                frame= detect_face(frame)
            if(grey):
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            if(neg):
                frame=cv2.bitwise_not(frame)    
            if(capture):
                capture=0
                now = datetime.datetime.now()
                p = os.path.sep.join(['shots', "shot_{}.png".format(str(now).replace(":",''))])
                cv2.imwrite(p, frame)
            
            if(rec):
                rec_frame=frame
                frame= cv2.putText(cv2.flip(frame,1),"Recording...", (0,25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),4)
                frame=cv2.flip(frame,1)
            
                
            try:
                ret, buffer = cv2.imencode('.jpg', cv2.flip(frame,1))
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            except Exception as e:
                pass
                
        else:
            pass

def speak(txt):
    engine.say(txt)
    engine.runAndWait()

def output(reply):
    t1 = Thread(target=speak, args=(reply,))
    t1.start()
    #t1.join()


def interpret(txt):
    reply=''
    if "play" in txt:
        #need=txt.split("play")[2]
        #print(txt.split("play"))
        reply="Playing the song"
        music.playvideo(music.search_youtube(txt))

    elif "what" in txt or "where" in txt or "why" in txt or "how" in txt:
        print(browser.search_wolfram(txt))
        reply=browser.search_wolfram(txt)
        if reply=='':
            reply=browser.search_wiki(txt)

    elif "hello" in txt:
        print("Hi")

    output(reply)
    return reply

@app.route('/listen')
def listen():
    with sr.Microphone() as source:
        speak('How can I help u?')
        print("Listening...")
        aud=r.listen(source)

    try:
        txt=r.recognize_google(aud)
        print(txt)
        interpret(txt)
        print("done")
       
    except:
        speak('Ooops!,I did not get that') 
            
    return render_template('index.html')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/requests',methods=['POST','GET'])

def tasks():
    global switch,camera
    choice="text"

    if request.method == 'POST':
        print(request.form.get('lname'))

        if (request.form.get('lname')!=""):
            reply=interpret(request.form.get('lname'))
        if request.form.get('video') == 'VideoInput':
            choice="video"
            #print("Video")
        elif  request.form.get('audio') == 'VoiceInput': 
            #print("Audio")
            choice="audio"
        elif  request.form.get('text') == 'TextInput':
            choice="text"
            #print("Text")

        print(choice)

    elif request.method=='GET':
        return render_template('index.html')
    return render_template('index.html',results=reply)


if __name__ == '__main__':
    app.run()

