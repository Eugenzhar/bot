from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from cbrf import get_rates
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# не пойму как приделать cbrf
def main():
    rate = get_rates()


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что нибудь!")


@dp.message_handler(commands=['help'])
async def proces_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отправлю этот текст в ответ тебе в ответ!")


@dp.message_handler(commands=['dollar'])
async def proces_dollar_command(message: types.Message):
    await message.reply("я пока не знаю сколько стоит доллар!")


@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
    if msg.text.lower() == 'курс':
        # здесь бот должен сказать результат cbrf , но не говорит
        await msg.answer('я пока не знаю как определять курсы валют!')


# @dp.message_handler(commands=['курс', 'курсы', 'цена', 'стоймость'])
# async def proces_currency_command(message: types.Message):
#    await message.reply("я пока не знаю как определять курсы валют!")

@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
    if msg.text.lower() == 'привет':
        await msg.answer('Привет!')
    else:
        await msg.answer('Не понимаю, что это значит.')


@dp.message_handler()
# 1 способ ответа
async def echo_message(message: types.Message):
    #    text = f"Ты что написал: {message.text} !"
    #    await bot.send_message(message.chat.id,chat.id, message.text)
    # 2 способ ответа
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
