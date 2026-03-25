import os
import asyncio
from aiohttp import web
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

# Вставьте сюда ваш токен от @BotFather
TOKEN = "8310202959:AAEz-uJWNy4qNRw_zGAIVxGqbOZLzuN5V9o"

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher



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

async def handle(request):
    return web.Response(text="Bot is alive!")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    # Render автоматически передает порт в переменную окружения PORT
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    print(f"Web server started on port {port}")

# Запуск процесса поллинга
async def main():
    asyncio.create_task(start_web_server())
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")
