from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text= 'Set Reminder')],
    [KeyboardButton(text = 'Deleted')]
])
options = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Banger", url="https://open.spotify.com/track/7mVZeLt9f1IaYIl8lXgC59?si=af5963e36acc4840")],
                                                [InlineKeyboardButton(text="Click", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUXbmV2ZXIgZ29ubmEgZ2l2ZSB5b3UgdXA%3D")]])
date = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Yesterday", url='xxx.html')],
    [InlineKeyboardButton(text="This Morning", url='xxx.html'),InlineKeyboardButton(text="This Evening", url='xxx.html')],
    [InlineKeyboardButton(text="Tomorrow", url='xxx.html')]])

priorities = ['HIGH','MID','LOW']

async def pr():
    keyboard = InlineKeyboardBuilder()
    for i in priorities:
        keyboard.add(InlineKeyboardButton(text=i, url="xx.html"))
    return keyboard.adjust(1).as_markup()