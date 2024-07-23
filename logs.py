from datetime import datetime as dt



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
        'd': 'DOGS',
        'o': 'OTHER'
    }
    
    with open('logs.log', 'a+', encoding='utf-8') as file:
        file.write(f'{dt.now()} : {type_dict[type]} : {quest_dict[name_quest.lower()]} : {message.lower()} \n')
