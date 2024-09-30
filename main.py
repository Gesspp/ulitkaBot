from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.utils.media_group import MediaGroupBuilder
from kb import post_keyboard
from callbacks import PostCallback
from states import PostState
import asyncio


bot = Bot('8064482140:AAFGqr48VTiLHjYAanI1wWbJ4sMA7JHhmdU')
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer('This bot is created for making posts', reply_markup=post_keyboard())


@dp.callback_query(PostCallback.filter())
async def callback_inline(
    callback: types.CallbackQuery, 
    callback_data: PostCallback,
    state: FSMContext
):
    if callback_data.action == 'info':
        await callback.message.answer("This bot is for making posts")
    elif callback_data.action == 'make_post':
        await callback.message.answer("Please enter your post text")
        await state.set_state(PostState.process)
        

@dp.message(PostState.process)
async def process_post(message: types.Message):
    if message.photo:
        photos = message.photo
        caption_outer = message.caption if message.caption else ""
        caption_inner = caption_outer + f" @{message.from_user.username}"
        media_group = MediaGroupBuilder(caption=caption_inner)
        for photo in photos: media_group.add_photo(photo.file_id)
        # await bot.send_media_group(-1002441261910, media_group.build())
        media_group.caption = caption_outer
        await bot.send_media_group(-1002461746865, media_group.build())
    else:
        mess = message.text
        # await bot.send_message(-1002441261910, "Post: " + mess + f" @{message.from_user.username}")
        await bot.send_message(-1002461746865, "Post: " + mess)

async def on_startup():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(on_startup())