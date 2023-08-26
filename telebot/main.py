import logging
from aiogram import Bot, Dispatcher, executor, types
import requests


bot = Bot(token='1955432392:AAFIKGS33j1DsT-zsWIAc_fs6ckOX4yjLQY', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

SERVER_URL = 'http://127.0.0.1:8000/'       #url адрес сервера на котором расположена api


@dp.message_handler(content_types=['text'])
async def descripte_address(message: types.Message):
    """
    Данный обработчик принимает от пользователя сообщение с некорректным адресом,
        отправляет его API через
    :param message:
    :return:
    """
    await message.answer(text='Выберите действие', reply_markup=keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
