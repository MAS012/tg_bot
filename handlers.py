from aiogram.filters import CommandStart, Command
from aiogram.types import Message,CallbackQuery
from aiogram import Router,F
import kb
router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Hello my friend", reply_markup=kb.main)


@router.message(Command('help'))
async def help_cmd(message: Message):
    await message.answer("I cannot help you bruh \n Choose options instead", reply_markup=kb.options)

@router.message(F.text =='What up')
async def f_reply(message:Message):
    await message.reply("Nothing much G \n Choose Priority", reply_markup=await kb.pr())

@router.message(F.text =='Set Reminder')
async def r_reply(message:Message):
    await message.reply("Choose Time", reply_markup=kb.date)

@router.callback_query(F.data == "exact")
async def yday(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text("Choose EXACT TIME", reply_markup= await kb.time())
    