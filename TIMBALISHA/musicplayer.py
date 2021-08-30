import os
from playsound import playsound
import random
import sys

def naming(name):
    
    from pydub import AudioSegment
    sound = AudioSegment.from_wav(name)

    sound.export(name+'.mp3', format='mp3')

def check(wr):
    ww=wr.split()
    
    we=(ww[0])
    if ww[0]==(''or ' '):
        we=(ww[1])
    wq=we
    
    li=[]
    li.append(wq)
    li.append(wq.capitalize())
    li.append(wq.upper())
    li.append(wq.lower())
    return li

def find(name, path):
    li=check(name)
   
    for root, dirs, files in os.walk(path):
        for j in files:
            for i in li:
                if i in j:
                    return os.path.join(root, j)

if __name__=='__main__':            
    playsound(sys.argv[1])
    input()


def record(name,duration):
    import sounddevice as sd
    from scipy.io.wavfile import write
    
    fs = 44100  # Sample rate
    seconds = duration # Duration of recording
    print('recording')
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write(name+'.wav', fs, myrecording)  # Save as WAV file

    print('recorded')

def play(path):
    seq=os.listdir(path)
    print(seq)
    se=os.listdir(path+'\\'+seq[0])
    print(se[0])
    s=path+'\\'+seq[0]+'\\'+se[18]
    print(s)
    #musicplayer.music(s)
    return s

choice='shuffle'
num=-1

def checkr(path):
    global num,choice
    try:
        num=-1
        li=os.listdir(path)
        #print(li)
        lifolder=[]
        linrml=[]
        for i in li:
            patn=path+'\\'+i
            if os.path.isdir(patn):  
                #print("\nIt is a directory")
                lifolder.append(patn)
            elif os.path.isfile(patn):  
                #print("\nIt is a normal file")
                linrml.append(patn)

        #print(lifolder)
        lisong=[]

        for i in range(len(linrml)):
            if linrml[i].endswith(".mp3"):
                pa=os.path.join(path,li[i])
                lisong.append(pa)
                
        for i in range(len(lisong)):
            if choice=='shuffle':
                sdd=random.randint(0,len(lisong)-1)
                #music(lisong[sdd])
            else:
                #music(lisong[i])
                print()
        else:
            num+=1
            
            try:
                num+=1
                checkr(lifolder[num])
            except:
                print()
    except:
        print()
            
