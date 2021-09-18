# -*- coding: utf-8 -*-

import hashlib
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle, InlineKeyboardMarkup, InlineKeyboardButton


bot = Bot(token="1936543415:AAE4z01Zxsz6j7EUjwOpxSZLbHmJ6mcw-QU")
dp = Dispatcher(bot)
i = 1
y = 1


@dp.message_handler(commands=["start"])
async def process_start_command(message: types.Message):
    await message.reply("Здоровенькі були, введите ваш текст для перевода")


@dp.message_handler(commands=["site"])
async def process_site_command(message: types.Message):
    site_btn = InlineKeyboardButton("Перейти", url="http://ukraindaldartaibolno.cf/")
    site_kb = InlineKeyboardMarkup().add(site_btn)
    await message.reply("Милости прошу на мой сайт", reply_markup=site_kb)


@dp.message_handler(commands=["about"])
async def process_about_command(message: types.Message):
    await message.reply("Глаголица — первый славянский алфавит. Создан в середине IX века византийскими миссионерами, братьями Кириллом и Мефодием, для перевода богослужебных текстов с греческого языка на старославянский.\nГлаголица использовалась как в качестве непосредственно старославянского алфавита, так и в качестве тайнописи(так её использовали на Руси). Ативно использовалась в церковной жизни в Хорватии. К хорватским глаголическим памятникам относится, в частности, знаменитая Башчанская плита.\nЧто же касается кириллицы, то её разработали ученики Кирилла несколько позже.")


@dp.message_handler(commands=["settings"])
async def process_settings_command(message: types.Message):
    settingi = InlineKeyboardButton("Отображение литер И и І", callback_data="i")
    settingy = InlineKeyboardButton("Отображение литеры Ы", callback_data="y")
    settings = InlineKeyboardMarkup().add(settingi, settingy)
    await message.reply("Что вы хотите изменить?", reply_markup=settings)


@dp.callback_query_handler(lambda c: c.data == "i")
async def process_callback_settingi(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    settingi1 = InlineKeyboardButton("И = Ⰺ, І = Ⰻ", callback_data="i1")
    settingi2 = InlineKeyboardButton("И = Ⰹ, І = Ⰻ", callback_data="i2")
    settingi3 = InlineKeyboardButton("И = Ⰻ, І = Ⰺ", callback_data="i3")
    settingi4 = InlineKeyboardButton("И = Ⰻ, І = Ⰹ", callback_data="i4")
    settingi5 = InlineKeyboardButton("И = Ⰺ, І = Ⰹ", callback_data="i5")
    settingi6 = InlineKeyboardButton("И = Ⰹ, І = Ⰺ",  callback_data="i6")
    settingiback = InlineKeyboardButton("Назад", callback_data="iback")
    settingsi = InlineKeyboardMarkup().add(settingi1, settingi2, settingi3, settingi4, settingi5, settingi6, settingiback)
    await bot.send_message(callback_query.from_user.id, "Отображение литер И и І", reply_markup=settingsi)


@dp.callback_query_handler(lambda c: c.data == "i1")
async def process_callback_settingi1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, "Настройки изменены")
    global i
    i = 1


@dp.callback_query_handler(lambda c: c.data == "i2")
async def process_callback_settingi2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, "Настройки изменены")
    global i
    i = 2


@dp.callback_query_handler(lambda c: c.data == "i3")
async def process_callback_settingi3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, "Настройки изменены")
    global i
    i = 3


@dp.callback_query_handler(lambda c: c.data == "i4")
async def process_callback_settingi4(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, "Настройки изменены")
    global i
    i = 4


@dp.callback_query_handler(lambda c: c.data == "i5")
async def process_callback_settingi5(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, "Настройки изменены")
    global i
    i = 5


@dp.callback_query_handler(lambda c: c.data == "i6")
async def process_callback_settingi6(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, "Настройки изменены")
    global i
    i = 6


