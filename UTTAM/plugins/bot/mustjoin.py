from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden

# Replace these with your actual channel usernames or IDs
MUST_JOIN_1 = "DP_WORLD7"  # Replace with your first channel username or ID
MUST_JOIN_2 = "ll_BOTCHAMBER_ll"  # Replace with your second channel username or ID

app = Client("my_bot")

@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channels(client: Client, msg: Message):
    if not MUST_JOIN_1 or not MUST_JOIN_2:
        return

    async def check_membership(channel_id):
        try:
            await client.get_chat_member(channel_id, msg.from_user.id)
            return None
        except UserNotParticipant:
            if channel_id.isalpha():
                return "https://t.me/" + channel_id
            else:
                chat_info = await client.get_chat(channel_id)
                return chat_info.invite_link

    try:
        link_1 = await check_membership(MUST_JOIN_1)
        link_2 = await check_membership(MUST_JOIN_2)

        if link_1 or link_2:
            buttons = []
            if link_1:
                buttons.append([InlineKeyboardButton("๏ Join Channel 1 ๏", url=link_1)])
            if link_2:
                buttons.append([InlineKeyboardButton("๏ Join Channel 2 ๏", url=link_2)])

            try:
                await msg.reply_photo(
                    photo="https://envs.sh/jeg.jpg",  # Replace with a valid URL or file_id
                    caption=(f"**👋 ʜᴇʟʟᴏ {msg.from_user.mention},**\n\n"
                             "**ʏᴏᴜ ᴍᴜsᴛ ᴊᴏɪɴ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ᴄʜᴀɴɴᴇʟs ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ:**"),
                    reply_markup=InlineKeyboardMarkup(buttons))
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Promote me as admin in one or both channels: {MUST_JOIN_1}, {MUST_JOIN_2}!")

