import os
import asyncio
import importlib
import logging
import random
from pyrogram import  idle
from pyrogram.client import Client
from PORN import ubot, app
from PORN.modules import ALL_MODULES
from PORN.core.db import add_user, add_group, all_users, all_groups, users, remove_user
from pyrogram import filters, errors
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import ChatAdminRequired, UserNotParticipant
from pyrogram.errors import FloodWait, PeerIdInvalid
from config import api_id, api_hash, bot_token,OWNER_ID
from PORN import app
import subprocess
import shlex
from pyrogram.errors import FloodWait


loop = asyncio.get_event_loop()


async def init():
  await app.start()
  for all_module in ALL_MODULES:
    importlib.import_module("PORN.modules." + all_module)
    print(f"LOADING {all_module} ...")
  await ubot.start()
  print(f"""\n
  ___  ___  ___ _  _   ___  ___ _____      _            _          _ 
 | _ \/ _ \| _ \ \| | | _ )/ _ \_   _|  __| |_ __ _ _ _| |_ ___ __| |
 |  _/ (_) |   / .` | | _ \ (_) || |   (_-<  _/ _` | '_|  _/ -_) _` |
 |_|  \___/|_|_\_|\_| |___/\___/ |_|   /__/\__\__,_|_|  \__\___\__,_|
""")
  await idle()

print(f"""\n
  ___           _     _                       
 |   \ ___ _ __| |___(_)_ _  __ _             
 | |) / -_) '_ \ / _ \ | ' \/ _` |  _   _   _ 
 |___/\___| .__/_\___/_|_||_\__, | (_) (_) (_)
          |_|               |___/             
""")


logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO
    format=
    '%(asctime)s - %(levelname)s - %(message)s',  # Define log message format
    filename='app.log',  # Log file name
    filemode='w')  # Set log file mode to 'write'

# Create a logger
logger = logging.getLogger()

# Log messages at different levels
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

# Define a filter to check if the user is in the channel or group
def check_user_in_channel(func):

  async def wrapper(_, message: Message):
    # Replace 'YOUR_CHANNEL_ID' with the ID of your channel or group
    channel_id = -100123456789  # Example channel ID
    user_id = message.from_user.id
    try:
      # Check if the user is in the channel
      await app.get_chat_member(channel_id, user_id)
      # User is found, allow them to use commands
      await func(_, message)
    except Exception as e:
      # User is not found, reply with a message asking them to join first
      await message.reply_text("Please join our channel or group first.")

  return wrapper


@app.on_message(filters.command("start"))
async def start(client, msg):
  await app.delete_bot_commands()
  channel_id = -1001967606455  # Example channel ID
  user_id = msg.from_user.id
  try:
    await app.get_chat_member(channel_id, user_id)
    await msg.reply_text(
        "Welcome to my bot",
        reply_markup=ReplyKeyboardMarkup(
            [["STUDY-MATERIAL", "VIDEOS", "EROTIC-VIDEOS"], ["INDIAN-VIDEOS"],
             ["JOIN-CHANNEL-FOR-UPDATES"], ["ABOUT"]],
            resize_keyboard=True))
  except Exception as e:
    abtbtn = InlineKeyboardMarkup([[
        InlineKeyboardButton("JOIN CHANNEL FOR UPDATES",
                             url="https://t.me/+Y9O5ptuPEFs3NGE1")
    ]])
    await msg.reply_text(
        "Please join our channel or group first. Then CLICK ON BUTTON RESTART ",
        reply_markup=abtbtn)


@app.on_message(filters.new_chat_members)
async def welcome_message(client, message):
  for member in message.new_chat_members:
    # Send a private message to the new member
    await client.send_message(
        chat_id=member.id,
        text="Welcome to my bot",
        reply_markup=ReplyKeyboardMarkup(
            [["STUDY-MATERIAL", "VIDEOS", "EROTIC-VIDEOS"], ["INDIAN-VIDEOS"],
             ["JOIN-CHANNEL-FOR-UPDATES"], ["ABOUT"]],
            resize_keyboard=True))
    await client.send_video(
        chat_id=member.id,
        video="https://telegra.ph/file/ba1f5214811914857ad44.mp4",
        caption="how to use this BOT \n \n **इस रोबोट का उपयोग कैसे करें**, ")


@app.on_message(filters.regex("ABOUT"))
async def about(client, msg):
  await app.delete_messages(chat_id=msg.chat.id, message_ids=msg.id)
  channel_id = -1001967606455  # Example channel ID
  user_id = msg.from_user.id
  try:
    await app.get_chat_member(channel_id, user_id)
    await msg.reply(
        text=
        "Disclaimer: This bot is made for Entertainment purposes only. \n\n if you want to create bots like this you can message me on @CODEX_ML_bot "
    )
  except Exception as e:
    abtbtn = InlineKeyboardMarkup([[
        InlineKeyboardButton("JOIN CHANNEL FOR UPDATES",
                             url="https://t.me/+Y9O5ptuPEFs3NGE1"),
        InlineKeyboardButton("RESTART  BOT",
                             url="http://t.me/Pronexe_bot?start=start")
    ]])
    await msg.reply_text(
        "Please join our channel or group first. Then CLICK ON BUTTON RESTART ",
        reply_markup=abtbtn)


