from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from bot import Bot
from config import CHANNEL1, CHANNEL2, CHANNEL3, GROUP, OWNER


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=f"<b>Tentang Bot ini:\n\n • ᴏᴡɴᴇʀ: @{OWNER}\n • ᴄʜᴀɴɴᴇʟ¹: @{CHANNEL1}\n • ᴄʜᴀɴɴᴇʟ²: @{CHANNEL2}\n • ᴄʜᴀɴɴᴇʟ³: @{CHANNEL3}\n • ɢʀᴏᴜᴘs: @{GROUP}\n • sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ: <a href='https://xnxx.com'>ᴋʟɪᴋ ᴅɪsɪɴɪ</a></b>\n",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")]]
            ),
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass
