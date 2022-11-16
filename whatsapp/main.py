import pyautogui as pt
from time import sleep
#from comandos. import comando
import pyperclip
import random

sleep(2)
pt.moveTo(pt.locateOnScreen("whatsapp/whatsapp_icon.png", confidence=.9))
pt.click()
sleep(1)
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
    #pt.click()
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
    
    pt.typewrite("\n", interval=.01)


# Processes response
def processes_response(message):
    random_no = random.randrange(3)
    
    if "oi" in str(message).lower():
        return "oii"
    elif "vai amanhã?" in str(message).lower():
        return "Sim"
    elif "/" in str(message):
        return 
    else:
        if random_no == 0:
            return "Provavelmente"
        elif random_no == 1:
            return "ablubluble"
        else:
            return "garay"


# chech new messages
def check_for_new_messages():
    pt.moveTo(x + 50, y - 45, duration=.5)
    grupo = True
    while True:
        #continuously checks
        test_group = "."
        
        try:
            position = pt.locateOnScreen("whatsapp/green_circle.png", confidence=.8)
            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100,0)
                pt.click()
                pt.moveTo(660,65)
                pt.click()
                sleep(1)
                pt.moveTo(860,475)
                pt.tripleClick()
                pt.rightClick()
                pt.moveRel(15,90)
                pt.click()
                test_group = pyperclip.paste()
                if "Grupo" in str(test_group):
                    grupo = True
                    print("grupo",grupo)
                else:
                    grupo = False
                    print("n grupo",grupo)
                sleep(1)
                pt.moveTo(pt.locateOnScreen("whatsapp/close_x.png", confidence = .9))
                pt.click()
                sleep(.5)
            
        except(Exception):
            print("No new other users with new messages located")
        
        if pt.pixelMatchesColor(int(x + 50), int(y - 45),(32,44,51), tolerance = 10) and grupo == False:
            print("is the gray")
            processed_message = processes_response(get_message())
            post_response(processed_message)
        else:
            print("Searching messages...")
        sleep(5)

check_for_new_messages()
#processed_message = processes_response(get_message())
#post_response(processed_message)

