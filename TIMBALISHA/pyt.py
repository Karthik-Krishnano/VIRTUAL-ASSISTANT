#pyttsx3
import pyttsx3
engine=pyttsx3.init()
nre=0
def rateofspeech(txt):
    global nre
    
    if nre==0:
        re=engine.getProperty('rate')
        nre=re
        
    if 'increase' in txt:
        nre=nre+10
        engine.setProperty('rate',nre)
        
    if 'decrease' in txt:
        nre=nre-10
        engine.setProperty('rate',nre)
   
    engine.say('DONE')
    engine.runAndWait()

def alis():
    output1=('Changing sir. Thank you for using me. Hope you will call me back,bye')
    engine.say(output1)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say('Hello sir, I am your new assistant Alisa.')
    output2=('Hello sir, I am your new assistant Alisa.')
    engine.runAndWait()
    return output1,output2

def tim():
    outpt1=('Changing sir. Thank you for using me. Bye . Hope you will call me back.')
    engine.say('Changing sir. Thank you for using me. Bye . Hope you will call me back.')
    engine.runAndWait()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say('Hello sir, I am your new assistant tim.')
    outpt2=('Hello sir, I am your new assistant tim.')
    engine.runAndWait()
    return outpt1,outpt2
#input("No Error")



