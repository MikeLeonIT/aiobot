import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

API_TOKEN = '6392530153:AAFLBiS0l06BQdxyVNJ9sGSlkFPDjaImxWY'  # token бота телега
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply('Привет! Вложенные функции:\n'
                        '/document')


@dp.message_handler(commands="document")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["...Да...", "...Нет..."]
    keyboard.add(*buttons)
    await message.answer("Загрузить файл?", reply_markup=keyboard)
    @dp.message_handler(Text(equals="...Да..."))
    async def with_puree(message: types.Message):
        await message.reply("Отличный выбор!")
        async def save_file()

    @dp.message_handler(lambda message: message.text == "...Нет...")
    async def without_puree(message: types.Message):
        await message.reply("Ну и ладно!")

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
