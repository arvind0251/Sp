# main.py
from telegram.ext import Updater
from start_handler import start_command
from button_handler import button_handler
from recharge_handler import utr_handler
from promo_handler import promo_code_handler
from admin_handler import admin_text
from data_handler import load_data
from constants import BOT_TOKEN
from telegram.ext import CommandHandler, CallbackQueryHandler, MessageHandler, Filters


def main():
    load_data()
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command, pass_args=True))
    dp.add_handler(CallbackQueryHandler(button_handler))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, promo_code_handler))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, utr_handler))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, admin_text))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
