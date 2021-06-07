# Leo Projects <https://t.me/leosupportx>
# @naviya2 🇱🇰

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from JESongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from JESongBot import Jebot as app
from JESongBot import LOGGER

pm_start_text = """
Hello [{}](tg://user?id={}), I'm Leo Song Downloader Bot 🇱🇰

You can download any song within a shortime with this Bot 🙂

If you want to know how to use this bot just
touch on this command " /help " 🙂

Leo Projects 🇱🇰
"""

help_text = """
You should know the following commands to use this bot 🙂

- /song <song name>: Download songs from Youtube 🙂
- /saavn <song name>: Download songs from JioSaavn 🙂
- /deezer <song name>: Download songs from Deezer 🙂
- Send youtube url to me directly i can download it to your telegram database in audio format 🙂

Made By : @naviya2 🇱🇰
Support Group : @leosuppportx 🇱🇰
"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Channel", url="https://t.me/new_ehi"
                    ),
                    InlineKeyboardButton(
                        text="Developer", url="https://t.me/naviya2"
                    ),
                    InlineKeyboardButton(
                        text="Group", url="https://t.me/leosupportx"
                    ),
                
                ]

            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)

@app.on_message(filters.command("help"))
async def start(client, message):
    await message.reply(help_text)

app.start()
LOGGER.info("LeoSongDownloaderBot is online.")
idle()
