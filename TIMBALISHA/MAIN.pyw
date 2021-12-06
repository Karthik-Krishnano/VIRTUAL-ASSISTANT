import pyttsx3
import speech_recognition as sr
import win32api
import musicplayer
import pyt
import webbrowser
#import browser
#import history
import clock
from tkinter import*
import tkinter.messagebox
from PIL import Image
from PIL import ImageTk
from threading import Thread
import os
import sys
import tkinter.scrolledtext as scrolledtext


def exi():
    sys.exit()
    
r=sr.Recognizer()
engine=pyttsx3.init()

assistant='TIM'

moon = Tk()
moon.title("TIMALISHA")
moon.configure(background="ivory3")
#moon.resizable(width=False,height=False)
#moon.geometry('665x444+0+0')
moon.geometry('900x900+0+0')

man = Frame(moon)
man.grid()

txtdisp=Text(man,bd=3, width=80,height=20,bg='ivory2',fg='gray1',font='Calibri ')
txtdisp.grid(row=0,column=0,columnspan=5)
txtdisp.tag_configure("USER",foreground='firebrick1')
txtdisp.tag_configure("TIM",foreground='DarkOrchid4')

engine.say("Hi sir,I'm your assistant. My name is Tim .")
engine.runAndWait()

drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]
driveli=[]
for i in drives:
    ss=i.split(':')
    driveli.append(ss[0]+':')
    
def play(s):
    os.system('python musicplayer.py "'+s+'"')
    #sys.exit()
    os.system('quit()')

def exiit():
    os.system('quit()')
    
def speak(data):
    engine.say(data)
    engine.runAndWait()

def Operate(scrtxt=''):
    data=txtdisp1.get('sent',INSERT)
    txt=data
    Delete1()
    
    
    inputUserData(txt)
    interpret(txt)
line=1
def inputUserData(data):
    global line
    x=txtdisp.get('sent',INSERT)
    
    txtdisp.insert(END,str(data.strip('\n')))
    txtdisp.insert(END,'\n')
    txtdisp.tag_add('USER',f'{line}.0',f'{line}.{len(data)}')
    #print(line,'user',data)
    line+=1
    txtdisp.see('end')
    
def inputData(data):
    global line
    x=txtdisp.get('sent',INSERT)
    txtdisp.insert(END,str(data.strip('\n')))
    txtdisp.insert(END,'\n'*2)
    txtdisp.tag_add('TIM',f'{line}.0',f'{line}.{len(data)}')
    #print(line,'tim',data)
    line+=2
    txtdisp.see('end')
    
def Delete1():
    txtdisp1.delete('sent',END)


def Quit():
    Quit=tkinter.messagebox.askyesno("Quit","Are you sure you want to quit?")
    if Quit==True:
        moon.destroy()
        return

def listening():
    moon.resizable(width=False,height=False)
    moon.geometry('665x444+0+0')
    
    return

def typing():
    moon.resizable(width=False,height=False)
    moon.geometry('665x492+0+0 ')
    
    return

def Help():
    Help=tkinter.messagebox.showinfo()
    return


