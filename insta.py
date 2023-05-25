import openai
from config import apikey
import os
import pyautogui as p,webbrowser
from time import sleep

lang = 'hi-in'

# bio = "and Well Nabeel Ali Khan is my master is the man who created me and by profession he is a ethical hacker and a programmer and he knows very diffrent programming and spoken languages like python russion french java and more"

bio = "And by the way nabeel ali khan is my master who made me and by profession he is an ethical hacker and a programmer and he know very different programming and spoken languages like python russian french java and many more"


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
    chatStr += f"{response['choices'][0]['text']}\n"


    return response["choices"][0]["text"]




# chat(query="")
webbrowser.open("https://www.instagram.com/direct/inbox/")

msg = "img//msg.png"
emoji = "img//emoji.png"
dot = "img//dots.png"
copy = "img//copy.png"

# sleep(3)
# p.click(p.locateOnScreen(msg))
sleep(8)

p.click(433,370)
sleep(3)
p.moveTo(915,926)

sleep(1)
dots = list(p.locateOnScreen(dot))
# print(dots[1],dots[2])
p.click(dots)

width,height = int(dots[0]),int(dots[1])
sleep(1)
p.click(width+155,height-50)
sleep(1)
os.startfile("db.txt")
sleep(1)
p.hotkey("ctrl","a")
p.hotkey("ctrl","v")
p.hotkey("ctrl","s")


p.hotkey("alt","f4")
sleep(1)
emoji = list(p.locateOnScreen(emoji))
p.click(emoji[0]+100,emoji[1]+10)
# p.click(1202,974)
p.typewrite("Generating Response...")
p.press('enter')

with open("db.txt")as f:
    f = chat(query=f.read())
    if "nabeel".lower() in f.lower():
        f += " "+bio
        # f += " and Nabeel Ali Khan is my master"



sleep(1)
p.typewrite(f)
p.press('enter')