@app.on_message(filters.regex("JOIN-CHANNEL-FOR-UPDATES"))
async def join(client, msg):
  await app.delete_messages(chat_id=msg.chat.id, message_ids=msg.id)
  channel_id = -1001967606455  # Example channel ID
  user_id = msg.from_user.id
  try:
    await app.get_chat_member(channel_id, user_id)
    # Delete the command message
    abtbtn = InlineKeyboardMarkup([[
        InlineKeyboardButton("JOIN CHANNEL FOR UPDATES",
                             url="https://t.me/source_code_network")
    ]])
    await msg.reply_text(
        text="This is a bot made with Pyrogram, developed by AKG",
        reply_markup=abtbtn)
  except Exception as e:
    abtbtn = InlineKeyboardMarkup([[
        InlineKeyboardButton("JOIN CHANNEL FOR UPDATES",
                             url="https://t.me/+Y9O5ptuPEFs3NGE1"),
        InlineKeyboardButton("RESTART  BOT",
                             url="http://t.me/Pronexe_bot?start=start")
    ]])
    await msg.reply_text(
        "Please join our channel or group first. Then CLICK ON BUTTON RESTART ",
        reply_markup=abtbtn)


# study
@app.on_message(filters.regex("STUDY-MATERIAL"))
async def study(client, msg):
  await app.delete_messages(chat_id=msg.chat.id, message_ids=msg.id)
  channel_id = -1001967606455  # Example channel ID
  user_id = msg.from_user.id
  source = -1001520808241
  file_name = "study.txt"

  try:
    await app.get_chat_member(channel_id, user_id)
    with open(file_name, "r") as file:
      message_ids = [int(line.strip()) for line in file.readlines()]

    if not message_ids:
      await msg.reply("The posts.txt file is empty.")
      return

    # Pick a random message id
    random_message_id = random.choice(message_ids)

    # Forward the message to the user who sent the command
    await client.copy_message(chat_id=msg.chat.id,
                              from_chat_id=source,
                              message_id=random_message_id,
                              disable_notification=True)
  except FileNotFoundError:
    await msg.reply(f"File '{file_name}' not found.")
  except Exception as e:
    await msg.reply(f"An error occurred: {e}")
    abtbtn = InlineKeyboardMarkup([[
        InlineKeyboardButton("JOIN CHANNEL FOR UPDATES",
                             url="https://t.me/+Y9O5ptuPEFs3NGE1"),
        InlineKeyboardButton("RESTART  BOT",
                             url="http://t.me/Pronexe_bot?start=start")
    ]])
    await msg.reply_text(
        "Please join our channel or group first. Then CLICK ON BUTTON RESTART ",
        reply_markup=abtbtn)


# dark
@app.on_message(filters.regex("DARKWEB-VIDEOS"))
async def dark(client, msg):
  await app.delete_messages(chat_id=msg.chat.id, message_ids=msg.id)
  channel_id = -1001967606455  # Example channel ID
  user_id = msg.from_user.id
  source = -1001605681909
  file_name = "dark.txt"

  try:
    await app.get_chat_member(channel_id, user_id)
    with open(file_name, "r") as file:
      message_ids = [int(line.strip()) for line in file.readlines()]

    if not message_ids:
      await msg.reply("The posts.txt file is empty.")
      return

    # Pick a random message id
    random_message_id = random.choice(message_ids)

    # Forward the message to the user who sent the command
    await client.copy_message(chat_id=msg.chat.id,
                              from_chat_id=source,
                              message_id=random_message_id,
                              disable_notification=True)
  except FileNotFoundError:
    await msg.reply(f"File '{file_name}' not found.")
  except Exception as e:
    await msg.reply(f"An error occurred: {e}")
    abtbtn = InlineKeyboardMarkup([[
        InlineKeyboardButton("JOIN CHANNEL FOR UPDATES",
                             url="https://t.me/+Y9O5ptuPEFs3NGE1"),
        InlineKeyboardButton("RESTART  BOT",
                             url="http://t.me/Pronexe_bot?start=start")
    ]])
    await msg.reply_text(
        "Please join our channel or group first. Then CLICK ON BUTTON RESTART ",
        reply_markup=abtbtn)


