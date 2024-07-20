import pyautogui as pa
import time
import random




REGION = (1550, 50, 40, 700)
CONFIDENCE = 0.9

pages = {'b':'blum.png', 'p':'pocket.png', 'h':'hexacore.png', 'y':'yes.png', 's':'snapster.png',}

while True:
    answer = input('Название квеста >>>>> ')
    x,y = pa.locateCenterOnScreen(pages[answer], region=REGION, confidence=CONFIDENCE)
    pa.moveTo(x,y, duration=1)
    time.sleep(3)