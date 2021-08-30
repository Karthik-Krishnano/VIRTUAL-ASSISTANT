
#clock
import datetime

cl='12'

def format():
    global cl
    if cl=='12':
        cl='24'
    elif cl=='24':
        cl='12'
#format()

def date():
    months=['January','February','March','April'
            ,'May','June' ,'July','August','September',
            'October','November', 'December' ]
    date=str(datetime.date.today())
    
    da=date.split('-')
    #print(date,da)
    day=da[2]
    month=da[1]
    year=da[0]
    now = datetime.datetime.now()
    dayname=now.strftime("%A")
    #print(month)
    m=(months[int(month)-1])
    if day[1]=='1':
        ext='st'
    elif day[1]=='2':
        ext='nd'
    elif day[1]=='3':
        ext='rd'
    else:
        ext='th'
    if '0' in day[0]:
        day=day[1]
    ddate=day+ext+'  '+m+'  '+year+' '+','+dayname
    #print(ddate)
    return ddate

print(date())

def time():
    global cl
    timenow=str(datetime.datetime.now())
    aa=timenow.split()
    ab=aa[1].split(':')
    hh=ab[0]
    mm=ab[1]
    ss=ab[2]
    h=int(hh)
    if cl=='12':
        if h>12:
            h-=12
            h=str(h)
        if h==0:
            h='12'
    #print(type(h),type(mm))
    time=str(h)+' '+mm
    return time

print(time())

def timer(hr,mts,s):
    format()
    a=time()
    ra=a.split()
    hor=int(ra[0])+hr
    mor=int(ra[1])+mts
    tim='AM'
    
    if mor>59:
        mor-=59
        hor+=1
    if hor>24:
        hor-=24
    if hor>=12:
        tim='PM'
    else:
        tim='AM'

    print(hor,mor,tim) 
#timer(0,0,1)

def stopwatch():
    format()
    #a=time()
    perm=input('Start?[y/n]')
    a=str(datetime.datetime.now())
    r=a.split()
    ra=r[1].split(':')
    #print(ra)
    hor1=int(ra[0])
    mor1=int(ra[1])
    sec1=float(ra[2])
    #print(hor1,mor1,sec1)
    
    permn=input('Stop?[y/n]')
    a=str(datetime.datetime.now())
    r=a.split()
    ra=r[1].split(':')
    #print(ra)
    hor2=int(ra[0])
    mor2=int(ra[1])
    sec2=float(ra[2])
    #print(hor2,mor2,sec2)

    shr=hor2-hor1
    smt=mor2-mor1
    ssc=sec2-sec1

    print('time taken = ',shr,smt,ssc)

#stopwatch()


