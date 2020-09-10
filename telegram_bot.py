from telegram.ext import Updater,CommandHandler,MessageHandler, Filters
from Adafruit_IO import Client, Data
import os
x = os.getenv('x') # ADAFRUIT_IO_USERNAME
y = os.getenv('y') # ADAFRUIT_IO_KEY
z = os.getenv('z')  # TELEGRAM_BOT_TOKEN
aio = Client(x,y)

def start(bot,update):
    chat_id=update.message.chat_id
    bot.send_message(chat_id,text='''This bot sends data to adafruit for turning on or off the LED...,please type 
    1- (on,/turnon,turn on) to lightup the LED .
    2- (off,/turnoff,turn off) to put down the LED.
                thanks''')

def on(bot,update):
    chat_id=update.message.chat_id
    bot.send_message(chat_id,text="Led is on")
    bot.send_photo(chat_id,photo='https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Green_sphere.svg/1024px-Green_sphere.svg.png')
    value=Data(value=1)
    value_send=aio.create_data('lightbot',value)


def off(bot,update):
    chat_id=update.message.chat_id
    bot.send_message(chat_id,text="Led is off")
    bot.send_photo(chat_id,photo='https://cainlive.com/wp-content/uploads/2018/08/cropped-clip-art-red-dot-clipart-1.png')
    value=Data(value=0)
    value_send=aio.create_data('lightbot',value)

def inmes(bot,update):
    mess_text=update.message.text
    x1='turn on'
    x2='Turn on'
    x3='on'
    x4='On'
    y1='turn off'
    y2='Turn off'
    y3='off'
    y4='Off'
    if mess_text==(x1 or x2 or x3 or x4):
      on(bot,update)

    elif mess_text==(y1 or y2 or y3 or y4):
      off(bot,update)
   


u=Updater(z)
dp=u.dispatcher
dp.add_handler(CommandHandler('start',start))
dp.add_handler(CommandHandler('turnon',on))
dp.add_handler(CommandHandler('turnoff',off))
dp.add_handler(MessageHandler(Filters.text & (~Filters.command),inmes))
u.start_polling()
u.idle()
       