# videos
@app.on_message(filters.regex("VIDEOS"))
async def send_random_channel_post(client, msg):
  await app.delete_messages(chat_id=msg.chat.id, message_ids=msg.id)
  channel_id = -1001967606455  # Example channel ID
  user_id = msg.from_user.id
  source = -1002078572368
  file_name = "videos.txt"

  try:
    await app.get_chat_member(channel_id, user_id)
    with open(file_name, "r") as file:
      message_ids = [int(line.strip()) for line in file.readlines()]

    if not message_ids:
      await msg.reply("The posts.txt file is empty.")
      return

    # Pick a random message id
    random_message_id = random.choice(message_ids)

    # Forward the message to the user who sent the command
    await client.copy_message(chat_id=msg.chat.id,
                              from_chat_id=source,
                              message_id=random_message_id,
                              disable_notification=True)
  except FileNotFoundError:
    await msg.reply(f"File '{file_name}' not found.")
  except Exception as e:
    await msg.reply(f"An error occurred: {e}")
    abtbtn = InlineKeyboardMarkup([[
        InlineKeyboardButton("JOIN CHANNEL FOR UPDATES",
                             url="https://t.me/+Y9O5ptuPEFs3NGE1"),
        InlineKeyboardButton("RESTART  BOT",
                             url="http://t.me/Pronexe_bot?start=start")
    ]])
    await msg.reply_text(
        "Please join our channel or group first. Then CLICK ON BUTTON RESTART ",
        reply_markup=abtbtn)


# indian
@app.on_message(filters.regex("INDIAN-VIDEOS"))
async def INDIAN(client, msg):
  await app.delete_messages(chat_id=msg.chat.id, message_ids=msg.id)
  channel_id = -1001967606455  # Example channel ID
  user_id = msg.from_user.id
  source = -1002090806475
  file_name = "indian.txt"

  try:
    await app.get_chat_member(channel_id, user_id)
    with open(file_name, "r") as file:
      message_ids = [int(line.strip()) for line in file.readlines()]

    if not message_ids:
      await msg.reply("The posts.txt file is empty.")
      return

    # Pick a random message id
    random_message_id = random.choice(message_ids)

    # Forward the message to the user who sent the command
    await client.copy_message(chat_id=msg.chat.id,
                              from_chat_id=source,
                              message_id=random_message_id,
                              disable_notification=True)
  except FileNotFoundError:
    await msg.reply(f"File '{file_name}' not found.")
  except Exception as e:
    await msg.reply(f"An error occurred: {e}")
    abtbtn = InlineKeyboardMarkup([[
        InlineKeyboardButton("JOIN CHANNEL FOR UPDATES",
                             url="https://t.me/+Y9O5ptuPEFs3NGE1"),
        InlineKeyboardButton("RESTART  BOT",
                             url="http://t.me/Pronexe_bot?start=start")
    ]])
    await msg.reply_text(
        "Please join our channel or group first. Then CLICK ON BUTTON RESTART ",
        reply_markup=abtbtn)


@app.on_message(filters.command("broadcast") & filters.private)
async def broadcast_message(client, msg):
  # Get the message text or reply if provided
  text = msg.text.split(maxsplit=1)[1] if len(msg.text.split()) > 1 else None
  reply_to_message_id = msg.reply_to_message.message_id if msg.reply_to_message else None

  # Get all private chat users
  all_users = await client.get_users(is_bot=False)

  # Forward message to each user
  for user in all_users:
    try:
      await client.copy_message(chat_id=user.id,
                                from_chat_id=msg.chat.id,
                                message_id=reply_to_message_id,
                                disable_notification=True)
      if text:
        await client.send_message(chat_id=user.id, text=text)
    except Exception as e:
      print(f"Error sending message to user {user.id}: {e}")

  await msg.reply("Broadcast sent to all users!")





@app.on_message(filters.command("eval") & filters.user(OWNER_ID))
async def eval_python(client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("Please provide a Python code snippet to execute.")
        return

    # Extracting the code to execute
    code = message.text.split(None, 1)[1]

    # Security: It's critical to ensure that the executed code does not pose a risk
    # Implement code safety checks or sandboxing as needed

    # Executing the code
    exec_locals = {}
    try:
        exec(code, {}, exec_locals)
    except Exception as e:
        await message.reply_text(f"Error executing code: {e}")
        return

    await message.reply_text("Code executed successfully.")

@app.on_message(filters.command("sh") & filters.user(OWNER_ID))
async def exec_shell(client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("Please provide a shell command to execute.")
        return

    command = message.text.split(None, 1)[1]

    # Execute shell command
    try:
        proc = await asyncio.create_subprocess_shell(
            command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE)
        stdout, stderr = await proc.communicate()

        # Sending the results back to the user
        response_message = f"Output:\n{stdout.decode()}\nErrors:\n{stderr.decode()}"
        if len(response_message) > 4096:
            # If message is too long, send as a text file
            with open("output.txt", "w") as file:
                file.write(response_message)
            await message.reply_document("output.txt")
            os.remove("output.txt")
        else:
            await message.reply_text(response_message)
    except Exception as e:
        await message.reply_text(f"Error: {e}")





if __name__ == "__main__":
  loop.run_until_complete(init())
  print("Stopping Bot! GoodBye")
