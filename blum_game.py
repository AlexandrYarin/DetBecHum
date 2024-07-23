import pyautogui as pa
import time
import random 
import json


#-----------------/////-------------------

with open('jsons\\coordinates.json', 'r') as file:
    coor = json.load(file)

coor_b = coor['quests']['blum']
c_gram = coor['telegram']

REGION = (1505, 250, 380, 610) #область работы бота
OFFSET = 50 #смещение клика от найденных координат
DELAY = (0.03, 0.07) #задержка между кликами
CONFIDENCE = 0.6 #качество распознания
PAC_GAMES = map(int, str(input('Сколько игр нужно сделать? >>> ')).split(' ')) #кол-во игр которое нужно сыграть
GAME_BUTTON = coor_b['game_but'] #координаты кнопки начала игры
FIRST_PLAY = coor_b['first_play'] #координаты кнопки первой игры
SCROLL_BAR = coor_b['scroll_bar']


#-----------------/////-------------------

def blum_game_start():
    
    def find_star(end_time):
    
        while time.time() <= end_time:
            try:
                x, y = pa.locateCenterOnScreen('blum_game\\star4.png', region=REGION, confidence=CONFIDENCE, grayscale=True)
                pa.click(x, y + OFFSET)
                time.sleep(random.uniform(*DELAY))
            except pa.ImageNotFoundException:
                continue
        #заcыпание перд новой попыткой
        time.sleep(random.randrange(6,10))
    
    for n_pack in PAC_GAMES:
        for i in range(n_pack):
            if i == 0:
                pa.moveTo(*SCROLL_BAR, duration=0.5)
                pa.drag(0, 100, button='left', duration=0.7)
                pa.click(*FIRST_PLAY, duration=0.7)
            pa.click(*GAME_BUTTON)
            time.sleep(2)
            end_time = time.time() + 28
            find_star(end_time)
        
        pa.click(*c_gram['exit_quest'], duration=0.5)
        time.sleep(1)
        pa.click(*coor_b['start'], duration=0.5)
        time.sleep(random.randrange(15,20))
        pa.click(*coor_b['continue'])
        time.sleep(4)
        pa.click(*coor_b['continue'])
        time.sleep(4)