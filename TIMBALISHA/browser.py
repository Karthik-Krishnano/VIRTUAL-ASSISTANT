import wikipedia as wiki
import wolframalpha
import webbot as w

client=wolframalpha.Client('TR453A-R8X2GE4653')

def langchange(la):
    wiki.set_lang(la)
    print('language changed')

def page(pg,im=0,li=0):
    p=wiki.page(pg)
    t=p.title
    u=p.url
    c=p.content
    i=p.images[im]
    l=p.links[li]
    print(p,t,u,c,i,l,end='\n')

def search_webbot(url):
    web=w.Browser()
    web.go_to('google.com')
    web.type(url)
    web.press(web.Key.ENTER)

#search_webbot('')

def search_wolfram(que):
    output='  '
    try:
        flagwolfram=1
        res=client.query(que)
        #print(res.results)
        output=next(res.results).text
        #print(output)
    except:
        #print('no information found')
        flagwolfram=0
        search_webbot(que)
    return output,flagwolfram

#search_wolfram('dog')

def search_wiki(que):
    a=wiki.search(que)
    #print(a)
    try:
        output=wiki.summary(a[0])
    except wiki.exceptions.DisambiguationError as e:
        y=e.options
        output=wiki.summary(y[0])
    #print(output)
    return output

#search_wiki(que)

