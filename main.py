######################################
# Hasil kegabutan yang hakiki        #
# Wuhh istrinya kang rekode;v        #
# Author : By X - MrG3P5             #
# Github : https://github.com/MrG3P5 #
######################################
import os
from gazpacho import Soup

brblue = '\x1b[94m'
white = '\x1b[37m'
green = '\x1b[32m'
red = '\x1b[31m'
yellow = '\x1b[33m'

def banner():
    my_banner = ''' {}____  _  __      ____ _               _             
/ ___|| |/ /     / ___| |__   ___  ___| | _____ _ __ 
\___ \| ' /_____| |   | '_ \ / _ \/ __| |/ / _ \ '__|
 ___) | . \_____| |___| | | |  __/ (__|   <  __/ | {}Created By  
{}|____/|_|\_\     \____|_| |_|\___|\___|_|\_\___|_| {}> X-MrG3P5'''.format(brblue, white, brblue, white)
    print(my_banner)

if __name__=='__main__':
    banner()
    ask_list = input('\n{}[{}?{}] List sk_live or pk_live (ex: list.txt): {}'.format(brblue, white, brblue, white))
    if os.path.exists(ask_list):
        with open (ask_list,'r') as f:
            sk_live = []
            sk_list = [line.strip() for line in f]
            sk_list_length = len(sk_list)
            for i in range(sk_list_length):
                soup = Soup.get('https://ninja-checker.herokuapp.com/skchk.php?lista='+sk_list[i])
                ress = soup.find("span", mode='first').text
                if ress == '[SK LIVE]':
                    sk_live.append(sk_list[i])
                    print('{}[{}LIVE{}] {}'.format(brblue, green, brblue, white) + sk_list[i])
                elif ress == '[TEST MODE]':
                    print('{}[{}TEST{}] {}'.format(brblue, yellow, brblue, white) + sk_list[i])
                else:
                    print('{}[{}DEAD{}] {}'.format(brblue, red, brblue, white) + sk_list[i])
        with open("live.txt", "w") as outfile:
            outfile.write("\n".join(str(item) for item in sk_live))
            print('\nSuccessfully saved to live.txt file with a total of {} Live'.format(len(sk_live)))
    else:
        print('File Not Found!')
        exit()
