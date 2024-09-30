from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart


router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Для узкого круга я полезен, а так могу дать твой id'
        )


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(
        text='Я могу помочь токо узкому кругу'
        )


@router.message(Command(commands='getid'))
async def process_get_id_command(message: Message):
    await message.answer(
        text=f'Прошу, твой id: {str(message.chat.id)}'
        )
