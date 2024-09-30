from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from kb import post_keyboard
from callbacks import PostCallback
from states import PostState


bot = Bot('8064482140:AAFGqr48VTiLHjYAanI1wWbJ4sMA7JHhmdU')
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer('This bot is created for making posts', reply_markup=post_keyboard())


@dp.callback_query(PostCallback.filer())
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
    mess = message.text
    bot.send_message(-1002441261910, "Post: " + mess + f" @{message.from_user.username}")
    bot.send_message(-1002461746865, "Post: " + mess)


bot.polling()