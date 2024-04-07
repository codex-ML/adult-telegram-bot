import asyncio
from pyrogram import Client, filters
from aiofiles import open as aio_open  # aio_open is used to avoid confusion with built-in open
from config import api_id, api_hash, session, OWNER_ID
from PORN import ubot



import asyncio
from pyrogram import Client, filters
from aiofiles import open as aio_open

# Erotic:= -1002063856222
# Desii mms= -1002081710985
# Videos= -1002078572368
# Indian= -1002090806475

channel_files = {
    -1002063856222: 'erotic.txt',
    -1002090806475: 'indian.txt',
    -1002078572368: 'videos.txt',
    -1001520808241: 'study.txt'
}

async def scrape_messages(client, channel_id, file_name):
    offset_id = 0
    message_count = 0  # Initialize message count
    
    async with aio_open(file_name, "a") as file:
        async for msg in client.get_chat_history(channel_id, limit=0, offset_id=offset_id):
            await file.write(f"{msg.id}\n")
            offset_id = msg.id
            message_count += 1
        
        await file.flush()
        notification_msg = f"Scraped {message_count} messages for channel {channel_id} into {file_name}."
        await client.send_message(chat_id=-1001903774899, text=notification_msg)
        print(notification_msg)

async def scrape_all_channels(client):
    for channel_id, file_name in channel_files.items():
        await scrape_messages(client, channel_id, file_name)

@ubot.on_message(filters.command("scrape") & filters.user(OWNER_ID))
async def handle_scrape_command(client, message):
    await message.reply_text("Scraping started. Please wait...")
    await scrape_all_channels(client)
    await message.reply_text("Scraping finished.")
