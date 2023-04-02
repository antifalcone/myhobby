from aiogram import Bot, Dispatcher,executor,types
from token_auth import token
from script import get_user_info,get_user_subs,get_friends_user,get_user_photo
import json


def telegram_bot(token):
    bot  = Bot(token=token,parse_mode=types.ParseMode.HTML)
    dp = Dispatcher(bot=bot)

    #@dp.message_handler(content_types=["text"])
    async def echo(message: types.Message):
        await message.answer("[ 🔧 ] Бот на разработке, но он обязательно оживёт ")
        await message.answer("🧑‍💻")
        print(f"[+] LOGGING: '{message.text}' от {message.from_user.full_name} ({message.from_user.id})")


    @dp.message_handler(commands=['start'])
    async def send_message(message: types.Message):
        await message.answer("<u>Важная информация</u>: данный бот находится в разработке, поэтому я жду от Вас фидбэк по работе бота в лс @gifgufgaf")
        await message.answer("Вкратце о боте: данный бот берёт данные исключительно из открытых источников (VK, Instagram(пока не добавлено)), поэтому важно, чтобы цели бота были открытыми профилями.")
        print(f"[+] LOGGING: '{message.text}' от {message.from_user.full_name} ({message.from_user.id})")

    @dp.message_handler(commands=['help'])
    async def send_message(message: types.Message):
        await message.answer("<b>Вводи в любом формате (числовой или буквенный)</b> \n\nНе нагружай бота страницами с 500> фото, а то ему станет плохо🥹 ")
        print(f"[+] LOGGING: '{message.text}' от {message.from_user.full_name} ({message.from_user.id})")

    @dp.message_handler(content_types=["text"])

    async def echo(message: types.Message):
        try:
            print(f"[+] LOGGING: '{message.text}' от {message.from_user.full_name} ({message.from_user.id})")
            user_id = message.text
            await message.answer(f"Информация, найденная по айди: {message.text}")
            get_user_info(user_id)
            with open("account_info.json", "r") as read_file:
                data = json.load(read_file)
                first_name = data["first_name"]
                second_name = data["second_name"]
                birth_date = data["birth_date"]
                interests = data["interests"]
                home_town = data["home_town"]
                city = data["city"]
                mobile_phone = data["mobile_phone"]
            read_file.close()
                
            await message.answer(f"Вот что удалось найти: \n \t 📋 Имя Фамилия: {first_name} {second_name} \n \t 🎉 День рождения: {birth_date} \n \t 😍 Интересы: {interests} \n \t 🏠 Родной город: {home_town} \n \t 🏙 Город: {city} \n \t 📱 Мобильный телефон: {mobile_phone} \n Подробная информация файлами ниже.")
            await message.answer_document(open('account_info.json', 'rb'))
            get_user_subs(user_id)
            await message.answer_document(open('account_subs.json', 'rb'))
            get_friends_user(user_id)
            await message.answer_document(open('account_friends.json', 'rb'))
            await message.answer(f"Раздел с фотографиями на доработке")
            #get_user_photo(user_id)
            #await message.answer_document(open('account_photos.zip', 'rb'))
            #await message.answer_video(open('success.mp4','rb'))
        except:
            await message.answer("Чёт пошло не так, но это обязательно пофиксится, надо просто подождать, правда ведь? ")
            await message.answer("🥺")
            print(f"[!] WARNING: '{message.text}' от {message.from_user.full_name} ({message.from_user.id})")
    executor.start_polling(dispatcher = dp)
if __name__ == "__main__":
    telegram_bot(token)
