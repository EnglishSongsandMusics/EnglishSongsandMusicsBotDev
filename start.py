from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""Hello ð there! I can play music in voice chats of Telegeam Groups. I have a lot of cool feature that will amaze you!\n\nð´ Do you want me to play music in your Telegram groups'voice chats? Please click the \'ð User Manual ð\' button below to know how you can use me.\n\nð´ The Assistant must be in your group to play music in the voice chat of your group.\n\nð´ More info & commands mentioned in the [User Manual]\n\nA project by @EnglishSongsandMusics""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "Join Our Famâ¤", url="https://t.me/english_songs_and_musics")
                  ],[
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/selenawayne"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "Our Channel", url="https://t.me/english_songs_and_musics"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**ð´ Music player is online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Support Chat", url="https://t.me/english_songs_and_musics")
                ]
            ]
        )
   )

