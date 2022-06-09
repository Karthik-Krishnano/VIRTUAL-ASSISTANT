#proton

def string(n,m=''):
    #print(n)
    for i in range((len(n)-1),-1,-1):
        #print(i)
        m+=n[i]
    #print(m)
    return m


def encrypt(val,ss='',sss=''):

    val=string(val)
    
    dic={"a":"Q","b":"W","c":"E","d":"R","e":"T","f":"Y","g":"U","h":"I","i":"O",
         "j":"P","k":"A","l":"S","m":"D","n":"F","o":"G","p":"H","q":"J","r":"K",
         "s":"L","t":"M","u":"N","v":"B","w":"V","x":"C","y":"X","z":"Z"}

    dic2={"A":"q","B":"w","C":"e","D":"r","E":"t","F":"y","G":"u","H":"i",
         "I":"o","J":"p","K":"a","L":"s","M":"d","N":"f","O":"g","P":"h",
         "Q":"j","R":"k","S":"l","T":"m","U":"n","V":"b","W":"v","X":"c",
         "Y":"x","Z":"z"}
    
    #print(val)
    s=val.split('/')
    for i in s:
        ss+=i
        ss+=u'\u2023'

    #print(ss)

    r=ss.split('.')
    for j in r:
        sss+=j
        sss+=u'\u00A9'

    #print(sss)

    ns=''

    li1=dic.keys()
    li2=dic2.keys()
    #print(li1,li2)
    for m in sss:
        for n in li1:
            if m==n:
                ns+=dic[n]
        for o in li2:
            if m==o:
                ns+=dic2[o]
        if m not in li1 and m not in li2:
            #print(m)
            ns+=m

    
    print(ns)
    return ns


def decrypt(stri):
    #print(stri)

    dec={"Q":"a","W":"b","E":"c","R":"d","T":"e","Y":"f","U":"g","I":"h",
         "O":"i","P":"j","A":"k","S":"l","D":"m","F":"n","G":"o","H":"p",
         "J":"q","K":"r","L":"s","M":"t","N":"u","B":"v","V":"w","C":"x",
         "X":"y","Z":"z"}
    
    dec2={"z":"Z","x":"Y","c":"X","v":"W","b":"V","n":"U","m":"T","l":"S",
          "k":"R","j":"Q","h":"P","g":"O","f":"N","d":"M","s":"L","a":"K",
          "p":"J","o":"I","i":"H","u":"G","y":"F","t":"E","r":"D","e":"C",
          "w":"B","q":"A"}
    
    ss=''
    s=stri.split(u'\u2023')
    for i in s:
        ss+=i
        ss+='/'

    sss=''

    r=ss.split(u'\u00A9')
    for j in r:
        sss+=j
        sss+='.'

    #print(sss)
    ns=''

    li1=dec.keys()
    li2=dec2.keys()
    #print(dic['a'])
    for m in sss:
        for n in li1:
            if m==n:
                ns+=dec[n]
        for o in li2:
            if m==o:
                ns+=dec2[o]
        if m not in li1 and m not in li2:
            #print(m)
            ns+=m
            
    #print(ns)

    re=string(ns)
    result=re[4:len(re)]
    print(result)



#stri=encrypt('KARTHIK:https://www.learncbse.in/ncert-solutions-for-class-12/')

decrypt('‣21-LLQSE-KGY-LFGOMNSGL-MKTEF‣FO©TLWEFKQTS©VVV‣‣:LHMMI:aoimkqa‣©')
