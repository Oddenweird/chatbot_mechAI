import asyncio
import config
import keyboards
from aiogram import Bot, Dispatcher, types , F
from aiogram.filters import Command
# from aiogram.filters import CommandObject
import logging
import random
import requests
from datetime import datetime
# from aiogram.utils import executor
# import aiohttp

logging.basicConfig(level=logging.INFO)

bot = Bot(token= config.ton, parse_mode='HTML')
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f'Приветствую 😊, {message.from_user.full_name}!')
    await asyncio.sleep(1)
    await message.answer('Я тестовый бот по имени Мехаила Прима!)')
    await asyncio.sleep(2)
    await message.answer('Странное имя, но уверяю, оно происходит от двух производных слов английского языка: mechanic (механический) и AI (искусственный интеллект). Прима же на латыне имеет значение "Первая"')
    await asyncio.sleep(2)
    await message.answer('Я могу рассказать о себе чуть-чуть больше или можем пройтись по моим основным функциям 😌', reply_markup=keyboards.keyboard1)

@dp.message(Command("about_me"))
async def cmd_aboutme(message: types.Message):
    await message.reply('Я была разработа в мае 2024 года. Мой создатель, начинающий программист и на меня он тратил свое драгаценное время... Хотя мог бы и отдохнуть, после тяжелого рабочего дня на заводе')
    await asyncio.sleep(3)
    await message.reply('Мой код был написан на языке программирования Python. Основной целью моего создания послужила итоговая аттестация по разработке чат-бота в телеграмме.')
    await asyncio.sleep(2)
    await message.reply('В принципе наверное это все, что я хотела бы написать. Перейдем к моим функциям?)', reply_markup=keyboards.keyboard2)

@dp.message(Command("functions"))
async def cmd_functions(message: types.Message):
    await message.reply('Я могу совсем немного, но все же: 1. Могу рассказать анекдот)')
    await message.reply('2. Могу сказать точное время')
    await message.reply('3. Могу сказать, какая сегодня погода в Москве')
    await message.reply('4. Могу скинуть смешную картинку', reply_markup=keyboards.keyboard3)

jokes = [
    "Почему программисты не ходят по лесу? Потому что они боятся встретить багов.",
    "Сколько программистов нужно, чтобы сменить лампочку? Ни одного, это аппаратная проблема.",
    "Что сказал программист своей жене? Нет времени объяснять, просто будь готова через 10 минут."
]

@dp.message(Command('fun'))
async def fun(message: types.Message):
    await message.reply(random.choice(jokes))

@dp.message(Command('time'))
async def send_time(message: types.Message):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    await message.reply(f"Текущее время: {now}")

@dp.message(Command('weather'))
async def send_weather(message: types.Message):
    city = "Moscow"
    api_key = "YOUR_OPENWEATHER_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        await message.reply(f"Погода в {city}: {weather}, {temp}°C")
    else:
        await message.reply("Не удалось получить данные о погоде.")

# Обработчик команды для отправки изображения
@dp.message(Command('send_photo'))
async def send_photo(message: types.Message):
    # URL изображения
    photo_url = 'https://w.forfun.com/fetch/5d/5d572d697e41c82ac511549420ebcf44.jpeg'
    
    # Отправка фото
    await bot.send_photo(message.chat.id, photo_url, caption="Вот ваше изображение!")


@dp.message(Command("info"))
async def cmd_info(message: types.Message):
    number = random.randint(1, 7)
    await message.answer("Я тестовый бот")
    await message.answer(f"Твоё число {number}")

async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())
    
# Обработчик команды для отправки изображения
# НЕ РАБОТАЕТ. ТРЕБУЕТ ВПН
# @dp.message(Command('send_photo'))
# async def send_photo(message: types.Message):
#     # URL для получения случайного изображения
#     random_image_url = 'https://picsum.photos/200/300'

#     async with aiohttp.ClientSession() as session:
#         async with session.get(random_image_url) as resp:
#             if resp.status == 200:
#                 photo_url = str(resp.url)
#                 await bot.send_photo(message.chat.id, photo_url, caption="Вот ваше случайное изображение!")

# @dp.message(F.text)
# async def msg(message: types.Message):
#     if 'расскажи о  себе' in message.text.lower() :
#         await message.reply('Я была разработа в мае 2024 года. Мой создатель, начинающий программист и на меня он тратил свое драгаценное время... Хотя мог бы и отдохнуть, после тяжелого рабочего дня на заводе')
#         await asyncio.sleep(2)
#         await message.reply('Мой код был написан на языке программирования Python. Основной целью моего создания послужила итоговая аттестация по разработке чат-бота в телеграмме.')
#         await asyncio.sleep(1)
#         await message.reply('В принципе наверное это все, что я хотела бы написать. Перейдем к моим функциям?)', reply_markup=keyboards.keyboard2)
#     elif 'перейдем к функциям' in message.text.lower() :
#         await message.reply('Я могу совсем немного, но все же:','1. Могу рассказать анекдот)','2. Могу сказать точное время','3. Могу сказать, какая сегодня погода в Москве','4. Могу скинуть смешную картинку', end='\n')
#         await asyncio.sleep(2)
#         await message.reply(reply_markup=keyboards.keyboard3)

    # elif 'споки' in message.text.lower() :
    #     await message.reply('Сладких снов! <3')
    # elif 'пока' in message.text.lower() :
    #     await message.reply('Пока-пока! До скорого! <3')
    # else :
    #     await message.reply('Не понимаю')
