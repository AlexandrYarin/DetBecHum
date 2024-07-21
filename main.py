import os
import random
import time
import json
import pyautogui as pa
import sys
from datetime import datetime as dt
from blum_game import blum_game_start
from quests import blum, yescoin, pocket, snapster, hexacore, tabizoo


#------------------------/////----------------------------
#                КОНСТАНТЫ И ПЕРЕМЕННЫЕ
#------------------------/////----------------------------

WORK_PATH = 'C:\\Users\\AYarin.StreetArt\\Desktop\\telegram'

pages = {
    'Blum':'find\\pages\\blum.png', 'PocketFi':'find\\pages\\pocket.png',
    'Hexacore Gaming Universe | AGO':'find\\pages\\hexacore.png',
    'Yescoin':'find\\pages\\yes.png', 'snapster trading bot':'find\\pages\\snapster.png',
    'TabiZoo': 'find\\pages\\tabizoo.png'
        }

with open('jsons\\q_a.json', 'r') as file: q_a = json.load(file)
with open('jsons\\coordinates.json', 'r') as file: coor = json.load(file)

accounts = q_a['accounts'] #словарь всех аккаунтов
quests = q_a['quests']#словарь всех квестов
work_list_account, work_list_quests = [elem for elem in accounts.values()][:-1], [elem for elem in quests.values()]


c_gram = coor['telegram']
c_text = coor['text_file']
c_quests = coor['quests']

buttons_b = c_quests['blum']
buttons_p = c_quests['pocket']
buttons_y = c_quests['yes']
buttons_h = c_quests['hexacore']
buttons_s = c_quests['snap']

REGION_Q = (1550, 50, 40, 700) #область поиска квестов
CONFIDENCE_Q = 0.9 #качество распознания квеста

#------------------------/////----------------------------
#                    ФУНКЦИИ КВЕСТОВ
#------------------------/////----------------------------

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
        time.sleep(2)
        
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
    
    
function_dict = {
    'Hexacore Gaming Universe | AGO': hexacore,
    'PocketFi': pocket,
    'snapster trading bot': snapster,
    'Yescoin': yescoin,
    'Blum': blum,
    'TabiZoo': tabizoo
}



#------------------------/////----------------------------
#                   РАБОЧИЕ ФУНКЦИИ
#------------------------/////----------------------------



def logs(type, name_quest, message):
    type_dict = {
        1: 'CRITICAL',
        2: 'WARNING',
        3: 'USSUALLY',
        4: 'SUCCESSFUL'
    }
    
    quest_dict = {
        'y': 'YESCOIN',
        'p': 'POCKET',
        'b': 'BLUM',
        'h': 'HEXACORE',
        's': 'SNAPSTER',
        't': 'TABIZOO',
        'o': 'OTHER'
    }
    
    with open('logs.log', 'a+') as file:
        file.write(f'{dt.now()} : {type_dict[type]} : {quest_dict[name_quest.lower()]} : {message.lower()} \n')



#проверка правильности названия мода
def mode_check():
    
    mode = input('Какой режим?    ').lower() # MODE: FARM OR CLAIM
    
    while True:
        if mode == 'claim':
            #print('CLAIM MODE ON')
            logs(4, 'o', 'mode accepted')
            return mode
        
        elif mode == 'farm':
            #print('FARM MODE ON')
            logs(4, 'o', 'mode accepted')
            return mode
            
        else:
            mode = input('Напиши верное название мода    ')
            logs(4, 'o', 'mode DECLINE')
            

def function_params():
    
    print('Какие аккаунты нужно пройти? Напиши цифрой через пробел')
    #выводит список аккаунтов
    for k, elem in accounts.items():
        print(f"{k}: {elem}")
    
    #запрашивает номера аккаунтов        
    list_needed_acc = input()
    list_needed_acc_f = [accounts[elem] for elem in list_needed_acc.split(' ')]
    
    
    print('Какие квесты нужно пройти? Напиши цифрой через пробел')
    #выводит список квестов
    for k, elem in quests.items():
        print(f"{k}: {elem}")
    
    #запрашивает номера квестов
    list_needed_quest = input()
    list_needed_quest_f = [quests[elem] for elem in list_needed_quest.split(' ')]
    
    #возвращает два списка с аккаунтами и квестами, которые нужно пройти
    return list_needed_acc_f, list_needed_quest_f


