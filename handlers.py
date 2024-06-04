from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import Router,F
import kb
router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Hello my friend", reply_markup=kb.main)


@router.message(Command('help'))
async def help_cmd(message: Message):
    await message.answer("I cannot help you bruh")

@router.message(F.text =='What up')
async def f_reply(message:Message):
    await message.reply("Nothing much G")