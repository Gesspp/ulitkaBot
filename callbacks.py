from aiogram.filters.callback_data import CallbackData


class PostCallback(CallbackData, prefix="post"):
    action: str