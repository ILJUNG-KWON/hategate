import telegram 
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import test
from config2 import TELEGRAM_TOKEN
import fword
import purify

def get_message(update, context):

  print('입력받은 문장: %s'%(update.message.text))
  g_m = test.mespredict(update.message.text)
  print('생성된 문장: %s'%(g_m))
  s_m = fword.slang(update.message.text)
  p_m = purify.purifier(update.message.text)
  


  if len(s_m)>0:
    bot = telegram.Bot(TELEGRAM_TOKEN)
    id = update.message.chat_id
    bot.send_photo(chat_id=id, photo=open("image/robot2.png", 'rb'))
    
  if len(p_m)>0:
    bot = telegram.Bot(TELEGRAM_TOKEN)
    id = update.message.chat_id
    bot.send_photo(chat_id=id, photo=open("image/robot1.png", 'rb'))
  
  update.message.reply_text("{0} {1} \n{2}".format(s_m, g_m, p_m))



    
    
updater = Updater(TELEGRAM_TOKEN, use_context=True)
    

message_handler = MessageHandler(Filters.text, get_message)
updater.dispatcher.add_handler(message_handler)

updater.start_polling(timeout=1, clean=True)
updater.idle()
