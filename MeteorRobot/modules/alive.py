import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from MeteorRobot.events import register
from MeteorRobot import telethn as tbot


PHOTO = "https://te.legra.ph/file/c8a24a036d02abca16395.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm 𝗨𝗡𝗢𝗙𝗙𝗜𝗖𝗜𝗔𝗟 𝗥𝗢𝗕𝗢𝗧.** \n\n"
  TEXT += "⚪ **I'm Working Properly** \n\n"
  TEXT += f"⚪ **Master Mind: Roman  × [𓃮]™](https://t.me/lll_Romaan_lll)** \n\n"
  TEXT += f"⚪ **Library Version :** `{telever}` \n\n"
  TEXT += f"⚪ **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"⚪ **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("Help", "https://t.me/Silent_robo_11?start=help"), Button.url("Support", "https://t.me/+JWHEg2H-FutjOTU1")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
