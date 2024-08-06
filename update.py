import pyautogui as pa
import json
import time
import random
import os
from shutil import copyfile
from datetime import datetime
from  getpass import getuser

reaction_ls = ['Nice', 'Good', 'Yep', 'Take it', 'We have the point', 'Nice job', 'Done']
USER = getuser()
TEMP_PATH = f'C:\\Users\\{USER}\\Desktop\\script\\auto\\temp'

def check_answer():

    while True:
        
        answer = input('>>> ').lower()
        
        if answer == 'y' or answer == 'n':
            return answer
        else:
            print('Write y or n')
            
            
def find_quests(name_quest):
    
    with open(f'{TEMP_PATH}\\jsons\\coordinates.json', 'r') as file: coor = json.load(file)
    REGION_Q, CONFIDENCE_Q = (1550, 50, 40, 800), 0.9 #область поиска квестов

    try:
            
        x,y = pa.locateCenterOnScreen(f'find\\{name_quest}.png', region=REGION_Q, confidence=CONFIDENCE_Q)
        pa.moveTo(x,y, duration=1)
        pa.click()
        time.sleep(1)
            
    except pa.ImageNotFoundException as e:
        print('Page not found')


def add_logo():
    
    image_path = f'C:\\Users\\{USER}\\Desktop\\script\\DetBecomeHum\\find'

    while True:
        
        print('Add another page? (y/n)')
        ans_page = check_answer()
        
        if ans_page == 'n':
            break
        
        print('R U REDY ?')
        input()
        for i in range(3, 0, -1):
            print(f'{i}...')
            time.sleep(0.8)
        
        print('scaning')
        time.sleep(1)
        
        centr = pa.position()
        x, y = centr[0] - 15, centr[1] - 15
        width, height = 30, 30
        
        print('Done')
        time.sleep(1)
        
        page_region = tuple([x, y, width, height])
        print(page_region)
        
        name = input('Name quest >>> ')
        
        img = pa.screenshot(region=page_region)
        img.save(f'find/{name}.png')
        
        
        print('check search page in ...')
        for i in range(3,0,-1):
            print(f'{i}...')
            time.sleep(0.9)
        
        find_quests(name)
        
        print('Look what we did >>>')
        time.sleep(1)
        os.startfile(f'{image_path}\\{name}.png')
            
        print('Save this picture? (y/n)')
        answer = check_answer()
        if answer == 'y':
            continue
        else:
            os.remove(f'{image_path}\\{name}.png')
            print('File delete')


def update_points():
    
    time = datetime.now()
    time_add = f'{time.time().hour}:{time.time().minute}:{time.time().second}'
    copyfile(f'{TEMP_PATH}\\jsons\\coordinates.json', f'{TEMP_PATH}\\backups\\coordinates{time_add}.json')
    with open(f'{TEMP_PATH}\\jsons\\coordinates.json', 'r') as file: coor = json.load(file)
    
    
    while True:
        
        print('LETS GO? (y/n)')
        ans_lets = check_answer()
        if ans_lets == 'y':
            print('What i need to do?')
            time.sleep(0.2)
            print('1: Update Telegram buttons')
            time.sleep(0.2)
            print('2: Update Quests buttons')
            time.sleep(0.2)
        
            ans = int(input('>>> '))
        
            if ans == 1:
                data = coor['telegram']
            
            elif ans == 2:
                data = coor['quests']
                print('Which quest should update?')
                for elem in data.keys():
                    print(f': {elem}')
                quest = input('>>> ')
                data_two = data[quest]
            
                while True:
                    print('1: Which button should update')
                    print('2: or should I add new ones?')
                
                    ans_update = int(input('>>> '))
                
                    if ans_update == 1:
                        for elem in data_two.keys():
                            print(f': {elem}')
                        button = input('>>> ')
                        print('OK')
                        time.sleep(1)
                        print('R U Ready?')
                        input()
                        time.sleep(1)
                        for i in range(3):
                            print(f'{i+1}...')
                            time.sleep(1.5)
                    
                        print('Scaning new values')
                        new_values = pa.position()
                        time.sleep(1)
                        print('DONE')
                        print(f'Its new values: {new_values}, save it? (y/n)')
                        ans_val = check_answer()
                        if ans_val == 'y':
                            coor['quests'][quest][button] = [new_values[0], new_values[1]]
                            with open(f'{TEMP_PATH}\\jsons\\coordinates.json', 'w') as file: json.dump(coor, file)
                            print('Update another one? (y/n)')
                            ans_val_second = check_answer()
                            if ans_val_second == 'n':
                                print('Understood')
                                time.sleep(1)
                                break
                            else:
                                continue
                        else:
                            break
                    else:
                        print('This script still building...')
                        time.sleep(2)
                        print('exit in ...')
                        for i in range(3,0,-1):
                            print(f'{i}...')
                            time.sleep(0.8)
                        break
        else:
            break

