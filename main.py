import logging
import requests
from telegram.ext import *
import time
#Updater, CommandHandler, MessageHandler, Filters

time.sleep(5)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)



def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)
    update.message.reply_text('Error somewhere')

def live(update, context):
    update.message.reply_text('Live')

def IP(update, context):
    update.message.reply_text('Getting IP')
    Address = requests.get('https://ifconfig.me/ip')
    print(Address.text)
    update.message.reply_text(Address.text)

def main():
    updater = Updater("<<API KEY>>", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("live", live))
    dp.add_handler(CommandHandler("IP", IP))


    dp.add_error_handler(error)
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
