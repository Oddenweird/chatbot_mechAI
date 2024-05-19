from aiogram import types

button1 = types.KeyboardButton(text='/about_me')
button2 = types.KeyboardButton(text='/functions')
button3 = types.KeyboardButton(text='/fun')
button4 = types.KeyboardButton(text='/time')
button5 = types.KeyboardButton(text='/weather')
button6 = types.KeyboardButton(text='/send_photo')


keyboards1 = [
    [button1,button2]
]

keyboards2 = [
    [button2]
]

keyboards3 = [
    [button3],
    [button4],
    [button5],
    [button6] 
]

keyboard1 = types.ReplyKeyboardMarkup(keyboard=keyboards1, resize_keyboard=True)
keyboard2 = types.ReplyKeyboardMarkup(keyboard=keyboards2, resize_keyboard=True)
keyboard3 = types.ReplyKeyboardMarkup(keyboard=keyboards3, resize_keyboard=True)
