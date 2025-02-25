import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from additional import execute_code
import re

# Встановлюємо логування для бота
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Команда старт
async def start(update: Update, context):
    await update.message.reply_text("Привіт! Я бот для виконання коду. Напишіть код, iS я його виконаю.")

# Перевірка, чи є повідомлення кодом
def is_code(text):
    # Перевіряємо, чи є в тексті Python, JavaScript або Ruby код
    python_pattern = re.compile(r'^\s*(def|import|from|print|class)\s')
    javascript_pattern = re.compile(r'^\s*(function|const|let|var|console\.log)\s')
    ruby_pattern = re.compile(r'^\s*(def|puts|class)\s')

    return bool(python_pattern.match(text)) or bool(javascript_pattern.match(text)) or bool(ruby_pattern.match(text))

# Обробник повідомлень
async def handle_message(update: Update, context):
    message_text = update.message.text
    if is_code(message_text):
        # Якщо повідомлення є кодом, виконуємо його
        result = await execute_code(message_text)
        await update.message.reply_text(f"Результат:\n{result}")
    else:
        # Якщо це не код, просто відповідаємо як звичайний бот
        await update.message.reply_text(f"Ви сказали: {message_text}")

# Основна функція
def main():
    # Токен вашого бота
    application = Application.builder().token('YOUR_BOT_TOKEN').build()

    # Обробники команд
    application.add_handler(CommandHandler('start', start))

    # Обробник повідомлень
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запускаємо бота
    application.run_polling()

if __name__ == '__main__':
    main()