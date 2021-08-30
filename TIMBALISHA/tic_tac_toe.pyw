#tic tak toe

from tkinter import*
import random

moon = Tk()
moon.title("tic tak toe")
moon.configure(background="blue2")
moon.resizable(width=False,height=False)
moon.geometry('168x282+0+0')

man = Frame(moon)
man.grid()

text='O'
chance=1
gtype='machine'
nli=[]
kali='small'

def single():
    global gtype
    gtype='machine'

def multi():
    global gtype
    gtype='man'

def inputData(data):
    x=txtdisp.get('sent',INSERT)
    txtdisp.insert(END,str(data))

def Delete():
    txtdisp.delete('sent',END)
    
def Quit():
    moon.destroy()
    return

def Help():
    root = Tk()
    root.title("RULES")
    root.configure(background="cornflower blue")
    root.resizable(width=False,height=False)
    root.geometry('525x200+0+0')

    txt='\n'+"1. The game is played on a grid that's 3 squares by 3 squares."+'\n'+'\n'+'2. You are O, your friend (or the computer ) is X. Players take '+'\n'+'turns putting their marks in empty squares.  '+'\n'+'\n'+'3. The first player to get 3 of her marks in a row (up, down,    '+'\n'+'across, or diagonally) is the winner.'+'\n'+'\n'+'4. When all 9 squares are full, the game is over. If no player   '+'\n'+'has 3 marks in a row, the game ends in a tie.'

    scr = Label(root, text= txt,fg = "gray1",bg = "linen",font = "Verdana 12")

    scr.pack()

def About():
    root = Tk()
    root.title("About")
    root.configure(background="cornflower blue")
    root.resizable(width=False,height=False)
    root.geometry('485x190+0+0')

    txt='\n'+"You probably already know how to play Tic-Tac-Toe.      "+'\n'+"It's a really simple game, right? That's what most people"+'\n'+"think. But if you really wrap your brain around it, you'll    "+'\n'+"discover that Tic-Tac-Toe isn't quite as simple as you      "+'\n'+"think! Tic-Tac -Toe (along with a lot of other games)       "+'\n'+"involves looking ahead and trying to figure out what  the"+'\n'+" the person playing against you might do next.                "
    scr = Label(root, text= txt,fg = "gray1",bg = "linen",font = "Verdana 12")

    scr.pack()

    txt1='This version of the game is a part of the virtual assistant '+'\n'+'TIMALISHA by KARTHIK KRISHNAN O      '

    scr1 = Label(root, text= txt1,fg = "gray1",bg = "linen",font = "Verdana 12 bold")

    scr1.pack()

   

def Restart():
    global nli
    #li=['b1','b2','b3','b4','b5','b6','b7','b8','b9']
    Delete()
    l=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
    chance=1
    for button in l:
        button['text']=''
        button['bg']='sky blue'
        button['state']='normal'
    nli=[]


def againstme():
    global chance,nli,kali
    
    li=[[b1,b2,b3],[b4,b5,b6],[b7,b8,b9],
        [b1,b4,b7],[b2,b5,b8],[b3,b6,b9],[b1,b5,b9],[b3,b5,b7]]
    l=[b1,b2,b3,b4,b5,b6,b7,b8,b9]

    print('agu')

    for i in li:

        if i[0]['bg']==i[1]['bg']==i[2]['bg']=='red2':
            nli.append(i)

        if (i not in nli) and((i[0]['bg']==i[1]['bg']=='red2') or (i[1]['bg']==i[2]['bg']=='red2')or (i[0]['bg']==i[2]['bg']=='red2'))and (i[0]['bg']!='green2') and (i[1]['bg']!='green2')and (i[2]['bg']!='green2') :
            nli.append(i)
            kali='big'
            if i[0]['bg']!='green2' and i[0]['bg']!='red2':
                i[0]['text']='X'
                i[0]['bg']='green2'
                i[0]['state']='disabled'
            elif i[1]['bg']!='green2'and i[1]['bg']!='red2':
                i[1]['text']='X'
                i[1]['bg']='green2'
                i[1]['state']='disabled'
            elif i[2]['bg']!='green2'and i[2]['bg']!='red2':
                i[2]['text']='X'
                i[2]['bg']='green2'
                i[2]['state']='disabled'
            return
        
        if (i not in nli) and ((i[0]['bg']==i[1]['bg']=='green2') or (i[1]['bg']==i[2]['bg']=='green2')or (i[0]['bg']==i[2]['bg']=='green2'))and (i[0]['bg']!='red2') and (i[1]['bg']!='red2')and (i[2]['bg']!='red2') :
            nli.append(i)
            kali='big'
            
            if i[0]['bg']!='red2' and i[0]['bg']!='green2':
                i[0]['text']='X'
                i[0]['bg']='green2'
                i[0]['state']='disabled'
            elif i[1]['bg']!='red2'and i[1]['bg']!='green2':
                i[1]['text']='X'
                i[1]['bg']='green2'
                i[1]['state']='disabled'
            elif i[2]['bg']!='red2'and i[2]['bg']!='green2':
                i[2]['text']='X'
                i[2]['bg']='green2'
                i[2]['state']='disabled'
            return

    
    if kali=='small':       
        while True:
            
            a=random.randint(1,8)
            button=l[a]
            if l[a]['state']!='disabled':
                button['text']='X'
                button['bg']='green2'
                button['state']='disabled'
                button_element='X'
                return
    else:

        for buu in l:
            
            if buu['state']=='normal':
                buu['text']='X'
                buu['bg']='green2'
                buu['state']='disabled'
                button_element='X'
                return
    


