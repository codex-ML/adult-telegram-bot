from pyrogram.client import Client
from pyrogram import Client, filters
from config import api_id, api_hash, bot_token,OWNER_ID
from PORN import app
from pyrogram.errors import FloodWait
from pyrogram.types import Message
from PORN.core.db import add_user, add_group, all_users, all_groups, users, remove_user
import asyncio

@app.on_message(filters.command("upload") & filters.reply)
async def upload_info(client, message: Message):
            # Check if the replied message contains a document
       if not message.reply_to_message.document:
            await message.reply_text("Please reply to a file message.")
            return
            
            # Extract file information
            document = message.reply_to_message.document
            file_name = document.file_name
            file_size = document.file_size  # Size in bytes

            # Reply with file information
            info_message = await message.reply_text(f"File Name: {file_name}\nFile Size: {file_size} bytes\n\nDownloading...")
            
            # Download the document
            file_path = await message.reply_to_message.download()
            await info_message.edit(f"File downloaded successfully: {file_path}")