from pyrogram import filters
from pyrogram.types import Message

from StringGen import Anony
from StringGen.utils import add_served_user, keyboard


@Anony.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    await message.reply_text(
        text=f"𝘄𝗼𝘆 {message.from_user.first_name},\n\n๏ 𝗯𝗶𝗷𝗶 {Anony.mention},\𝗷𝗲𝗺𝗯𝘂𝘁 𝘄𝗼𝘆 𝗴𝘂𝗮 𝗮𝗱𝗮𝗹𝗮𝗵 𝗯𝗼𝘁 𝘀𝘁𝗿𝗶𝗻𝗴 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗴𝘂𝗮 𝗯𝗶𝘀𝗮 𝗮𝗺𝗯𝗶𝗹 𝘀𝘁𝗿𝗶𝗻𝗴 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝘁𝗲𝗹𝗲𝘁𝗵𝗼𝗻 & 𝗽𝘆𝗿𝗼𝗴𝗿𝗮𝗺𝘃𝟭 & 𝗽𝘆𝗿𝗼𝗴𝗿𝗮𝗺𝘃𝟮 𝘀𝗶𝗹𝗮𝗵𝗸𝗮𝗻 𝗽𝗶𝗹𝗶𝗵 𝗹𝘂 𝗺𝗮𝘂 𝘆𝗮𝗻𝗴 𝗺𝗮𝗻𝗮 𝗮𝗻𝗷𝗴.",
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
    await add_served_user(message.from_user.id)
