from django.core.management import BaseCommand
from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

from ..start import *
from ..inline import *
from ..order import *
from ..replay import *

TOKEN = "2019705982:AAGo1WyKgNQrCQAcNHuxc66ho6u9L0jU6d4"


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        updater = Updater(TOKEN)
        updater.dispatcher.add_handler(CommandHandler('start', start))
        updater.dispatcher.add_handler(MessageHandler(Filters.reply, reply))
        updater.dispatcher.add_handler(MessageHandler(Filters.all, order))
        updater.dispatcher.add_handler(CallbackQueryHandler(inline))
        updater.start_polling()
        updater.idle()







