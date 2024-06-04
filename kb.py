from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[
    KeyboardButton(text= 'My Reminders')],
    [KeyboardButton(text = 'Deleted')]
])
options = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Banger", url="https://open.spotify.com/track/7mVZeLt9f1IaYIl8lXgC59?si=af5963e36acc4840")],
                                                [InlineKeyboardButton(text="Click", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=ygUXbmV2ZXIgZ29ubmEgZ2l2ZSB5b3UgdXA%3D")]])