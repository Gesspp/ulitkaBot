from aiogram.utils.keyboard import InlineKeyboardBuilder
from callbacks import PostCallback


def post_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="Want to make a post?", callback_data=PostCallback(action="make_post"))
    builder.button(text="Information", callback_data=PostCallback(action="info"))
    builder.adjust(2)
    return builder.as_markup()