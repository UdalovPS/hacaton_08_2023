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
        отправляет его в API и в ответ получает JSON массив с корректным набором данных
    """
    data = {'textInput': message.text}
    if len(data['textInput']) <= 3:
        await message.answer(text="Слишком короткий адрес")
    else:
        responce = requests.post(url=SERVER_URL + "one-string/", data=data)
        n = 1
        res_str = ''
        for item in responce.json():
            res_str += f"{n}){item['address']} -> <b>{item['value']}</b>\n"
            n += 1
        await message.answer(text=res_str)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
