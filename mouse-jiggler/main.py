import pyautogui as pag
from pymsgbox import *
# import random
import time

# while True :
#     x = random.randint(600,700)
#     y = random.randint(200,600)
#     pag.moveTo(x, y, 0.5)
#     time.sleep(5)

seconds = 30

print("Auto mouse-jiggler activated. Press ^C to cancel")
alert(text='', title='', button='OK')

try:
    while True :
        x,y = pag.position()
        x += 1
        pag.moveTo(x, y)
        time.sleep(seconds)

        x,y = pag.position()
        x -= 1
        pag.moveTo(x, y)
        time.sleep(seconds)

except KeyboardInterrupt:
    print("\nAuto mouse-jiggler deactivated.")

