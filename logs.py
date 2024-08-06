from datetime import datetime as dt
from getpass import getuser

USER = getuser()
TEMP_PATH = f'C:\\Users\\{USER}\\Desktop\\script\\auto\\temp'


def logs(type, name_quest, message):
    type_dict = {
        1: 'CRITICAL',
        2: 'WARNING',
        3: 'USSUALLY',
        4: 'SUCCESSFUL'
    }
    
    quest_dict = {
        'yes': 'YESCOIN',
        'poc': 'POCKET',
        'blu': 'BLUM',
        'hex': 'HEXACORE',
        'sna': 'SNAPSTER',
        'tab': 'TABIZOO',
        'dog': 'DOGS',
        'oth': 'OTHER',
        'los': 'LOST_DOGS',
        'yum': 'YUMIFY',
        'cla': 'CLAYTON',
        'nas': 'NASDUCK'
    }
    
    with open(f'{TEMP_PATH}\\logs.log', 'a+', encoding='utf-8') as file:
        file.write(f'{dt.now()} : {type_dict[type]} : {quest_dict[name_quest.lower()]} : {message.lower()} \n')
