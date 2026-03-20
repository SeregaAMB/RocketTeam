import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from flask import Flask
from threading import Thread

# Создаем веб-сервер для "оживлятора"
app = Flask('')

@app.route('/')
def home():
    return "I am alive!"

def run():
    # Render выдает порт автоматически, берем его из переменной окружения
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

# --- ВСТАВЬТЕ ВАШ ТОКЕН НИЖЕ ---
API_TOKEN = '8538494246:AAH3v-kqF2bK5Yd73B_soJAaZmb0EpYph-g'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer("""🇬🇧Welcome in our support chat! Ask your question here
    
    🇷🇺Добро пожаловать в чат поддержки. Задавайте свои вопросы здесь""")

async def main():
    keep_alive()
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
