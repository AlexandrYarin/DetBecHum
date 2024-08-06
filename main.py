import os
import random
import time
import json
import pyautogui as pa
from datetime import datetime as dt
from logs import logs
from quests import blum, yescoin, pocket, snapster, hexacore, tabizoo, dogs, clayton, nasduck, yumify, lost_dogs
from getpass import getuser
pa.FAILSAFE = False

#------------------------/////----------------------------
#                КОНСТАНТЫ И ПЕРЕМЕННЫЕ
#------------------------/////----------------------------

USER = getuser()
TEMP_PATH = f'C:\\Users\\{USER}\\Desktop\\script\\auto\\temp'
WORK_PATH = f'C:\\Users\\{USER}\\Desktop\\accounts'


with open(f'{TEMP_PATH}\\jsons\\q_a.json', 'r') as file: q_a = json.load(file)
with open(f'{TEMP_PATH}\\jsons\\coordinates.json', 'r') as file: coor = json.load(file)

#создание словаря аккаунтов
ls = [elem.replace('.lnk', '') for elem in os.listdir(WORK_PATH)]
accounts = {} #словарь всех аккаунтов
ls_ = list(zip([i + 1 for i in range(len(ls))], ls))
for elem in ls_:
    accounts[elem[0]] = elem[1]




quests = q_a['quests']#словарь всех квестов
work_list_account, work_list_quests = [elem for elem in accounts.values()], [elem for elem in quests.values()]
c_gram = coor['telegram']


REGION_Q = (1550, 50, 40, 800) #область поиска квестов
CONFIDENCE_Q = 0.9 #качество распознания квеста

    
    
function_dict = {
    'hexacore': hexacore,
    'pocketfi': pocket,
    'snapster': snapster,
    'yescoin': yescoin,
    'blum': blum,
    'tabizoo': tabizoo,
    'dogs': dogs,
    'clayton': clayton,
    'nasduck': nasduck,
    'yumify': yumify,
    'lost_dogs': lost_dogs
    }



#------------------------/////----------------------------
#                   РАБОЧИЕ ФУНКЦИИ
#------------------------/////----------------------------



#проверка правильности названия мода
def mode_check():
    
    mode = input('Какой режим?    ').lower() # MODE: FARM OR CLAIM
    
    while True:
        if mode == 'claim':
            logs(4, 'oth', 'mode accepted')
            return mode
        
        elif mode == 'farm':
            logs(4, 'oth', 'mode accepted')
            return mode
        
        elif mode == 'claim&farm':
            logs(4, 'oth', 'mode accepted')
            return mode
            
        else:
            mode = input('Напиши верное название мода    ')
            logs(4, 'oth', 'mode DECLINE')


def show_stat(name_account):
    
    mask = {
    'hexacore': ['Cs', 'Fs'],
    'pocketfi': ['Cs', 'Cs'],
    'snapster': ['Cs'],
    'yescoin': ['Cs', 'Fs', 'Cs'],
    'blum': ['Cs', 'Fs', 'Cs'],
    'tabizoo': ['Cs', 'Fs'],
    'dogs': ['Cs'],
    'yumify': ['Cs'],
    'clayton': ['Cs', 'Cs'],
    'nasduck': ['Cs', 'Cs'],
    'lost_dogs': ['Cs']
}
    
    quest_dict = stat_dict[name_account]
    note_done = []
        
    for q, res in quest_dict.items():
        if 'e' in ''.join(res):
            return '!'
        else:
            if len(note_done) > 0:
                return '*'
            else:
                refer = mask[q]
                raw_list = res.copy()
                for elem in refer:
                    try:
                        raw_list.remove(elem)
                    except ValueError:
                        continue
                if len(raw_list) == 0:
                    continue
                else:
                    note_done.append(q)
        
    return '_'            


def function_params():
    
    print('Какие аккаунты нужно пройти?')
    #выводит список аккаунтов
    for k, elem in accounts.items():
        if k < 10:
            print(f" {k}: [ {show_stat(elem)} ] {elem}")
        else:
            print(f"{k}: [ {show_stat(elem)} ] {elem}")
    
    #запрашивает номера аккаунтов        
    list_needed_acc = input()
    if '-' in list_needed_acc:
        s_ = list(map(int, list_needed_acc.split('-')))
        raw_list = [i for i in range(s_[0], s_[1]+1)]
        list_needed_acc_f = [accounts[int(elem)] for elem in raw_list]
    else:        
        list_needed_acc_f = [accounts[int(elem)] for elem in list_needed_acc.split(' ')]
    
    
    print('Какие квесты нужно пройти? Напиши цифрой через пробел')
    #выводит список квестов
    for k, elem in quests.items():
        print(f"{k}: {elem}")
    
    #запрашивает номера квестов
    list_needed_quest = input()
    list_needed_quest_f = [quests[elem] for elem in list_needed_quest.split(' ')]
    
    #возвращает два списка с аккаунтами и квестами, которые нужно пройти
    return list_needed_acc_f, list_needed_quest_f


def find_quests(name_quest, takes=5):
    
    count = 0
    
    while count <= 0:
        try:
            
            x,y = pa.locateCenterOnScreen(f'find\\{name_quest}.png', region=REGION_Q, confidence=CONFIDENCE_Q)
            pa.moveTo(x,y, duration=1)
            pa.click()
            time.sleep(2)
            count = 1
            return True
        
        except pa.ImageNotFoundException as e:
        
            count -= 1
            pa.click(coor['telegram']['tap_folder'], duration=0.5)
            print('page not found')
            time.sleep(5)
        
            if count <= -takes:
                logs(1, name_quest[0:3], f'Page not found >>>> {e}')
                return None


