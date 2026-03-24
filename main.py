import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

# Вставьте сюда ваш токен от @BotFather
TOKEN = "8310202959:AAEz-uJWNy4qNRw_zGAIVxGqbOZLzuN5V9o"

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    # ПРИВЕТСТВЕННОЕ СООБЩЕНИЕ
    await message.answer("""🇬🇧Welcome in our support chat! Ask your question here
    
🇷🇺Добро пожаловать в чат поддержки. Задавайте свои вопросы здесь""")

# Хэндлер на любое текстовое сообщение от пользователя
@dp.message(F.text)
async def handle_all_messages(message: types.Message):
    # ВАШ ТЕКСТ, КОТОРЫЙ БУДЕТ ИДТИ ПОСЛЕ КАЖДОГО СООБЩЕНИЯ
    await message.answer("""🇬🇧Thank you for contacting us. We will answer as soon as possible.

🇷🇺Спасибо за то что вышли с нами на связь. Мы занимаемся вашим вопросом и ответим как можно скорее""")

# Запуск процесса поллинга
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")
