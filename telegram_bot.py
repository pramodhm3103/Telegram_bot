from telegram.ext import Updater,CommandHandler
from Adafruit_IO import Client, Data
import os
x = os.getenv('x') # ADAFRUIT_IO_USERNAME
y = os.getenv('y') # ADAFRUIT_IO_KEY
z = os.getenv('z')  # TELEGRAM_BOT_TOKEN


def on(bot,update):
    chat_id=update.message.chat_id
    bot.send_photo(chat_id,photo='https://img.icons8.com/plasticine/2x/light-on.png')
    bot.send_message(chat_id,text="Led is on")
    aio = Client(x,y)
    value=Data(value=1)
    value_send=aio.create_data('lightbot',value)


def off(bot,update):
    chat_id=update.message.chat_id
    bot.send_photo(chat_id,photo='https://pngimg.com/uploads/bulb/bulb_PNG1241.png')
    bot.send_message(chat_id,text="Led is off")
    aio = Client(x,y)
    value=Data(value=0)
    value_send=aio.create_data('lightbot',value)

u=Updater(z)
dp=u.dispatcher
dp.add_handler(CommandHandler('turnon',on))
dp.add_handler(CommandHandler('turnoff',off))
u.start_polling()
u.idle()