def add_points_quest():
    
    
    with open(f'{TEMP_PATH}\\jsons\\coordinates.json', 'r') as file: coor = json.load(file)
    
    new_quest= {}
    
    while True:
        print('ADD ANOTHER QUEST (y/n)? ')    
        ans_q = check_answer()
        
        if ans_q == 'n':
            
            print('Check result? (y/n) ')
            ans_check = check_answer()
            if ans_check == 'y':
                print('-----------------CHECK-----------------')
                for i in range(3): print()
                print('WE HAVE:')
                time.sleep(0.2)
                for i in range(2):
                    time.sleep(0.2)
                    print()
                    
                for elem in new_quest.keys():
                    print('-------NAME QUEST-------')
                    print(elem)
                    print('-------NAME POINTS-------')
                    for point in new_quest[elem]:
                        print(f'NAME POINT: {point} - COORDINATE: {new_quest[elem][point]}')
                        pa.moveTo(*new_quest[elem][point], duration=0.7)
                        time.sleep(1)
                        input('next?')
                
                print('Save this? (y/n)')
                ans_save = check_answer()
                if ans_save == 'n':
                    print('Then i delete this trash and start again')
                    new_quest= {}
                
                    
            else:
                pass
            
            #WRITE NEW QUEST TO JSON
            print('Saving results')
            #animation
            animation = "|/-\\"
            idx = 0
            while idx <=32:
                print(animation[idx % len(animation)], end="\r")
                idx += 1
                time.sleep(0.05)
            
            try:                
                for name in new_quest.keys(): coor['quests'][name] = new_quest[name]
                
                with open(f'{TEMP_PATH}\\jsons\\coordinates.json', 'w') as file: json.dump(coor, file)
                print('Results have been saved')
                break
            
            except UnboundLocalError:
                print('Not have name of quests')
                break
        
        else:
            print('Name quest')
            name_quest = input('>>> ')
            new_quest[name_quest] = {}
            
            while True:
                print('ADD POINT? (y/n)? ')
                ans_point = check_answer()
        
                if ans_point == 'n':
                    break
                
                else:
                    while True:
                        print('Adding a point in .....')
                        for i in range(3):
                            time.sleep(1)
                            print(f'{i+1}...')
                    
                        time.sleep(1)
                    
                        point = pa.position()
                    
                        print(random.choice(reaction_ls))
                        print(f'Your point: {point}')
                        print('Save this point? (y/n)')
                        time.sleep(1.5)
                        pa.moveTo(*point, duration=0.5)
                        ans_write_point = check_answer()
                        
                        if ans_write_point == 'n':
                            
                            print('Try another one')
                            time.sleep(2)
                        else:
                            
                            name_point = input('Give name of this point >>>> ')
                            #WRITE POINT
                            new_quest[name_quest][name_point] = [point[0], point[1]]
                            print('Point saved')
                            break
                        
                    
                    
            
                

def main():
    
    func_dict = {
        1: add_logo,
        2: add_points_quest, 
        3: update_points
                }
    
    
    answer = 'y'
    while answer == 'y':
        print('What Im doing today?')
        for k, v in func_dict.items():
            print(f'{k} : {v.__name__.replace('_', ' ')}')
            time.sleep(0.3)
        num_func = int(input('>>>> '))
        func_dict[num_func]()
        
        print('Is there anything else? (y/n)')
        answer = check_answer()
        if answer == 'y':
            continue
        else:
            print('BYE =)')
            
if __name__ == '__main__':
    main()