def find_quests(name_quest):
    count = 0
    
    while count <= 0:
        try:
            x,y = pa.locateCenterOnScreen(pages[name_quest], region=REGION_Q, confidence=CONFIDENCE_Q)
            pa.moveTo(x,y, duration=1)
            pa.click()
            time.sleep(2)
            count = 1
            return True
        
        except pa.ImageNotFoundException as e:
        
            count -= 1
            time.sleep(5)
        
            if count <= -10:
                logs(1, name_quest[0], 'Page not found >>>> e')
                return None

def roll_down(mode, list_of_quests):
    
    logs(3, 'o', 'roll_down starting')
        
    for i, quest in enumerate(list_of_quests):
        
        
        #проверяет был ли сделан данный квест
        try:
            list_of_quests.remove(quest)
            logs(3, quest[0], f'was delete from var_list')
            
        except ValueError:
            
            logs(3, 'o', f'{quest} was alredy done')
            print('Этот квест уже сделан')
            continue
        
        
        flag = find_quests(quest)
        
        if flag:
            
            if quest == 'Hexacore Gaming Universe | AGO':
                time.sleep(1.5)
            else:
                pa.click(*c_gram['menu'], duration=1)
                time.sleep(2)
                pa.hotkey('enter')
                time.sleep(2)
                
            
                logs(3, quest[0], 'quest restart')
                
            # Выполенние квеста
            #-------------------------------------
            try:
            
                function_dict[quest](mode)
                logs(4, quest[0], 'quest was done')
        
            except Exception as e:
            
                logs(1, quest[0], f'type error ---> {e}')
                logs(1, quest[0], 'some error during launch quest')
            #-------------------------------------
        
        #возвращается в исходное положение
        pa.click(*c_gram['tap_folder'])
        time.sleep(0.1)
        pa.click(*c_gram['tap_folder'])
        time.sleep(2)

        logs(3, 'o', 'back to main position')
        
    if len(list_of_quests) > 0:
        roll_down(mode, list_of_quests)
    



#Функция по очереди открывает квесты и выполняет их
def main_function(type_pass, mode, work_list_account, work_list_quests):
    
    print(f'Включен {type_pass.upper()} режим. Квесты будут {mode.upper()}-иться')
    
    if type_pass == 'm':
        
        work_list_account, work_list_quests = function_params()
        
        if 'ALL' in work_list_account:
            work_list_account = list(accounts.values())[:-1]
            
        var_list_account, var_list_quests = work_list_account.copy(), work_list_quests.copy()
        
    else:
        var_list_account, var_list_quests = work_list_account.copy(), work_list_quests.copy()

    
    
    
    
    while len(var_list_account) > 0:

        #pre-launch
        sum_acc = len(work_list_account)
        random.shuffle(work_list_account)
        
        for i, account in enumerate(work_list_account):
            
            #make new var_list_quests for accounts that dont launch yet!
            if i > 0:
                var_list_quests = work_list_quests.copy()
            
            random.shuffle(var_list_quests)
            
            
            logs(3, 'o', f'{account} will launch')
            
            

            if account not in var_list_account:
                
                logs(2, 'o', f'{account} was alredy done')
                pa.click(*c_gram['exit_account'], duration=0.5)
                time.sleep(2)
                continue
                
            else:
                
                print(f'Launch {account} account {i+1}/{sum_acc}')
                
                #открывает телеграм аккаунт
                os.startfile(f'{WORK_PATH}\\{account}')
                time.sleep(15)
                pa.click(*c_gram['tap_folder'])
                time.sleep(4)
                logs(4, 'o', f'{account} launching')
                
                #выполняются квесты
                roll_down(mode, var_list_quests)
                logs(3, 'o', f'All quests on {account} account done')
                
                #закрывается телеграм аккаунт
                pa.click(*c_gram['exit_account'])     
                var_list_account.remove(account) 
                logs(3, 'o', f'{account} was close')
                print(f'{account} was done')
                time.sleep(2)
                
    print('Все аккаунты сделаны')
    logs(3, 'o', 'Все аккаунты сделаны')
#------------------------/////----------------------------
#                   РАБТА СКРИПТА
#------------------------/////----------------------------

print('Введи режим работы и способ прохожденияя квестов')

type_pass, mode = input('Вручную(m) или автоматически(a=default)? ').lower(), mode_check()

main_function(type_pass, mode, work_list_account, work_list_quests)