from colorama import init
from colorama import Fore, Back, Style
init()
print(Back.BLACK)
print(Fore.CYAN)
print("Script by Zevi/Скрипт сделан Zevi")
print("┌────────────────────────────────────┐")
print("│Author :  LilZevi                   │")
print("│Github : https://github.com/LilZevi │")
print("└────────────────────────────────────┘")
print("YouTube: https://www.youtube.com/channel/UCJ61JlXJckmO6yJr8BDRuGQ")
print("▄▀▄ █▄░▄█ ▀ █▄░█ ▄▀▄ ▄▀▀ █▀▄ ▄▀▄ █▄░▄█ █▀▄ ▄▀▄")
print("█▀█ █░█░█ █ █░▀█ █░█ ░▀▄ █░█ █▀█ █░█░█ █▀█ █░█")
print("▀░▀ ▀░░░▀ ▀ ▀░░▀ ░▀░ ▀▀░ █▀░ ▀░▀ ▀░░░▀ ▀▀░ ░▀░")
print("▐▌░▐▌ █▀▀ █▀▀▄ ▄▀▀ ▀ ▄▀▄ █▄░█ ▒▄▀▄")
print("░▀▄▀░ █▀▀ █▐█▀ ░▀▄ █ █░█ █░▀█ ░▒▄▀")
print("░░▀░░ ▀▀▀ ▀░▀▀ ▀▀░ ▀ ░▀░ ▀░░▀ ▒█▄▄")
communities = {}
import amino
client = amino.Client()
email=str(input("Email/Почта:"))
password=str(input("Password/Пароль:"))
from threading import Thread
r = 0
msgSpam = str(input("Message/Сообщение:"))
print('MessageTypes/Типы сообщений:Default-0,Transparent-110/100/115')
msgType = int(input("MessageType/Тип сообщения:"))
def spam(sub_client, chatId, msgSpam, msgType):
    
    while True:
        try: sub_client.send_message(message=msgSpam, chatId=chatid, messageType=msgType)
        except: pass
        
client = amino.Client()
client.login(email=email, password=password)
clients = client.sub_clients(size=100)
x = 0
for name, id in zip(clients.name, clients.comId):
    print(f"{x + 1}.{name}")
    communities[x] = str(id)
    x+=1

communityid = communities[int(input("Выберите сообщество/Select the community: "))-1]
sub_client = amino.SubClient(comId=communityid, profile=client.profile)

chatInfo = sub_client.get_chat_threads(size=1000)
for title, chatId in zip(chatInfo.title, chatInfo.chatId):
	print(f"{title}: {chatId}")

chatid=input("Type chatid/Введите чат айди:")

print("\nLogged in/Бот зашел!")
print("Print Zevi in selected chat/Введите Zevi в нужном чате!")

@client.callbacks.event("on_text_message")


def on_text_message(data):
    
	content = data.message.content
	chatId = ('chatid'), ('chatid')
	msgId = data.message.messageId
	comId = data.json["ndcId"]
	
	if content.startswith("Zevi"):
		global r
		
		sub_client = amino.SubClient(comId=str(comId), profile=client.profile)
		
		while r < 10000:
                    
			r = r + 1

			
			Thread(target=spam, args=(sub_client, chatId, msgSpam, msgType)).start()
			
			print(f"{str(r)}/sec")