def interpret(txt):
    global driveli
    
    if 'hi' in txt:
        inputData('Hello sir')
        engine.say('Hello Sir')
        engine.runAndWait()

    elif 'name' in txt and 'you' in txt:
        inputData('My name is TIM and my partners name is ALISHA')
        engine.say('My name is TIM and my partners name is ALISHA')
        engine.runAndWait()

    elif 'favourite' in txt:
        inputData('I love Shivang and Nunu the most')
        engine.say('I love Shivang and Nunu the most')
        engine.runAndWait()
        
    elif 'hello' in txt:
        inputData('Hi sir')
        engine.say('Hi Sir')
        engine.runAndWait()
        
    elif 'how are you' in txt:
        inputData("I'm fine sir")
        engine.say("I'm fine sir")
        engine.runAndWait()
        
    elif 'where are you from' in txt:
        inputData("I'm from a place in india,kunhimangalam")
        engine.say("I'm from a place in india,kunhimangalam")
        engine.runAndWait()
        
    elif ' role model' in txt:
        inputData("My role model is Dr APJ Abdul Kalam, the peoples president,the missile man of india")
        engine.say("My role model is Dr APJ Abdul Kalam, the peoples president,the missile man of india")
        engine.runAndWait()
        
    elif 'who created you' in txt:
        inputData('Karthik Krishnan, a young indian computer science student created me as a part of his school project')
        engine.say('Karthik Krishnan, a young indian computer science student created me as a part of his school project')
        engine.runAndWait()

    elif 'stopwatch' in txt:
        inputData('Here is your stopwatch sir')
        engine.say('Here is your stopwatch sir')
        engine.runAndWait()
        import stopwatch
        
    elif 'bored' in txt:
        brd=('Bored! You will never get bored with your assistant.\
    I will show you the right place ! ENJOY!')
        inputData(brd)
        
        t=Thread(target=speak, args=(brd,))
        t.start()
        webbrowser.open_new_tab('https://www.boredbutton.com')
        
    elif 'change' in txt and ('Alis' in txt or 'alis' in txt):
        a1,a2=pyt.alis()
        inputData(a1)
        
        inputData(a2)
        
        
    elif ('change' ) in txt and ('tim' or 'Tim')in txt:
        #print('ti m')
        b1,b2=pyt.tim()
        inputData(b1)
        
        inputData(b2)
        
        
    elif 'search' in txt:
        lii=txt.split()
        if 'for' in lii:
            browser.search_webbot(lii[2])
            inputData(lii[2])
            
        else:
            browser.search_webbot(lii[1])
            inputData(lii[1])
            
            
            

    elif ('today' and ( 'date' or 'day')) in txt:
            d=clock.date()
            dt='Todays date is '+d
            inputData(dt)
            
            engine.say(dt)
            engine.runAndWait()

    elif ('time' or 'Time') in txt:
        t=clock.time()
        tme='The Time is '+t
        inputData(tme)
        
        engine.say(tme)
        engine.runAndWait()

    elif ('play' or 'Play') in txt:
        
        inputData('playing')
        ll=txt.split()
        inputData(ll)
        
        
        flag = False
        for i in range(len(ll)):
            if ll[i]==('song' or 'Song' or 'music' or 'Music'):
                #print(ll[i+1])
                ass=i
                flag=True
                break

        if flag==False:
            for i in range(len(ll)):
                if ll[i]==(('play' or 'Play')):
                    ass=i
                    inputData(ass)
                    
                    
        
        for j in driveli:
           
            s=musicplayer.find(ll[ass+1],j)
            if s!=None:
                
                if s.endswith('.mp3'):
                    inputData(s)
                    wow=0

                    try:
                        print(s)
                        t1=Thread(target=play,args=(s,))
                        t1.start()
                        
                        wow=1
                    except:
                        pass
                        

    elif ('what is' in txt) or ('what are'  in txt)or('who is' in txt) or ('who are' in txt)  or ('wikip' in txt):
        
        if 'what is'in txt:
            li=txt.split('what is')
        elif 'what are' in txt:
            li=txt.split('what are')
        elif  'who is' in txt:
            li=txt.split('who is')
        elif 'who are' in txt:
            li=txt.split('who are')
        elif 'wikip' in txt:
            li=txt.split('wikipedia')

        enc=browser.search_wiki(li[1])
        a=enc.split('.')
        resu='Here is some matching results'
        inputData(resu)
        

        sayi=a[0]+'.'+a[1]+'.'+a[2]+'.'
        
        inputData(sayi)
        
        #print(sayi)

        t=Thread(target=speak, args=(resu))
        t.start()
        t=Thread(target=speak, args=(sayi))
        t.start()

    elif ('break' in txt )or ('bye' in txt )or ('Bye' in txt) or ('quit' in txt )or ('Quit' in txt ):
            inputData('Bye sir')
            engine.say('Bye sir')
            engine.runAndWait()
            #Quit()
            quit()
    elif ('shutdown' in txt):
        inputData('SHUTTING DOWN THE SYSTEM')
        engine.say('SHUTTING DOWN THE SYSTEM')
        engine.runAndWait()
        #os.system('shutdown /s /t 1')
       
        
        
