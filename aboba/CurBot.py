import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup
import datetime

TOKEN = '5253153120:AAFxBhTYmqQlCIAWIUUZ4ihro0faaP6qHaU'
print("Bot is bot")
uupdater = Updater(TOKEN)


def nowerday():
    """
    returns today date
    """
    nowday = ''
    now = str(datetime.date.today())
    now = now.split('-')
    for i in now:
        nowday += i
    return nowday

def start(update, context):
    chat = update.effective_chat
    buttons = [[KeyboardButton('AUD')], [KeyboardButton('AZN')], [KeyboardButton('EUR')], [KeyboardButton('DZD')],
               [KeyboardButton('USD')], [KeyboardButton('GBP')], [KeyboardButton('CNY')], [KeyboardButton('KRW')],
               [KeyboardButton('AMD')], [KeyboardButton('JPY')]]
    context.bot.send_message(chat_id=chat.id, text='Hello! I am your currency bot',
                             reply_markup=ReplyKeyboardMarkup(buttons))


def terminal_cur(name_of_cur):
    if name_of_cur in ['AUD', 'AZN', 'EUR', 'DZD', 'USD', 'GBP', 'CNY', 'KRW', 'AMD', 'JPY']:
        new_course = requests.get(f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode='
                                  f'{name_of_cur}&date={nowerday()}&json').json()
        result = f'1 {name_of_cur} {new_course[0]["rate"]} is UAH '
        return result


def cur(update, context):

    chat = update.effective_chat
    text = update.message.text
    if text in ['AUD', 'AZN', 'EUR', 'DZD', 'USD', 'GBP', 'CNY', 'KRW', 'AMD', 'JPY']:
        new_course = requests.get(f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode='
                                  f'{text}&date={nowerday()}&json').json()
        g = f'1 {text} {new_course[0]["rate"]} is UAH '
        context.bot.send_message(chat_id=chat.id, text=g)


disp = uupdater.dispatcher
disp.add_handler(CommandHandler('start', start))
disp.add_handler(MessageHandler(Filters.all, cur))
uupdater.start_polling()
uupdater.idle()
