import time
import pyautogui as pa
import random
import json
from blum_game import blum_game_start
from logs import logs


with open('jsons\\coordinates.json', 'r') as file: coor = json.load(file)

pac_games = input('Сколько игр нужно сделать? >>> ')


c_gram = coor['telegram']
c_quests = coor['quests']

buttons_b = c_quests['blum']
buttons_p = c_quests['pocket']
buttons_y = c_quests['yes']
buttons_h = c_quests['hexacore']
buttons_s = c_quests['snap']
buttons_t = c_quests['tabizoo']
buttons_d = c_quests['dogs']


def claytoncoin(mode):
    pass


def yumify(mode):
    pass


def nasduck(mode):
    pass


def dogs(mode):
    pa.click(*buttons_d['start'], duration=0.5)
    time.sleep(8)
    pa.click(*c_gram['exit_quest'], duration=0.5)
    time.sleep(1.5)


def tabizoo(mode):
    
    dur = 0.5
    
    #start quest
    pa.click(*buttons_t['start'], duration=dur)
    pa.click(*buttons_t['start2'], duration=dur+2)
    time.sleep(10)
    
    def basic():
        pa.click(*buttons_t['checkin'], duration=dur)
        pa.click(*buttons_t['checkin2'], duration=dur+0.5)
        pa.click(*buttons_t['checkin_confirm'], duration=dur+0.5)
        time.sleep(2)
        pa.click(*buttons_t['claim'], duration=dur+0.5)
        pa.click(*buttons_t['claim_confirm'], duration=dur+0.5)
        time.sleep(2)
    
    def farm():
        pa.click(*buttons_t['upgrade'], duration=dur)
        pa.click(*buttons_t['upgrade2'], duration=dur+0.5)
        pa.click(*buttons_t['upgrade_exit'], duration=dur+0.5)
        time.sleep(2)
    
    if mode == "claim":
        basic()
        
    elif mode == "farm":
        farm()

    else:
        basic()
        farm()     
    
    pa.click(*c_gram['exit_quest'])
    time.sleep(1.5)
    



def blum(mode):
    
    if pac_games == 'd':
        pac = [5, 5]
    else:
        pac = list(map(int, pac_games.split(' '))) #кол-во игр которое нужно сыграть
    
    logs(2, 'o', f'games -> {pac}')
    
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
    elif mode == 'farm':        
        
        try:
            blum_game_start(pac)
            logs(4, 'b', 'Blum is been through every game.')
        except Exception as e:
            logs(2, 'b', f'blum_game error >>>>> {e}')
    
    else:
        pass
            
        
    
    
    pa.click(*c_gram['exit_quest'])
    time.sleep(1.5)
    
    
def yescoin(mode):
    for i in range(3):
        pa.click(*buttons_y['start'], duration=1)
        time.sleep(1)
    
    time.sleep(2)
    pa.click(*buttons_y['start2'], duration=1)
    time.sleep(15)
    
    if mode == 'claim':
        pa.click(*buttons_y['get_coin'])
        time.sleep(3)
        pa.click(*buttons_y['exit_daily'])
        time.sleep(2)
        
    elif mode == 'farm':
        
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
    else:
        pass
            
    pa.click(*c_gram['exit_quest'])
    time.sleep(1.5)
    pa.click(*c_gram['exit_quest2'])
    


def pocket(mode):
    
    pa.click(*buttons_p['start'], duration=1)
    time.sleep(7)
    
    for i in range(3):pa.click(*buttons_p['claim'], duration=0.3)
    
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
    d= 0.5
    
    
    #store in
    pa.click(*buttons_h['store'], duration=d)
    time.sleep(2)
    #store2
    pa.click(*buttons_h['store2'], duration=d)
    #scrollbar down
    pa.moveTo(*buttons_b['scroll_bar'], duration=d)
    pa.drag(0, 100, button='left', duration=d + 0.5)
    #buy clicks
    pa.click(*buttons_h['clicks'], duration=d)
    #main menu
    pa.click(*buttons_h['main_menu'], duration=d)
    time.sleep(2)
    
    def claim():
        
        pa.moveTo(*buttons_h['scroll_bar'], duration=d)
        pa.drag(0, 100, button='left', duration=0.7)
        #daily button
        pa.click(*buttons_h['daily'], duration=d)
        pa.moveTo(*buttons_h['scroll_bar'], duration=d)
        pa.drag(0, 100, button='left', duration=0.7)
        #daily button2
        pa.click(*buttons_h['daily2'], duration=d)
        time.sleep(2)
        #gotit
        pa.click(1685, 640)
        time.sleep(2)
        
        #-------------STOP------------------
        #pa.moveTo(*buttons_b['scroll_bar'], duration=0.5)
        #pa.drag(0, 100, button='left', duration=0.7)
        #pa.click(*buttons_h['claim'])
        #time.sleep(3)
        #pa.click(*buttons_h['claim2'])
        #pa.sleep(2)
        #-------------STOP------------------
    
    def farm():
        for i in range(11000):
            pa.click(*buttons_h['push'])
            time.sleep(random.uniform(0.03,0.1))
        time.sleep(1)
        
    if mode == 'claim':
        claim()
    
    elif mode == 'farm':
        farm()

    else:
        claim()
        farm()
    
    pa.click(*c_gram['exit_quest'])
    time.sleep(1.5)
