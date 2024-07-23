import os
import random
import time
import json
import pyautogui as pa
from datetime import datetime as dt
from logs import logs
from quests import blum, yescoin, pocket, snapster, hexacore, tabizoo, dogs


#------------------------/////----------------------------
#                КОНСТАНТЫ И ПЕРЕМЕННЫЕ
#------------------------/////----------------------------

WORK_PATH = 'C:\\Users\\ya\\Desktop\\accounts'

pages = {
    'Blum':'find\\pages\\blum.png', 'PocketFi':'find\\pages\\pocket.png',
    'Hexacore Gaming Universe | AGO':'find\\pages\\hexacore.png',
    'Yescoin':'find\\pages\\yes.png', 'snapster trading bot':'find\\pages\\snapster.png',
    'TabiZoo': 'find\\pages\\tabizoo.png', 'Dogs': 'find\\pages\\dogs.png'
        }

with open('jsons\\q_a.json', 'r') as file: q_a = json.load(file)
with open('jsons\\coordinates.json', 'r') as file: coor = json.load(file)

accounts = q_a['accounts'] #словарь всех аккаунтов
quests = q_a['quests']#словарь всех квестов
work_list_account, work_list_quests = [elem for elem in accounts.values()][:-1], [elem for elem in quests.values()]
c_gram = coor['telegram']


REGION_Q = (1550, 50, 40, 700) #область поиска квестов
CONFIDENCE_Q = 0.9 #качество распознания квеста

    
    
function_dict = {
    'Hexacore Gaming Universe | AGO': hexacore,
    'PocketFi': pocket,
    'snapster trading bot': snapster,
    'Yescoin': yescoin,
    'Blum': blum,
    'TabiZoo': tabizoo,
    'Dogs': dogs
}



#------------------------/////----------------------------
#                   РАБОЧИЕ ФУНКЦИИ
#------------------------/////----------------------------



#проверка правильности названия мода
def mode_check():
    
    mode = input('Какой режим?    ').lower() # MODE: FARM OR CLAIM
    
    while True:
        if mode == 'claim':
            logs(4, 'o', 'mode accepted')
            return mode
        
        elif mode == 'farm':
            logs(4, 'o', 'mode accepted')
            return mode
            
        else:
            mode = input('Напиши верное название мода    ')
            logs(4, 'o', 'mode DECLINE')
            

def function_params():
    
    print('Какие аккаунты нужно пройти? Напиши цифрой через пробел или тире')
    #выводит список аккаунтов
    for k, elem in accounts.items():
        print(f"{k}: {elem}")
    
    #запрашивает номера аккаунтов        
    list_needed_acc = input()
    if '-' in list_needed_acc:
        raw_list = [i for i in range(int(list_needed_acc[0]), int(list_needed_acc[2])+1)]
        list_needed_acc_f = [accounts[str(elem)] for elem in raw_list]
    else:        
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
            
            if quest == 'Hexacore Gaming Universe | AGO' or 'TabiZoo' or 'Dogs':
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
