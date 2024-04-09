from pyrogram import filters, Client
from pyrogram.types import Message

from LostChatBot import OWNER, VenomBot
from LostChatBot.database.chats import get_served_chats
from LostChatBot.database.users import get_served_users


@VenomBot.on_message(filters.command("stats") & filters.user(OWNER))
async def stats(cli: Client, message: Message):
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    await message.reply_text(
        f"""☞ 𝖲𝗍𝖺𝗍𝗌 𝖠𝗇𝖽 𝖨𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇 : {(await cli.get_me()).mention} :

 **⪼ 𝖢𝗁𝖺𝗍𝗌 :** {chats}
 **⪼ 𝖴𝗌𝖾𝗋𝗌 :** {users}"""
    )
