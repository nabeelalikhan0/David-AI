import pyttsx3,speech_recognition as sr,random,wikipedia,os,webbrowser,openai,datetime
from config import apikey

chatStr = ""
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Nabeel: {query}\n David:"

    response = openai.Completion.create(
      model="text-davinci-003",
      prompt= chatStr,
      temperature=0.7,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    print(response["choices"][0]["text"])
    speak(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


    # if not os.path.exists("Openai"):
    #     os.mkdir("Openai")
    
    # with open(f"Openai/{''.join(promt.split('intelligence')[1:]).strip()}.txt","w")as f:
    #     f.write(text)


def ai(promt):
    openai.api_key = apikey
    text = f"OpenAI response for Promt: {promt}\n ***********\n \n"

    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=promt,
      temperature=0.7,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]


    if not os.path.exists("Openai"):
        os.mkdir("Openai")
    
    with open(f"Openai/{''.join(promt.split('intelligence')[1:]).strip()}.txt","w")as f:
        f.write(text)



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# def face_recognition():
#     print("Recognizing Face...")
#     speak("Recognizing Face")

    # from virtual.Face_Recognition.main import main as main1
    # main1()
    
lang = "en-in"

def takeCommand(lang):
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language=lang)
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

sites = [["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],["instagram","https://www.instagram.com"],["facebook","https://www.facebook.com"],["google","https://www.google.com"]]


if __name__ == "__main__":
    speak("Hello I am David AI")
    while True:
    # if 1:
        query = takeCommand(lang=lang).lower()

        #Sites
        for site in sites:
            if f"Open {site[0]}".lower() in query:
                print(f"Opening {site[0]} sir")   
                speak(f"Opening {site[0]} sir")   
                webbrowser.open(site[1])


        # Logic for executing tasks based on query
        if 'wikipedia'.lower() in query:
            speak('Searching Wikipedia...')
            if query == "wikipedia":
                results = wikipedia.summary(query, sentences=2)
                print(results)
                speak("According to Wikipedia")

            else:
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                print(results)
                speak(results)

        elif "play music".lower() in query:
            path = random.choice(os.listdir("C://Users//nabee//Music//"))
            os.startfile("C://Users//nabee//Music//"+path)

        elif "the time".lower() in query:
            strftime = datetime.datetime.now().strftime("%H:%M")
            print("Sir the time is ",strftime)
            speak("Sir the time is ",strftime)

        elif "Using artificial intelligence".lower() in query:
            ai(promt=query)

        elif "david quit".lower() in query:
            exit()

        elif "reset chat".lower() in query:
            chatStr = ""


        else:
            print("Chatting")
            chat(query)
