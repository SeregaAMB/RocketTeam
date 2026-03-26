import os
import asyncio
import logging
from aiohttp import web
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

# 1. Исправлено: добавлены логи в начало для отладки
logging.basicConfig(level=logging.INFO)

TOKEN = "8310202959:AAEz-uJWNy4qNRw_zGAIVxGqbOZLzuN5V9o"

# 2. ОШИБКА БЫЛА ТУТ: Нужно добавить скобки (), чтобы создать экземпляр класса
bot = Bot(token=TOKEN)
dp = Dispatcher() # Было dp = Dispatcher

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("""🇬🇧Welcome in our support chat! Ask your question here
    
🇷🇺Добро пожаловать в чат поддержки. Задавайте свои вопросы здесь""")

# Хэндлер на любое текстовое сообщение от пользователя
@dp.message(F.text)
async def handle_all_messages(message: types.Message):
    await message.answer("""🇬🇧Thank you for contacting us. We will answer as soon as possible.

🇷🇺Спасибо за то что вышли с нами на связь. Мы занимаемся вашим вопросом и ответим как можно скорее""")

async def handle(request):
    return web.Response(text="Bot is alive!")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    print(f"Web server started on port {port}")

async def main():
    # Запускаем веб-сервер в фоне
    asyncio.create_task(start_web_server())
    # Запускаем бота
    await dp.start_polling(bot)

# 3. ОШИБКА БЫЛА ТУТ: В Python системные переменные пишутся с ДВОЙНЫМ подчеркиванием
if __name__ == "__main__": # Было if name == "main"
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Бот выключен")