@dp.callback_query_handler(lambda c: c.data == "iback")
async def process_callback_settingiback(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    settingi = InlineKeyboardButton("Отображение литер И и І", callback_data="i")
    settingy = InlineKeyboardButton("Отображение литеры Ы", callback_data="y")
    settings = InlineKeyboardMarkup().add(settingi, settingy)
    await bot.send_message(callback_query.from_user.id, "Что вы хотите изменить?", reply_markup=settings)


@dp.callback_query_handler(lambda c: c.data == "y")
async def process_callback_settingy(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    settingy1 = InlineKeyboardButton("Ы = ⰟⰊ", callback_data="y1")
    settingy2 = InlineKeyboardButton("Ы = ⰟⰉ", callback_data="y2")
    settingy3 = InlineKeyboardButton("Ы = ⰟⰋ", callback_data="y3")
    settingyback = InlineKeyboardButton("Назад", callback_data="yback")
    settingsy = InlineKeyboardMarkup().add(settingy1, settingy2, settingy3, settingyback)
    await bot.send_message(callback_query.from_user.id, "Отображение литеры Ы", reply_markup=settingsy)


@dp.callback_query_handler(lambda c: c.data == "y1")
async def process_callback_settingy1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, "Настройки изменены")
    global y
    y = 1


@dp.callback_query_handler(lambda c: c.data == "y2")
async def process_callback_settingy2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, "Настройки изменены")
    global y
    y = 2


@dp.callback_query_handler(lambda c: c.data == "y3")
async def process_callback_settingy3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, "Настройки изменены")
    global y
    y = 3


