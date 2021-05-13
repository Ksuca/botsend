import datetime,time
from twilio.rest import Client
from dotenv import load_dotenv
import os
import telegram
load_dotenv()


date=datetime.datetime.today().weekday()

def sendmessage(text):
    telegramtoken=os.getenv('TELEGRAMTOKEN')
    chat_id=os.getenv('CHAT_ID')
    bot=telegram.Bot(telegramtoken)
    bot.send_message(chat_id=chat_id,text=text)
'''    acount_sid=os.getenv("acount_sid")
    token=os.getenv("token")
    client=Client(acount_sid,token)
    number_from=os.getenv("number_from")
    number_to=os.getenv("number_to")
    message=client.messages.create(body=text,from_=number_from,to=number_to)
    message.sid'''

    
    
def table(y):
    if y==3:
        timetable=open("Thursday.txt","r", encoding = 'utf8')
        timetable=timetable.read()
        message=f"Сегодня четверг твоё рассписание:{timetable}"
        sendmessage(message)
    elif y==1:
        timetable=open("Tuesday.txt","r", encoding = 'utf8')
        timetable=timetable.read()
        message=f"Сегодня вторник твоё рассписание:{timetable}"
        sendmessage(message)
    elif y==0:
        timetable=open("Monday.txt","r", encoding = 'utf8')
        timetable=timetable.read()
        message=f"Сегодня понедельник твоё рассписание:{timetable}"
        sendmessage(message) 
    elif y==2:
        timetable=open("Wensday.txt","r", encoding = 'utf8')
        timetable=timetable.read()
        message=f"Сегодня среда твоё рассписание:{timetable}"
        sendmessage(message)
    elif y==4:
        timetable=open("Friday.txt","r", encoding = 'utf8')
        timetable=timetable.read()
        message=f"Сегодня пятница твоё рассписание:{timetable}"
        sendmessage(message)

    elif y==5:
        print()
    elif y==6:
        print()
        
def birthday_party(day1,mon):
    date=open('important_dates.txt', 'r', encoding = 'utf8')
    date=date.read().split('\n')
    p=0
    while p<len(date):

        day =int(date [p].split('"')[0].split('.')[0])
        month =int(date[p].split('"')[0].split('.')[1])
        if day==day1 and month==mon:
            text=date[p].split('"')
            text = (' '.join(str(e)) for e in text)
def main():
   
    run=True
    while run:
        now=datetime.datetime.now()
        subjeckt=now.replace(hour=15,minute=00)
        call=now.replace(hour=9,minute=30) 

        today=now.replace(hour=17,minute=00)
        if now==today:
            table(date)
            time.sleep(60)
        elif now==subjeckt:
            sendmessage("ПОРА ДЕЛАТЬ УРОКИ!!")
            time.sleep(60)
        elif now==call:
            sendmessage("ПОЗВОНИ МАМЕ ИЛИ ПАШЕ!")
            time.sleep(60)
       

main ()
