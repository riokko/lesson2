from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import ephem
from datetime import datetime

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = 'Привет, {}! Ты написал «{}»'.format(update.message.chat.first_name, update.message.text)
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username, 
                update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)

def planet_ephem(bot, update):
    user_planet = update.message.text
    user_planet = user_planet.split(" ")[1].capitalize()
    date = datetime.now()
    today = date.strftime('%Y/%m/%d')
    if user_planet == 'Mars':
        result = ephem.Mars(today)
    if user_planet == 'Venus':
        result = ephem.Venus(today)
    if user_planet == 'Pluto':
        result = ephem.Pluto(today)
    if user_planet == 'Jupiter':
        result = ephem.Jupiter(today)

    constellation = ephem.constellation(result)
    update.message.reply_text(constellation)

def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    
    logging.info('Бот запускается')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", planet_ephem))

    mybot.start_polling()
    mybot.idle()


main()