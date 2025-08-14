from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from parser import parse
from my_gigachat import send_giga_message

TOKEN = '7274649543:AAGU-Gw8xm3MThLDxnv-o0FTG2HjcXCOZko'
content = parse()


async def start(update: Update, context):
    await update.message.reply_text("Привет! Я бот-помощник компании EOLA.\n"
                                    "Я могу рассказать тебе о наших продуктах.\n"
                                    "Можешь задать любой вопрос, и я отвечу тебе!")


async def echo(update: Update, context):
    # Реакция на любое сообщение кроме команд
    user_message = update.message.text
    answer=send_giga_message(user_message, content)
    await update.message.reply_text(answer)



application = ApplicationBuilder().token(TOKEN).build()

# Регистрация обработчиков сообщений
application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))


print("Запускаю бота...")
application.run_polling()