##        question='Are you satisfied with the result?[y,n]'
##        ds=input(question)
##        if ds=='n':
##            output,flagwolfram=browser.search_wolfram(li[1])
##            if flagwolfram==1:
##                engine.say(output)
##                engine.runAndWait()
##            else:
##                print()

    


def listen():
    with sr.Microphone() as source:
        inputData("How can I help u?")
        
        engine.say('How can I help u?')
        engine.runAndWait()
        inputData('Listening....')
        
        aud=r.listen(source)

    try:
        txt=r.recognize_google(aud)
        inputUserData(txt)
        
        interpret(txt)
    
    except:
        inputData('Ooops!,I did not get that')
        
        engine.say('Ooops!,I did not get that')
        engine.runAndWait()
    
    return




ProgressScroll=Scrollbar(man,orient='vertical')
ProgressScroll.config(command=txtdisp.yview)
ProgressScroll.grid(row=0,rowspan=10,column=5)
txtdisp.config(yscrollcommand=ProgressScroll.set)

##scrollb = tkinter.Scrollbar(man, command=txtdisp.yview)
##txtdisp['yscrollcommand']=scrollb.set

mon = Frame(moon)
mon.grid()

def mic():
    #inputData('Listening')
    listening()
    listen()

def keyboard():
    txtdisp1.focus()
    #print('Writing')
    typing()

width = 50
height = 50
img = Image.open("close.gif")
img = img.resize((width,height), Image.ANTIALIAS)
photoImg =  ImageTk.PhotoImage(img)
b = Button(mon,image=photoImg,command=mic,width=50)
#moon.bind('<Return>', lambda event=None: b1.invoke())
b.pack(side = LEFT,fill = BOTH, expand = True)

width = 50
height = 50
img1 = Image.open("timbumic.gif")
img1 = img1.resize((width,height), Image.ANTIALIAS)
photoImg1 =  ImageTk.PhotoImage(img1)
b1 = Button(mon,image=photoImg1,command=mic,width=50)
b1.pack(side = LEFT,fill = BOTH, expand = True)


##b = Button(mon,text='YES',command=Operate,width=50)
##moon.bind('<Return>', lambda event=None: b.invoke())
##b.pack(side = LEFT,fill = BOTH, expand = True)

width = 50
height = 50
img3 = Image.open("timbukeyboard.gif")
img3 = img3.resize((width,height), Image.ANTIALIAS)
photoImg3 =  ImageTk.PhotoImage(img3)
b3 = Button(mon,image=photoImg3,command=keyboard, width=50)
b3.pack(side = LEFT,fill = BOTH, expand = True)

width = 50
height = 50
img2 = Image.open("set.gif")
img2 = img2.resize((width,height), Image.ANTIALIAS)
photoImg2 =  ImageTk.PhotoImage(img2)
b2 = Button(mon,image=photoImg2,command=Operate,width=50)
moon.bind('<Return>', lambda event=None: b2.invoke())
b2.pack(side = LEFT,fill = BOTH, expand = True)

maan=Frame(moon)
maan.grid()

txtdisp1=Text(maan,bd=3, width=80,height=2,bg='ivory1',fg='gray1',font='Calibri ')
txtdisp1.grid(row=2,column=0,columnspan=5)

txtdisp.mark_set("sent", INSERT)
txtdisp.mark_gravity("sent", LEFT)

txtdisp1.mark_set("sent", INSERT)
txtdisp1.mark_gravity("sent", LEFT)

menu=Menu(man)

file=Menu(menu, tearoff=False)
menu.add_cascade(label="File",menu=file)
##file.add_command(label="listening",command=listening)
##file.add_command(label="typing",command=typing)
file.add_command(label="Quit",command=Quit)

help=Menu(menu, tearoff=False)
menu.add_cascade(label="Help",menu=help)
help.add_command(label="May I help you",command=Help)


moon.config(menu=menu)
moon.mainloop()



