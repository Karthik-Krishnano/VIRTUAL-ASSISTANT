import wikipedia as wiki
import wolframalpha
import webbot as w


def search_wolfram(question):
    app_id = 'TR453A-K6KWYAR8QL'
    client = wolframalpha.Client(app_id)
    try:
        res = client.query(question)
        answer = next(res.results).text
    except:
        answer="Sorry, Found nothing relevent"
    return (answer)

def search_webbot(url):
    web=w.Browser()
    web.go_to('google.com')
    web.type(url)
    web.press(web.Key.ENTER)

    
def search_wiki(que):
    a=wiki.search(que)
    #print(a)
    try:
        output=wiki.summary(a[0])
    except wiki.exceptions.DisambiguationError as e:
        y=e.options
        output=wiki.summary(y[0])
    return output

if __name__ == "__main__":

    print("According to Wolfram Alpha")
    print(search_wolfram('what is the time now?'))

    print("\n\n")

    print("According to Wikipedia")
    print(search_wiki('What is Artificial Intelligence?'))

    print("\n\n")

    print("According to Webbot")
    print(search_webbot('What is Artificial Intelligence?'))