def letter(x):
    global chance,gtype,ag
    
    button=x
    button_element=''
    l=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
    fg=1

    
    if (chance)==1 :
        if button['text']=='':
            button['text']='O'
            button['bg']='red2'
            button['state']='disabled'
            button_element='O'
            for b in l:
                    if b['state']=='normal':
                        chance=0
        
            #chance=0

    for bu in l:
        
        if bu['state']=='normal':
            fg=0
            break
    
    

    if fg==0:
   
        if gtype!='machine' :
            if (chance)==0:
                if button['text']=='':
                    button['text']='X'
                    button['bg']='green2'
                    button['state']='disabled'
                    button_element='X'
                    chance=1
        else:
            if (chance)==0:
                againstme()
                chance=1
                


    flag=1

    opoint=0
    xpoint=0

    li=[[b1,b2,b3],[b4,b5,b6],[b7,b8,b9],
        [b1,b4,b7],[b2,b5,b8],[b3,b6,b9],[b1,b5,b9],[b3,b5,b7]]

    for i in li:
        
        if i[0]['bg']==i[1]['bg']==i[2]['bg']=='green2':
            nm='X'
            xpoint+=1
            Delete()
            inputData(nm+' secured '+str(xpoint)+' point'+'\n')

        if i[0]['bg']==i[1]['bg']==i[2]['bg']=='red2':
            opoint+=1
            nm='O'
            Delete()
            inputData(nm+' secured '+str(opoint)+' point'+'\n')

            
                


    
    for button in l:
        if button['state']=='normal':
            flag=0
    else:
        if flag:
            if opoint==xpoint:
                txt='IT WAS A TIE'
            elif opoint>xpoint:
                txt='O WON'
            elif opoint<xpoint:
                txt='X WON'
            Delete()
            inputData('GAME OVER'+'\n'+txt+'\n'+'O secured '+str(opoint)+
                                             ' point'+'\n'+'X secured '+str(xpoint)+' point')
        


txtdisp=Text(man,bd=10, width=18,height=4,bg='snow',fg='gray1',font='Calibri ')
txtdisp.grid(row=0,column=0,columnspan=5)

b1=Button(man,text='',width=6,height=2,bd=4,command=lambda:letter(b1),bg='sky blue',fg='gray1',font='Helvetica 8 bold')
b1.grid(row=1,column=1,pady=1)

b2=Button(man,text='',width=6,height=2,bd=4,command=lambda:letter(b2),bg='sky blue',fg='gray1',font='Helvetica 8 bold')
b2.grid(row=1,column=2,pady=1)

b3=Button(man,text='',width=6,height=2,bd=4,command=lambda:letter(b3),bg='sky blue',fg='gray1',font='Helvetica 8 bold')
b3.grid(row=1,column=3,pady=1)

b4=Button(man,text='',width=6,height=2,bd=4,command=lambda:letter(b4),bg='sky blue',fg='gray1',font='Helvetica 8 bold')
b4.grid(row=2,column=1,pady=1)

b5=Button(man,text='',width=6,height=2,bd=4,command=lambda:letter(b5),bg='sky blue',fg='gray1',font='Helvetica 8 bold')
b5.grid(row=2,column=2,pady=1)

b6=Button(man,text='',width=6,height=2,bd=4,command=lambda:letter(b6),bg='sky blue',fg='gray1',font='Helvetica 8 bold')
b6.grid(row=2,column=3,pady=1)

b7=Button(man,text='',width=6,height=2,bd=4,command=lambda:letter(b7),bg='sky blue',fg='gray1',font='Helvetica 8 bold')
b7.grid(row=3,column=1,pady=1)

b8=Button(man,text='',width=6,height=2,bd=4,command=lambda:letter(b8),bg='sky blue',fg='gray1',font='Helvetica 8 bold')
b8.grid(row=3,column=2,pady=1)

b9=Button(man,text='',width=6,height=2,bd=4,command=lambda:letter(b9),bg='sky blue',fg='gray1',font='Helvetica 8 bold')
b9.grid(row=3,column=3,pady=1)

br=Button(man,text='RESTART',width=18,height=1,bd=10,command=lambda:Restart(),bg='DodgerBlue2',fg='gray1',font='Calibri')
br.grid(row=4,column=0,columnspan=4,pady=1)


txtdisp.mark_set("sent", INSERT)
txtdisp.mark_gravity("sent", LEFT)

menu=Menu(man)

file=Menu(menu, tearoff=False)
menu.add_cascade(label="File",menu=file)
file.add_command(label="Single Player",command=single)
file.add_command(label="Multi player",command=multi)
file.add_command(label="Quit",command=Quit)

help=Menu(menu, tearoff=False)
menu.add_cascade(label="Help",menu=help)
help.add_command(label="About",command=About)
help.add_command(label="Rules",command=Help)

moon.config(menu=menu)

moon.mainloop()
