import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(str):
    engine.say(str)
    engine.runAndWait()

if __name__ == '__main__':
    import requests
    import json
    url = ('http://newsapi.org/v2/top-headlines?country=in&apiKey=<get your api key at newsapi.org>')
    n = int(input("No . of news Headlines"))   #Input number of news you want to listen
    response = requests.get(url)
    text = response.text
    my_json = json.loads(text)
    for i in range(0, n):
        print(my_json['articles'][i]['title'])
        speak(my_json['articles'][i]['title'])
