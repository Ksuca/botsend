import datetime,time
from twilio.rest import Client
from dotenv import load_dotenv
import os
load_dotenv()
'''name=input("как тебя зовут?")
print("привет",name)
print(datetime.datetime.now())
x=5
while x>0:
    print ("привет меня зовут Робот компьютер")
    print(datetime.datetime.now())
    time.sleep(5)
    x -=1'''

date=datetime.datetime.today().weekday()

def sendmessage(text):
    acount_sid=os.getenv("acount_sid")
    token=os.getenv("token")
    client=Client(acount_sid,token)
    number_from=os.getenv("number_from")
    number_to=os.getenv("number_to")
    message=client.messages.create(body=text,from_=number_from,to=number_to)
    message.sid

    
    
def table(y):
    if y==3:
        timetable=open("timetable/Thursday.txt","r", encoding = 'utf8')
        timetable=timetable.read()
        message=f"Сегодня четверг твоё рассписание:{timetable}"
        sendmessage(message)
    elif y==1:
        timetable=open("timetable/Tuesday.txt","r", encoding = 'utf8')
        timetable=timetable.read()
        message=f"Сегодня вторник твоё рассписание:{timetable}"
        sendmessage(message)
    elif y==0:
        timetable=open("timetable/Monday.txt","r", encoding = 'utf8')
        timetable=timetable.read()
        message=f"Сегодня понедельник твоё рассписание:{timetable}"
        sendmessage(message) 
    elif y==2:
        timetable=open("timetable/Wensday.txt","r", encoding = 'utf8')
        timetable=timetable.read()
        message=f"Сегодня среда твоё рассписание:{timetable}"
        sendmessage(message)
    elif y==4:
        timetable=open("timetable/Friday.txt","r", encoding = 'utf8')
        timetable=timetable.read()
        message=f"Сегодня пятница твоё рассписание:{timetable}"
        sendmessage(message)

    elif y==5:
        print()
    elif y==6:
        print()
        

def main():
    run=True
    while run:
        now=datetime.datetime.now()
        today=now.replace(hour=20,minute=00)
        if now==today:
            table(date)
            time.sleep(60)
                
main ()