@dp.callback_query_handler(lambda c: c.data == "yback")
async def process_callback_settingyback(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    settingi = InlineKeyboardButton("Отображение литер И и І", callback_data="i")
    settingy = InlineKeyboardButton("Отображение литеры Ы", callback_data="y")
    settings = InlineKeyboardMarkup().add(settingi, settingy)
    await bot.send_message(callback_query.from_user.id, "Что вы хотите изменить?", reply_markup=settings)


@dp.message_handler()
async def translate(message: types.Message):
    global i
    global y
    str = message.text
    kirilltext = ["А", "а", "Б", "б", "В", "в", "Г", "г", "Д", "д", "Е", "е", "Ж", "ж", "Ѕ", "ѕ", "З", "з", "И", "и", "І", "і", "Ћ", "ћ", "К", "к", "Л", "л", "М", "м", "Н", "н", "О", "о", "П", "п", "Р", "р", "С", "с", "Т", "т", "Ѵ", "ѵ", "У", "у", "Ф", "ф", "Х", "х", "Ѡ", "ѡ", "Ц", "ц", "Ч", "ч", "Ш", "ш", "Щ", "щ", "Ъ", "ъ", "Ы", "ы", "Ь", "ь", "Ѣ", "ѣ", "Ё", "ё", "Ю", "ю", "Ѧ", "ѧ", "Ѩ", "ѩ", "Ѫ", "ѫ", "Ѭ", "ѭ", "Ѳ", "ѳ"]
    glagoltext = ["Ⰰ", "ⰰ", "Ⰱ", "ⰱ", "Ⰲ", "ⰲ", "Ⰳ", "ⰳ", "Ⰴ", "ⰴ", "Ⰵ", "ⰵ", "Ⰶ", "ⰶ", "Ⰷ", "ⰷ", "Ⰸ", "ⰸ", "Ⰺ", "ⰺ", "Ⰹ", "ⰹ", "Ⰻ", "ⰻ", "Ⰼ", "ⰼ", "Ⰽ", "ⰽ", "Ⰾ", "ⰾ", "Ⰿ", "ⰿ", "Ⱀ", "ⱀ", "Ⱁ", "ⱁ", "Ⱂ", "ⱂ", "Ⱃ", "ⱃ", "Ⱄ", "ⱄ", "Ⱅ", "ⱅ", "Ⱛ", "ⱛ", "Ⱆ", "ⱆ", "Ⱇ", "ⱇ", "ⱇ", "Ⱈ", "ⱈ", "Ⱉ", "ⱉ", "Ⱌ", "ⱌ", "Ⱍ", "ⱍ", "Ⱎ", "ⱎ", "Ⱋ", "ⱋ", "Ⱏ", "ⱏ", "Ⱐ", "ⱐ", "Ⱑ", "ⱑ", "Ⱖ", "ⱖ", "Ⱓ", "ⱓ", "Ⱔ", "ⱔ", "Ⱗ", "ⱗ", "Ⱘ", "ⱘ", "Ⱙ", "ⱙ", "Ⱚ", "ⱚ"]

    if any(text in str for text in kirilltext):
        glagol = str.replace("А", "Ⰰ").replace("а", "ⰰ")\
            .replace("Б", "Ⰱ").replace("б", "ⰱ")\
            .replace("В", "Ⰲ").replace("в", "ⰲ")\
            .replace("Г", "Ⰳ").replace("г", "ⰳ")\
            .replace("Д", "Ⰴ").replace("д", "ⰴ")\
            .replace("Е", "Ⰵ").replace("е", "ⰵ")\
            .replace("Ж", "Ⰶ").replace("ж", "ⰶ")\
            .replace("Ѕ", "Ⰷ").replace("ѕ", "ⰷ")\
            .replace("З", "Ⰸ").replace("з", "ⰸ")\
            .replace("Ћ", "Ⰼ").replace("ћ", "ⰼ")\
            .replace("К", "Ⰽ").replace("к", "ⰽ")\
            .replace("Л", "Ⰾ").replace("л", "ⰾ")\
            .replace("М", "Ⰿ").replace("м", "ⰿ")\
            .replace("Н", "Ⱀ").replace("н", "ⱀ")\
            .replace("О", "Ⱁ").replace("о", "ⱁ")\
            .replace("П", "Ⱂ").replace("п", "ⱂ")\
            .replace("Р", "Ⱃ").replace("р", "ⱃ")\
            .replace("С", "Ⱄ").replace("с", "ⱄ")\
            .replace("Т", "Ⱅ").replace("т", "ⱅ")\
            .replace("Ѵ", "Ⱛ").replace("ѵ", "ⱛ")\
            .replace("У", "Ⱆ").replace("у", "ⱆ")\
            .replace("Ф", "Ⱇ").replace("ф", "ⱇ")\
            .replace("Х", "Ⱈ").replace("х", "ⱈ")\
            .replace("Ѡ", "Ⱉ").replace("ѡ", "ⱉ")\
            .replace("Ц", "Ⱌ").replace("ц", "ⱌ")\
            .replace("Ч", "Ⱍ").replace("ч", "ⱍ")\
            .replace("Ш", "Ⱎ").replace("ш", "ⱎ")\
            .replace("Щ", "Ⱋ").replace("щ", "ⱋ")\
            .replace("Ъ", "Ⱏ").replace("ъ", "ⱏ")\
            .replace("Ь", "Ⱐ").replace("ь", "ⱐ")\
            .replace("Ѣ", "Ⱑ").replace("ѣ", "ⱑ")\
            .replace("Ё", "Ⱖ").replace("ё", "ⱖ")\
            .replace("Ю", "Ⱓ").replace("ю", "ⱓ")\
            .replace("Ѧ", "Ⱔ").replace("ѧ", "ⱔ")\
            .replace("Ѩ", "Ⱗ").replace("ѩ", "ⱗ")\
            .replace("Ѫ", "Ⱘ").replace("ѫ", "ⱘ")\
            .replace("Ѭ", "Ⱙ").replace("ѭ", "ⱙ")\
            .replace("Ѳ", "Ⱚ").replace("ѳ", "ⱚ")

        if y == 1:
            glagol = glagol.replace("Ы", "ⰟⰊ").replace("ы", "ⱏⰺ")
        elif y == 2:
            glagol = glagol.replace("Ы", "ⰟⰉ").replace("ы", "ⱏⰹ")
        elif y == 3:
            glagol = glagol.replace("Ы", "ⰟⰋ").replace("ы", "ⱏⰻ")

        if i == 1:
            glagol = glagol.replace("И", "Ⰺ").replace("и", "ⰺ")\
                .replace("І", "Ⰻ").replace("і", "ⰻ")
        elif i == 2:
            glagol = glagol.replace("И", "Ⰹ").replace("и", "ⰹ")\
                .replace("І", "Ⰻ").replace("і", "ⰻ")
        elif i == 3:
            glagol = glagol.replace("И", "Ⰻ").replace("и", "ⰻ")\
                .replace("І", "Ⰺ").replace("і", "ⰺ")
        elif i == 4:
            glagol = glagol.replace("И", "Ⰻ").replace("и", "ⰻ")\
                .replace("І", "Ⰹ").replace("і", "ⰹ")
        elif i == 5:
            glagol = glagol.replace("И", "Ⰺ").replace("и", "ⰺ")\
                .replace("І", "Ⰹ").replace("і", "ⰹ")
        elif i == 6:
            glagol = glagol.replace("И", "Ⰹ").replace("и", "ⰹ")\
                .replace("І", "Ⰺ").replace("і", "ⰺ")

        await message.reply(glagol)
    elif any(text in str for text in glagoltext):
        kirill = str.replace("Ⰰ", "А").replace("ⰰ", "а")\
            .replace("Ⰱ", "Б").replace("ⰱ", "б")\
            .replace("Ⰲ", "В").replace("ⰲ", "в")\
            .replace("Ⰳ", "Г").replace("ⰳ", "г")\
            .replace("Ⰴ", "Д").replace("ⰴ", "д")\
            .replace("Ⰵ", "Е").replace("ⰵ", "е")\
            .replace("Ⰶ", "Ж").replace("ⰶ", "ж")\
            .replace("Ⰷ", "Ѕ").replace("ⰷ", "ѕ")\
            .replace("Ⰸ", "З").replace("ⰸ", "з")\
            .replace("Ⰼ", "Ћ").replace("ⰼ", "ћ")\
            .replace("Ⰽ", "к").replace("ⰽ", "к")\
            .replace("Ⰾ", "Л").replace("ⰾ", "л")\
            .replace("Ⰿ", "М").replace("ⰿ", "м")\
            .replace("Ⱀ", "Н").replace("ⱀ", "н")\
            .replace("Ⱁ", "О").replace("ⱁ", "о")\
            .replace("Ⱂ", "П").replace("ⱂ", "п")\
            .replace("Ⱃ", "Р").replace("ⱃ", "р")\
            .replace("Ⱄ", "С").replace("ⱄ", "с")\
            .replace("Ⱅ", "Т").replace("ⱅ", "т")\
            .replace("Ⱛ", "Ѵ").replace("ⱛ", "ѵ")\
            .replace("Ⱆ", "У").replace("ⱆ", "у")\
            .replace("Ⱇ", "Ф").replace("ⱇ", "ф")\
            .replace("Ⱈ", "Х").replace("ⱈ", "х")\
            .replace("Ⱉ", "Ѡ").replace("ⱉ", "ѡ")\
            .replace("Ⱌ", "Ц").replace("ⱌ", "ц")\
            .replace("Ⱍ", "Ч").replace("ⱍ", "ч")\
            .replace("Ⱎ", "Ш").replace("ⱎ", "ш")\
            .replace("Ⱋ", "Щ").replace("ⱋ", "щ")\
            .replace("Ⱐ", "Ь").replace("ⱐ", "ь")\
            .replace("Ⱑ", "Ѣ").replace("ⱑ", "ѣ")\
            .replace("Ⱖ", "Ё").replace("ⱖ", "ё")\
            .replace("Ⱓ", "Ю").replace("ⱓ", "ю")\
            .replace("Ⱔ", "Ѧ").replace("ⱔ", "ѧ")\
            .replace("Ⱗ", "Ѩ").replace("ⱗ", "ѩ")\
            .replace("Ⱘ", "Ѫ").replace("ⱘ", "ѫ")\
            .replace("Ⱙ", "Ѭ").replace("ⱙ", "ѭ")\
            .replace("Ⱚ", "Ѳ").replace("ⱚ", "ѳ")

        if y == 1:
            kirill = kirill.replace("ⰟⰊ", "Ы").replace("ⱏⰺ", "ы")
        elif y == 2:
            kirill = kirill.replace("ⰟⰉ", "Ы").replace("ⱏⰹ", "ы")
        elif y == 3:
            kirill = kirill.replace("ⰟⰋ", "Ы").replace("ⱏⰻ", "ы")

        if i == 1:
            kirill = kirill.replace("Ⰺ", "И").replace("ⰺ", "и")\
                .replace("Ⰻ", "І").replace("ⰻ", "і")
        elif i == 2:
            kirill = kirill.replace("Ⰹ", "И").replace("ⰹ", "и")\
                .replace("Ⰻ", "І").replace("ⰻ", "і")
        elif i == 3:
            kirill = kirill.replace("Ⰻ", "И").replace("ⰻ", "и")\
                .replace("Ⰺ", "І").replace("ⰺ", "і")
        elif i == 4:
            kirill = kirill.replace("Ⰻ", "И").replace("ⰻ", "и")\
                .replace("Ⰹ", "І").replace("ⰹ", "і")
        elif i == 5:
            kirill = kirill.replace("Ⰺ", "И").replace("ⰺ", "и")\
                .replace("Ⰹ", "І").replace("ⰹ", "і")
        elif i == 6:
            kirill = kirill.replace("Ⰹ", "И").replace("ⰹ", "и")\
                .replace("Ⰺ", "І").replace("ⰺ", "і")

        kirill = kirill.replace("Ⱏ", "Ъ").replace("ⱏ", "ъ")

        await message.reply(kirill)
    else:
        await message.reply("Пожалуйста, введите текст глаголицей или кириллицей")


@dp.inline_handler()
async def inline_translate(inline_query: InlineQuery):
    global i
    global y
    str = inline_query.query
    kirilltext = ["А", "а", "Б", "б", "В", "в", "Г", "г", "Д", "д", "Е", "е", "Ж", "ж", "Ѕ", "ѕ", "З", "з", "И", "и", "І", "і", "Ћ", "ћ", "К", "к", "Л", "л", "М", "м", "Н", "н", "О", "о", "П", "п", "Р", "р", "С", "с", "Т", "т", "Ѵ", "ѵ", "У", "у", "Ф", "ф", "Х", "х", "Ѡ", "ѡ", "Ц", "ц", "Ч", "ч", "Ш", "ш", "Щ", "щ", "Ъ", "ъ", "Ы", "ы", "Ь", "ь", "Ѣ", "ѣ", "Ё", "ё", "Ю", "ю", "Ѧ", "ѧ", "Ѩ", "ѩ", "Ѫ", "ѫ", "Ѭ", "ѭ", "Ѳ", "ѳ"]
    glagoltext = ["Ⰰ", "ⰰ", "Ⰱ", "ⰱ", "Ⰲ", "ⰲ", "Ⰳ", "ⰳ", "Ⰴ", "ⰴ", "Ⰵ", "ⰵ", "Ⰶ", "ⰶ", "Ⰷ", "ⰷ", "Ⰸ", "ⰸ", "Ⰺ", "ⰺ", "Ⰹ", "ⰹ", "Ⰻ", "ⰻ", "Ⰼ", "ⰼ", "Ⰽ", "ⰽ", "Ⰾ", "ⰾ", "Ⰿ", "ⰿ", "Ⱀ", "ⱀ", "Ⱁ", "ⱁ", "Ⱂ", "ⱂ", "Ⱃ", "ⱃ", "Ⱄ", "ⱄ", "Ⱅ", "ⱅ", "Ⱛ", "ⱛ", "Ⱆ", "ⱆ", "Ⱇ", "ⱇ", "ⱇ", "Ⱈ", "ⱈ", "Ⱉ", "ⱉ", "Ⱌ", "ⱌ", "Ⱍ", "ⱍ", "Ⱎ", "ⱎ", "Ⱋ", "ⱋ", "Ⱏ", "ⱏ", "Ⱐ", "ⱐ", "Ⱑ", "ⱑ", "Ⱖ", "ⱖ", "Ⱓ", "ⱓ", "Ⱔ", "ⱔ", "Ⱗ", "ⱗ", "Ⱘ", "ⱘ", "Ⱙ", "ⱙ", "Ⱚ", "ⱚ"]

    if any(text in str for text in kirilltext):
        glagol = str.replace("А", "Ⰰ").replace("а", "ⰰ")\
            .replace("Б", "Ⰱ").replace("б", "ⰱ")\
            .replace("В", "Ⰲ").replace("в", "ⰲ")\
            .replace("Г", "Ⰳ").replace("г", "ⰳ")\
            .replace("Д", "Ⰴ").replace("д", "ⰴ")\
            .replace("Е", "Ⰵ").replace("е", "ⰵ")\
            .replace("Ж", "Ⰶ").replace("ж", "ⰶ")\
            .replace("Ѕ", "Ⰷ").replace("ѕ", "ⰷ")\
            .replace("З", "Ⰸ").replace("з", "ⰸ")\
            .replace("Ћ", "Ⰼ").replace("ћ", "ⰼ")\
            .replace("К", "Ⰽ").replace("к", "ⰽ")\
            .replace("Л", "Ⰾ").replace("л", "ⰾ")\
            .replace("М", "Ⰿ").replace("м", "ⰿ")\
            .replace("Н", "Ⱀ").replace("н", "ⱀ")\
            .replace("О", "Ⱁ").replace("о", "ⱁ")\
            .replace("П", "Ⱂ").replace("п", "ⱂ")\
            .replace("Р", "Ⱃ").replace("р", "ⱃ")\
            .replace("С", "Ⱄ").replace("с", "ⱄ")\
            .replace("Т", "Ⱅ").replace("т", "ⱅ")\
            .replace("Ѵ", "Ⱛ").replace("ѵ", "ⱛ")\
            .replace("У", "Ⱆ").replace("у", "ⱆ")\
            .replace("Ф", "Ⱇ").replace("ф", "ⱇ")\
            .replace("Х", "Ⱈ").replace("х", "ⱈ")\
            .replace("Ѡ", "Ⱉ").replace("ѡ", "ⱉ")\
            .replace("Ц", "Ⱌ").replace("ц", "ⱌ")\
            .replace("Ч", "Ⱍ").replace("ч", "ⱍ")\
            .replace("Ш", "Ⱎ").replace("ш", "ⱎ")\
            .replace("Щ", "Ⱋ").replace("щ", "ⱋ")\
            .replace("Ъ", "Ⱏ").replace("ъ", "ⱏ")\
            .replace("Ь", "Ⱐ").replace("ь", "ⱐ")\
            .replace("Ѣ", "Ⱑ").replace("ѣ", "ⱑ")\
            .replace("Ё", "Ⱖ").replace("ё", "ⱖ")\
            .replace("Ю", "Ⱓ").replace("ю", "ⱓ")\
            .replace("Ѧ", "Ⱔ").replace("ѧ", "ⱔ")\
            .replace("Ѩ", "Ⱗ").replace("ѩ", "ⱗ")\
            .replace("Ѫ", "Ⱘ").replace("ѫ", "ⱘ")\
            .replace("Ѭ", "Ⱙ").replace("ѭ", "ⱙ")\
            .replace("Ѳ", "Ⱚ").replace("ѳ", "ⱚ")

        if y == 1:
            glagol = glagol.replace("Ы", "ⰟⰊ").replace("ы", "ⱏⰺ")
        elif y == 2:
            glagol = glagol.replace("Ы", "ⰟⰉ").replace("ы", "ⱏⰹ")
        elif y == 3:
            glagol = glagol.replace("Ы", "ⰟⰋ").replace("ы", "ⱏⰻ")

        if i == 1:
            glagol = glagol.replace("И", "Ⰺ").replace("и", "ⰺ")\
                .replace("І", "Ⰻ").replace("і", "ⰻ")
        elif i == 2:
            glagol = glagol.replace("И", "Ⰹ").replace("и", "ⰹ")\
                .replace("І", "Ⰻ").replace("і", "ⰻ")
        elif i == 3:
            glagol = glagol.replace("И", "Ⰻ").replace("и", "ⰻ")\
                .replace("І", "Ⰺ").replace("і", "ⰺ")
        elif i == 4:
            glagol = glagol.replace("И", "Ⰻ").replace("и", "ⰻ")\
                .replace("І", "Ⰹ").replace("і", "ⰹ")
        elif i == 5:
            glagol = glagol.replace("И", "Ⰺ").replace("и", "ⰺ")\
                .replace("І", "Ⰹ").replace("і", "ⰹ")
        elif i == 6:
            glagol = glagol.replace("И", "Ⰹ").replace("и", "ⰹ")\
                .replace("І", "Ⰺ").replace("і", "ⰺ")

        input_content = InputTextMessageContent(glagol)
        result_id: str = hashlib.md5(glagol.encode()).hexdigest()
        result = InlineQueryResultArticle(
            id = result_id,
            title = f"Перевод {glagol!r}",
            input_message_content = input_content,
        )
        await bot.answer_inline_query(inline_query.id, results=[result], cache_time=1)
    elif any(text in str for text in glagoltext):
        kirill = str.replace("Ⰰ", "А").replace("ⰰ", "а")\
            .replace("Ⰱ", "Б").replace("ⰱ", "б")\
            .replace("Ⰲ", "В").replace("ⰲ", "в")\
            .replace("Ⰳ", "Г").replace("ⰳ", "г")\
            .replace("Ⰴ", "Д").replace("ⰴ", "д")\
            .replace("Ⰵ", "Е").replace("ⰵ", "е")\
            .replace("Ⰶ", "Ж").replace("ⰶ", "ж")\
            .replace("Ⰷ", "Ѕ").replace("ⰷ", "ѕ")\
            .replace("Ⰸ", "З").replace("ⰸ", "з")\
            .replace("Ⰼ", "Ћ").replace("ⰼ", "ћ")\
            .replace("Ⰽ", "к").replace("ⰽ", "к")\
            .replace("Ⰾ", "Л").replace("ⰾ", "л")\
            .replace("Ⰿ", "М").replace("ⰿ", "м")\
            .replace("Ⱀ", "Н").replace("ⱀ", "н")\
            .replace("Ⱁ", "О").replace("ⱁ", "о")\
            .replace("Ⱂ", "П").replace("ⱂ", "п")\
            .replace("Ⱃ", "Р").replace("ⱃ", "р")\
            .replace("Ⱄ", "С").replace("ⱄ", "с")\
            .replace("Ⱅ", "Т").replace("ⱅ", "т")\
            .replace("Ⱛ", "Ѵ").replace("ⱛ", "ѵ")\
            .replace("Ⱆ", "У").replace("ⱆ", "у")\
            .replace("Ⱇ", "Ф").replace("ⱇ", "ф")\
            .replace("Ⱈ", "Х").replace("ⱈ", "х")\
            .replace("Ⱉ", "Ѡ").replace("ⱉ", "ѡ")\
            .replace("Ⱌ", "Ц").replace("ⱌ", "ц")\
            .replace("Ⱍ", "Ч").replace("ⱍ", "ч")\
            .replace("Ⱎ", "Ш").replace("ⱎ", "ш")\
            .replace("Ⱋ", "Щ").replace("ⱋ", "щ")\
            .replace("Ⱐ", "Ь").replace("ⱐ", "ь")\
            .replace("Ⱑ", "Ѣ").replace("ⱑ", "ѣ")\
            .replace("Ⱖ", "Ё").replace("ⱖ", "ё")\
            .replace("Ⱓ", "Ю").replace("ⱓ", "ю")\
            .replace("Ⱔ", "Ѧ").replace("ⱔ", "ѧ")\
            .replace("Ⱗ", "Ѩ").replace("ⱗ", "ѩ")\
            .replace("Ⱘ", "Ѫ").replace("ⱘ", "ѫ")\
            .replace("Ⱙ", "Ѭ").replace("ⱙ", "ѭ")\
            .replace("Ⱚ", "Ѳ").replace("ⱚ", "ѳ")

        if y == 1:
            kirill = kirill.replace("ⰟⰊ", "Ы").replace("ⱏⰺ", "ы")
        elif y == 2:
            kirill = kirill.replace("ⰟⰉ", "Ы").replace("ⱏⰹ", "ы")
        elif y == 3:
            kirill = kirill.replace("ⰟⰋ", "Ы").replace("ⱏⰻ", "ы")

        if i == 1:
            kirill = kirill.replace("Ⰺ", "И").replace("ⰺ", "и")\
                .replace("Ⰻ", "І").replace("ⰻ", "і")
        elif i == 2:
            kirill = kirill.replace("Ⰹ", "И").replace("ⰹ", "и")\
                .replace("Ⰻ", "І").replace("ⰻ", "і")
        elif i == 3:
            kirill = kirill.replace("Ⰻ", "И").replace("ⰻ", "и")\
                .replace("Ⰺ", "І").replace("ⰺ", "і")
        elif i == 4:
            kirill = kirill.replace("Ⰻ", "И").replace("ⰻ", "и")\
                .replace("Ⰹ", "І").replace("ⰹ", "і")
        elif i == 5:
            kirill = kirill.replace("Ⰺ", "И").replace("ⰺ", "и")\
                .replace("Ⰹ", "І").replace("ⰹ", "і")
        elif i == 6:
            kirill = kirill.replace("Ⰹ", "И").replace("ⰹ", "и")\
                .replace("Ⰺ", "І").replace("ⰺ", "і")

        kirill = kirill.replace("Ⱏ", "Ъ").replace("ⱏ", "ъ")

        input_content = InputTextMessageContent(kirill)
        result_id: str = hashlib.md5(kirill.encode()).hexdigest()
        result = InlineQueryResultArticle(
            id=result_id,
            title=f"Перевод {kirill!r}",
            input_message_content=input_content,
        )
        await bot.answer_inline_query(inline_query.id, results=[result], cache_time=1)
    else:
        settingi1 = InlineKeyboardButton("И = Ⰺ, І = Ⰻ", callback_data="i1")
        settingi2 = InlineKeyboardButton("И = Ⰹ, І = Ⰻ", callback_data="i2")
        settingi3 = InlineKeyboardButton("И = Ⰻ, І = Ⰺ", callback_data="i3")
        settingi4 = InlineKeyboardButton("И = Ⰻ, І = Ⰹ", callback_data="i4")
        settingi5 = InlineKeyboardButton("И = Ⰺ, І = Ⰹ", callback_data="i5")
        settingi6 = InlineKeyboardButton("И = Ⰹ, І = Ⰺ", callback_data="i6")
        settingiback = InlineKeyboardButton("Назад", callback_data="iback")
        settingsi = InlineKeyboardMarkup().add(settingi1, settingi2, settingi3, settingi4, settingi5, settingi6,
                                               settingiback)
        isettings = "Отображение литер И и І"
        input_contenti = InputTextMessageContent(isettings)
        result_idi: str = hashlib.md5(isettings.encode()).hexdigest()
        resulti = InlineQueryResultArticle(
            id=result_idi,
            title=f"{isettings!r}",
            input_message_content=input_contenti,
            reply_markup=settingsi
        )
        settingy1 = InlineKeyboardButton("Ы = ⰟⰊ", callback_data="y1")
        settingy2 = InlineKeyboardButton("Ы = ⰟⰉ", callback_data="y2")
        settingy3 = InlineKeyboardButton("Ы = ⰟⰋ", callback_data="y3")
        settingyback = InlineKeyboardButton("Назад", callback_data="yback")
        settingsy = InlineKeyboardMarkup().add(settingy1, settingy2, settingy3, settingyback)
        ysettings = "Отображение литеры Ы"
        input_contenty = InputTextMessageContent(ysettings)
        result_idy: str = hashlib.md5(ysettings.encode()).hexdigest()
        resulty = InlineQueryResultArticle(
            id=result_idy,
            title=f"{ysettings!r}",
            input_message_content=input_contenty,
            reply_markup=settingsy
        )
        await bot.answer_inline_query(inline_query.id, results=[resulti, resulty], cache_time=1)

if __name__ == "__main__":
    executor.start_polling(dp)
