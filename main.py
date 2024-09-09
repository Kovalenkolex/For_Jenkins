from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import requests

# Функция для получения случайного анекдота   не знаю уже че там за права
def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any?type=single"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['joke']
    else:
        return "Не удалось получить анекдот, попробуйте позже."

# Стартовая функция, которая отправляет приветственное сообщение и кнопку
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Получить анекдот", callback_data='get_joke')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Привет! Нажми на кнопку ниже, чтобы получить анекдот:", reply_markup=reply_markup)

# Обработка нажатия кнопки
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'get_joke':
        joke = get_joke()
        await query.edit_message_text(text=joke)

def main():
    # Вставьте свой токен!!!
    application = Application.builder().token('6727976761:AAGRqR5Bq26UX0QnobDg25Xu8fXnPiTE2Is').build()

    # Обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Обработчик нажатий на кнопку
    application.add_handler(CallbackQueryHandler(button))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()
