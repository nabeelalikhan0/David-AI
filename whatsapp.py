from main import chat
import pyautogui as p
from time import sleep
import webbrowser

webbrowser.open("https://web.whatsapp.com/")
sleep(7)

bell = "img//noti.png"
pin = "img//pin.png"

p.click(402,410)

pin = list(p.locateOnScreen(pin))
width,height = pin[0]+110,pin[1]+10
p.click(width,height)



