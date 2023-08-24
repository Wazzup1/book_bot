from aiogram import Router
from aiogram.types import Message

router: Router = Router()


@router.message()
async def send_echo(message: Message):
    await message.answer(f'Не понимаю Вас. Воспользуйтесь командой /help , чтобы узнать, что я умею.')