import time
import pyautogui as pa
import random
import json
from blum_game import blum_game_start


with open('jsons\\coordinates.json', 'r') as file: coor = json.load(file)

c_gram = coor['telegram']
c_text = coor['text_file']
c_quests = coor['quests']

buttons_b = c_quests['blum']
buttons_p = c_quests['pocket']
buttons_y = c_quests['yes']
buttons_h = c_quests['hexacore']
buttons_s = c_quests['snap']



def blum(mode):
    
    pa.click(*buttons_b['start'])
    time.sleep(random.randrange(15,20))
    pa.click(*buttons_b['continue'])
    time.sleep(4)
    pa.click(*buttons_b['continue'])
    time.sleep(4)
    
    if mode == 'claim':
    
        pa.click(buttons_b['claim-farming'])
        time.sleep(3)
        pa.click(buttons_b['claim-farming'])
        time.sleep(2)
    
    else:
        try:
            blum_game_start()
            logs(4, 'b', 'Blum is been through every game.')
        except Exception as e:
            logs(2, 'b', f'blum_game error >>>>> {e}')
            
        
    
    
    pa.click(*c_gram['exit_quest'])
    time.sleep(1.5)
    
    
def yescoin(mode):
    for i in range(3):
        pa.click(*buttons_y['start'], duration=1)
        time.sleep(1)
    
    time.sleep(2)
    pa.click(*buttons_y['start2'], duration=1)
    time.sleep(19)
    
    if mode == 'claim':
        pa.click(*buttons_y['get_coin'])
        time.sleep(3)
        pa.click(*buttons_y['exit_daily'])
        time.sleep(2)
        
    else:
        
        pa.click(*buttons_y['get_coin'])
        time.sleep(3)
        pa.click(*buttons_y['exit_daily'])
        time.sleep(80)
        
        for i in range(3):
            pa.click(*buttons_y['build'])
            time.sleep(3)
            pa.click(*buttons_y['try'])
            time.sleep(4)
            pa.click(*buttons_y['back'])
            time.sleep(80)
            
    pa.click(*c_gram['exit_quest'])
    time.sleep(1.5)
    pa.click(*c_gram['exit_quest2'])
    


def pocket(mode):
    
    pa.click(*buttons_p['start'], duration=1)
    time.sleep(7)
    
    for i in range(3): pa.click(*buttons_p['claim'], interval=1)
    time.sleep(1.5)
    pa.click(*buttons_p['tasks'])
    time.sleep(1.5)
    pa.click(*buttons_p['daily'])
    time.sleep(1.5)
    pa.click(*buttons_p['take_reward'])
    time.sleep(3)
    
    
    pa.click(*c_gram['exit_quest'])
    time.sleep(1.5)
    
    
def snapster(mode):
    pa.click(*buttons_s['start'])
    time.sleep(7)
    pa.click(*buttons_s['claim'])
    time.sleep(3)
    
    pa.click(*c_gram['exit_quest'])
    time.sleep(1.5)
    

def hexacore(mode):
    
    pa.click(*buttons_h['start'])
    time.sleep(7)
    
    if mode == 'claim':
        pa.click(*buttons_h['claim'])
        time.sleep(3)
        pa.click(*buttons_h['claim2'])
        pa.sleep(2)
    
    else:
        for i in range(11000):
            pa.click(*buttons_h['push'])
            time.sleep(random.uniform(0.1,0.2))
    
    pa.click(*c_gram['exit_quest'])
    time.sleep(1.5)

def tabizoo(mode):
    pa.click(1856, 200, duration=1)
    
from main import logs