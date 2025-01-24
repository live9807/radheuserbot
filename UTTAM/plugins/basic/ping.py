import time
from datetime import datetime

import speedtest
from pyrogram import Client, filters
from pyrogram.raw import functions
from pyrogram.types import Message

from UTTAM import StartTime, app, SUDO_USER
from UTTAM.helper.PyroHelpers import SpeedConvert
from UTTAM.plugins.bot.inline import get_readable_time

from UTTAM.plugins.help import add_command_help

class WWW:
    SpeedTest = (
        "Speedtest started at `{start}`\n\n"
        "Ping:\n{ping} ms\n\n"
        "Download:\n{download}\n\n"
        "Upload:\n{upload}\n\n"
        "ISP:\n__{isp}__"
    )

    NearestDC = "Country: `{}`\n" "Nearest Datacenter: `{}`\n" "This Datacenter: `{}`"

@Client.on_message(
    filters.command(["speedtest"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def speed_test(client: Client, message: Message):
    new_msg = await message.reply_text("`Running speed test . . .`")
    try:
       await message.delete()
    except:
       pass
    spd = speedtest.Speedtest()

    new_msg = await new_msg.edit(
        f"`{new_msg.text}`\n" "`Getting best server based on ping . . .`"
    )
    spd.get_best_server()

    new_msg = await new_msg.edit(f"`{new_msg.text}`\n" "`Testing download speed . . .`")
    spd.download()

    new_msg = await new_msg.edit(f"`{new_msg.text}`\n" "`Testing upload speed . . .`")
    spd.upload()

    new_msg = await new_msg.edit(
        f"`{new_msg.text}`\n" "`Getting results and preparing formatting . . .`"
    )
    results = spd.results.dict()

    await new_msg.edit(
        WWW.SpeedTest.format(
            start=results["timestamp"],
            ping=results["ping"],
            download=SpeedConvert(results["download"]),
            upload=SpeedConvert(results["upload"]),
            isp=results["client"]["isp"],
        )
    )



@Client.on_message(
    filters.command(["ping"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def pingme(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xx = await message.reply_text("**0% ▒▒▒▒▒▒▒▒▒▒**")
    try:
       await message.delete()
    except:
       pass
    await xx.edit("**20%  ██▒▒▒▒▒▒▒▒▒▒▒▒**")
    await xx.edit("**40%  ███▒▒▒▒▒▒▒▒▒▒▒**")
    await xx.edit("**60%  █████▒▒▒▒▒▒▒▒▒**")
    await xx.edit("**80%  ███████▒▒▒▒▒▒▒**")
    await xx.edit("**100% ████████████▒▒**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await xx.edit(
        f"❏ **╰☞ ʀᴀᴅʜᴇ **\n"
        f"├• **╰☞ 𝐒ᴘᴇᴇᴅ**`%sms`\n"
        f"├• **╰☞ 𝐔ᴘᴛɪᴍᴇ** `{uptime}` \n"
        f"└• **╰☞ 𝐍ᴀᴍᴇ:** {client.me.mention}" % (duration)
    )


add_command_help(
    "ping",
    [
        ["ping", "Check bot alive or not."],
    ],
)
