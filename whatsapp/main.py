import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(3)

position1 = pt.locateOnScreen("whatsapp/smiley_paperclip.png", confidence=.6)
x = position1[0]
y = position1[1]

#Get message
def get_message():
    global x, y
    
    position = pt.locateOnScreen("whatsapp/smiley_paperclip.png", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x,y, duration=.05) #only for mac, in windows its okay noto to declar the duration
    pt.moveTo(x + 60, y - 60, duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(50,-221)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("Message received: " + whatsapp_message)
    
    return whatsapp_message


# Posts
def post_response(message):
    global x ,y
    
    position = pt.locateOnScreen("whatsapp/smiley_paperclip.png", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x + 200, y + 20, duration=.5)
    pt.click()
    pt.typewrite(message, interval=.01)
    
    #pt.typewrite("\n", interval=.01)


# Processes response
def
    
post_response(get_message())