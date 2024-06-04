from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text= 'Set Reminder')],
    [KeyboardButton(text = 'Deleted')]
])
options = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Banger", url="https://open.spotify.com/track/7mVZeLt9f1IaYIl8lXgC59?si=af5963e36acc4840")],
                                                [InlineKeyboardButton(text="Click", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUXbmV2ZXIgZ29ubmEgZ2l2ZSB5b3UgdXA%3D")]])
date = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Yesterday", callback_data='exact')],
    [InlineKeyboardButton(text="This Morning", url='xxx.html'),InlineKeyboardButton(text="This Evening", url='xxx.html')],
    [InlineKeyboardButton(text="Tomorrow", url='xxx.html')]])

priorities = ['HIGH','MID','LOW']
exact_time = ['13:00','15:00','18:00','20:00']
async def pr():
    keyboard = InlineKeyboardBuilder()
    for i in priorities:
        keyboard.add(InlineKeyboardButton(text=i, url="xx.html"))
    return keyboard.adjust(1).as_markup()

async def time():
    keyboard = InlineKeyboardBuilder()
    for j in exact_time:
        keyboard.add(InlineKeyboardButton(text=j, callback_data=f'j_{j}'))
    return keyboard.adjust(2).as_markup()