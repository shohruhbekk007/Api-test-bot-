import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from config import token, admins
from aiogram.fsm.context import FSMContext
from base import  ReadVoice, DeleteVoices, AddInsert
from states import QoshishState


dp = Dispatcher()
logging.basicConfig(level=logging.INFO, stream=sys.stdout)

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Assalomu alaykum qiziqli voice botga xush kelibsiz\n{message.from_user.first_name}")

@dp.message(F.text=='post', F.from_user.id.in_(admins))
async def QoshishBot(message: Message, state: FSMContext):
    xabar = message.text
    await message.answer("Voice nomini yuboring ?")
    await state.set_state(QoshishState.name)


@dp.message(F.text, QoshishState.name)
async def SaqlashBot(message: Message, state: FSMContext):
    xabar = message.text
    await state.update({'name': xabar})
    await message.answer("endi yuboradigan voiceni yuboring? ")
    await state.set_state(QoshishState.url)

@dp.message(QoshishState.url)
async def YuborishVoiceBot(message: Message, state: FSMContext):
    xabar = message
    print(xabar)
    await message.answer("saqlashga rozimisiz !!!")




# @dp.message()
# async def echo_handler(message: Message) -> None:
#     """
#     Handler will forward receive a message back to the sender
#
#     By default, message handler will handle all message types (like a text, photo, sticker etc.)
#     """
#     try:
#         # Send a copy of the received message
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         # But not all the types is supported to be copied so need to handle it
#         await message.answer("Nice try!")


async def main() -> None:
    bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await  bot.send_message(chat_id=admins[0], text="bot ishga tushdi")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        print("tugadi")