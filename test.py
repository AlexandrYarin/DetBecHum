import os
WORK_PATH = 'C:\\Users\\AYarin.StreetArt\\Desktop\\telegram\\telegram_account'


for elem in os.listdir(WORK_PATH):
    print(elem.replace('.lnk', ''))