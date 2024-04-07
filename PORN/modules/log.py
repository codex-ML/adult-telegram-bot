from pyrogram.client import Client
from pyrogram import Client, filters
from pyrogram.types import Message
from config import OWNER_ID
from PORN import app



@app.on_message(filters.command("logs") & filters.user(OWNER_ID))
async def execute_command(client, message: Message):
    # Specify the path to your log file
    log_file_path = 'app.log'
    
    try:
        # Open the log file and send it as a document
        await message.reply_document(document=log_file_path, caption="Here are the logs.")
    except Exception as e:
        # If something goes wrong, send a message with the error
        await message.reply_text(f"An error occurred: {str(e)}")