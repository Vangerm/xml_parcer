from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsAdmin(BaseFilter):
    async def __call__(self, message: Message, admin_ids: list) -> bool:
        return message.from_user.id in admin_ids
