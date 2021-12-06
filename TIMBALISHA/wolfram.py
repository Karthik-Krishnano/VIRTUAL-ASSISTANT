'''
import wolframalpha

client=wolframalpha.Client('TR453A-K6KWYAR8QL')

def search_wolfram(que):
    output='  '
    flagwolfram=1
    res=client.query(que)
    #print(res.results)
    output=next(res.results).text
    #print(output)
    return output,flagwolfram

search_wolfram('dog')
'''

# Python program to
# demonstrate creation of an
# assistant using wolf ram API

import wolframalpha

# App id obtained by the above steps
app_id = 'TR453A-K6KWYAR8QL'

# Instance of wolf ram alpha
# client class
client = wolframalpha.Client(app_id)


# Taking input from user
question = input('Question: ')

# Stores the response from
# wolf ram alpha
res = client.query(question)

# Includes only text from the response
answer = next(res.results).text

print(answer)
