from pyrogram.client import Client
from pyrogram import Client, filters
from config import api_id, api_hash, bot_token,OWNER_ID
from PORN import app
from pyrogram.errors import FloodWait
from pyrogram.types import Message
from PORN.core.db import add_user, add_group, all_users, all_groups, users, remove_user
import asyncio

@app.on_message(filters.command("users") & filters.user(OWNER_ID))
async def dbtool(_, m : Message):
    xx = all_users()
    x = all_groups()
    tot = int(xx + x)
    await m.reply_text(text=f"""
🍀 Chats Stats 
🙋‍♂️ Users : `{xx}`
👥 Groups : `{x}`
🚧 Total users & groups : `{tot}` """)