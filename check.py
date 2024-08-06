import pandas as pd
from getpass import getpass
import json
from update import check_answer


USER = getuser()
TEMP_PATH = f'C:\\Users\\{USER}\\Desktop\\script\\auto\\temp'
WORK_PATH = f'C:\\Users\\{USER}\\Desktop\\accounts'

with open(f'{TEMP_PATH}\\jsons\\stat.json', 'r') as file: stat = json.load(file)

mask = {
    'hexacore': ['Cs', 'Fs'],
    'pocketfi': ['Cs', 'Cs'],
    'snapster': ['Cs'],
    'yescoin': ['Cs', 'Fs', 'Cs'],
    'blum': ['Cs', 'Fs', 'Cs'],
    'tabizoo': ['Cs', 'Fs'],
    'dogs': ['Cs'],
    'clayton': ['Cs', 'Cs'],
    'nasduck': ['Cs', 'Cs'],
    'lost_dogs': ['Cs']
}


while True:
    print('            |             ')
    print('           / \            ')
    print('          /   \           ')
    print('         /     \          ')
    print('        |       |         ')
    print('        V       V         ')
    print('1: ACCONTS      2: QUESTS')
    answer = int(input('>>> '))
    if answer == 1:
        pass
    
    elif answer == 2:
        pass
    else:
        print('check your answer (1 or 2)')
        
        
