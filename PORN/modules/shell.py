from pyrogram.client import Client
from pyrogram import Client, filters
from pyrogram.types import Message
from config import OWNER_ID
from PORN import app
import os
import subprocess
import shlex




@app.on_message(filters.command("sh") & filters.user(OWNER_ID))
async def execute_command(client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("Please provide a command to execute.")
        return

    command = " ".join(message.command[1:])
    try:
        # Execute the command
        process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        exit_code = process.wait()

        # Prepare the response message
        response_message = f"**Command:**\n`{command}`\n\n"
        if stdout:
            response_message += f"**Output:**\n`{stdout.decode()}`\n"
        if stderr:
            response_message += f"**Error:**\n`{stderr.decode()}`\n"
        response_message += f"**Exit Code:** `{exit_code}`"

        # Send the response back
        await message.reply_text(response_message, parse_mode="markdown")
    except Exception as e:
        await message.reply_text(f"Error executing command:\n`{e}`", parse_mode="markdown")
