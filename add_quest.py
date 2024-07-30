import pyautogui as pa
import json
import time
import random


reaction_ls = ['Nice', 'Good', 'Yep', 'Take it', 'We have the point', 'Nice job', 'Done']

def check_answer():

    while True:
        
        answer = input('>>> ').lower()
        
        if answer == 'y' or answer == 'n':
            return answer
        else:
            print('Write y or n')
            



def add_logo():
    pass


def update_points():
    pass    


def add_points_quest():
    
    
    with open('jsons/coordinates.json', 'r') as file: coor = json.load(file)
    
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
                
                with open('jsons/coordinates.json', 'w') as file: json.dump(coor, file)
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