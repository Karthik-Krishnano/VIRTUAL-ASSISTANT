import tkinter as tk

sco=0
mco=0
hco=0
flag=False

def allzero():
    sco=0
    mco=0
    hco=0
    
def counter(scr):
  def count():
    global sco,mco,hco
    if flag:
        ho=str(hco)
        mo=str(mco)
        so=str(sco)
        
        if len(ho)!=2:
            ho='0'+ho
        if len(mo)!=2:
            mo='0'+mo
        if len(so)!=2:
            so='0'+so
            
        scrtxt=ho+':'+mo+':'+so
        
        scr.config(text=scrtxt,fg = "blue",
		 bg = "yellow",font = "Verdana 18 bold")
        
        scr.after(1000, count)
        
        if sco==60:
            mco+=1
            sco=0
        if mco==60:
            hco+=1
            mco=0
            
        sco += 1
  count()
 
 
root = tk.Tk()
root.title("stopwatch")
scrF = tk.Label(root, text= 'STOPWATCH',fg = "blue",
		 bg = "IVORY3",
		 font = "Verdana 18 bold")

scrF.pack()

scr = tk.Label(root, text= '00:00:00',fg = "blue",
		 bg = "yellow",
		 font = "Verdana 18 bold")

scr.pack()

def start(scr):
    global flag
    global sco,mco,hco
    flag=True
    b1['state']='disabled'
    b2['state']='normal'
    b3['state']='normal'
    counter(scr)

def reset(scr):
    global flag
    global sco,mco,hco
    sco=0
    mco=0
    hco=0
    b1['state']='normal'
    b2['state']='normal'
    b3['state']='disabled'
    scr['text']='00:00:00'
    flag=False

def pause(scr):
    global flag
    global sco,mco,hco
    b1['state']='normal'
    b2['state']='disabled'
    b3['state']='normal'
    flag=False
    
    
b1=tk.Button(root,text='START',command=lambda:start(scr))
b1.pack(side = tk.LEFT,fill = tk.BOTH, expand = True)

b2=tk.Button(root,text='PAUSE',command=lambda:pause(scr))
b2.pack(side = tk.LEFT,fill = tk.BOTH, expand = True)

b3=tk.Button(root,text='RESET',command=lambda:reset(scr))
b3.pack(side = tk.LEFT,fill = tk.BOTH, expand = True)


root.mainloop()