#--------------СТАТИСТИКА-------------------
def create_basic_dict():
    #списки квестов и аккаунтов
    acc_list = [elem.replace('.lnk', '')for elem in os.listdir(WORK_PATH)]

    quest_list = list(q_a['quests'].values())

    #создание нулевого словаря
    basic_dict ={}
    for acc in acc_list:
        for quest in quest_list:
            basic_dict.setdefault(acc, {})

    for key in basic_dict.keys():
        for quest in quest_list:
            basic_dict[key][quest] = []
            
    with open(f'{TEMP_PATH}\\jsons\\stat.json', 'w') as file: json.dump(basic_dict, file)
    


while True:
    
    answer=input('Обнулить статистику?(y/n)')
    if answer == 'y':
        create_basic_dict()
        with open(f'{TEMP_PATH}\\jsons\\stat.json', 'r') as file: stat_dict = json.load(file)
        break
    elif answer == 'n':
        
        with open(f'{TEMP_PATH}\\jsons\\stat.json', 'r') as file: stat_dict = json.load(file)
        break
    else:
        print('write correct argument ---> y or n')
#--------------------------------------------    


def roll_down(mode, list_of_quests, account):
    
    logs(3, 'oth', 'roll_down starting')
        
    for i, quest in enumerate(list_of_quests):
        
        
        #проверяет был ли сделан данный квест
        try:
            list_of_quests.remove(quest)
            logs(3, quest[0:3], f'was delete from var_list')
            
        except ValueError:
            
            logs(3, 'oth', f'{quest} was alredy done')
            print('Этот квест уже сделан')
            continue
        
        
        flag = find_quests(quest)
        
        if flag:
            
            #
            #if quest in [
            #    'Hexacore', 'TabiZoo', 'Dogs',
            #    'lost_dogs', 'clayton', 'yumify', 'nasduck']:
            #    time.sleep(1.5)
            #else:
            #    pa.click(*c_gram['menu'], duration=1)
            #    time.sleep(2)
            #    pa.hotkey('enter')
            #    time.sleep(2)
                
            #    logs(3, quest[0:3], 'quest restart')
                
            # Выполенние квеста
            #-------------------------------------
            print(f'{quest}: {mode}')
            try:
            
                function_dict[quest](mode)
                pa.click(*c_gram['tap_folder'])
                time.sleep(1.5)
                cur_status = stat_dict[account][quest]
                cur_status.append(f'{mode[0].upper() + 's'}')
                stat_dict[account][quest] = cur_status
                logs(4, quest[0:3], 'quest was done')
                
        
            except Exception as e:
            
                logs(1, quest[0:3], f'Error is >>>> {e}')
                cur_status = stat_dict[account][quest]
                cur_status.append(f'{mode[0].upper() + 'e'}')
                stat_dict[account][quest] = cur_status
                logs(1, quest[0:3], f'some error during launch quest')
        else:
            print('quest was not found')
            cur_status = stat_dict[account][quest]
            cur_status.append(f'{mode[0].upper() + 'e'}')
            stat_dict[account][quest] = cur_status
            #stat_dict[account][quest] = stat_dict[account][quest].append(f'{mode[0].upper() + 'e'}')
            logs(2, 'oth', f'{quest} was not found')
            #-------------------------------------
        
        #возвращается в исходное положение
        pa.click(*c_gram['tap_folder'])
        time.sleep(0.1)
        pa.click(*c_gram['tap_folder'])
        time.sleep(2)

        logs(3, 'oth', 'back to main position')
        
    if len(list_of_quests) > 0:
        roll_down(mode, list_of_quests, account)
    



#Функция по очереди открывает квесты и выполняет их
def main_function(mode, work_list_account, work_list_quests):
    
    print(f'Квесты будут {mode.upper()}-иться')
    
    work_list_account, work_list_quests = function_params()
        
    if 'ALL' in work_list_account:
        work_list_account = list(accounts.values())[:-1]
            
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
            
            
            logs(3, 'oth', f'{account} will launch')
            
            

            if account not in var_list_account:
                
                logs(2, 'oth', f'{account} was alredy done')
                pa.click(*c_gram['exit_account'], duration=0.5)
                time.sleep(2)
                continue
                
            else:
                
                print(f'Launch {account} account {i+1}/{sum_acc}')
                
                #открывает телеграм аккаунт
                os.startfile(f'{WORK_PATH}\\{account}')
                time.sleep(13)
                pa.click(*c_gram['tap_folder'])
                time.sleep(4)
                logs(4, 'oth', f'{account} launching')
                
                #выполняются квесты
                roll_down(mode, var_list_quests, account)
                logs(3, 'oth', f'All quests on {account} account done')
                
                #закрывается телеграм аккаунт
                pa.click(*c_gram['exit_account'])     
                var_list_account.remove(account) 
                logs(3, 'oth', f'{account} was close')
                print(f'{account} was done')
                time.sleep(2)
                
    print('Все аккаунты сделаны')
    logs(3, 'oth', 'Все аккаунты сделаны')
#------------------------/////----------------------------
#                   РАБТА СКРИПТА
#------------------------/////----------------------------

print('Введи режим работы и способ прохожденияя квестов')

mode = mode_check()

try:
    main_function(mode, work_list_account, work_list_quests)
except Exception as e:
    print(e)
    print('Error')
finally:
    
    while True:
        
        answer2 = input('Сохранить в статистику пройденные квесты (y/n) ?')
        if answer2 == 'y':
            with open(f'{TEMP_PATH}\\jsons\\stat.json', 'w') as file: json.dump(stat_dict, file)
            break
        elif answer2 == 'n':
            break
        else:
            print('Write coorect argument ---> y or n')
