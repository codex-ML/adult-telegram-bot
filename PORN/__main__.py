import os
import asyncio
import importlib
import logging
import random
from pyrogram import idle
from pyrogram.client import Client
from PORN import ubot, app
from PORN.modules import ALL_MODULES
from PORN.core.db import add_user, add_group, all_users, all_groups, users, remove_user
from pyrogram import filters, errors
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import ChatAdminRequired, UserNotParticipant
from pyrogram.errors import FloodWait, PeerIdInvalid
from config import api_id, api_hash, bot_token, OWNER_ID
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
             ["STICKERS"], ["EROTIC-PICS"], ["ROMANTIC-GIFS"], ["SKETCH-PICS"],
             ['ROMANTIC-VIDEOS'], ['MEMES'], ['B/W-PICS'], ["GIFs"],
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


# Erotic:= -1002063856222
# Desii mms= -1002081710985 n
# Videos= -1002078572368
# Indian= -1002090806475
# Study material= -1001520808241
# Cp:- -1002123235233  n
# Stickers:- -1002045122639
# Erotic pics:- -1001797093743
# Romantic gif:- -1002079691484
# Sketch pic's:- -1002122885087
# Romantic  videos:- -1002141649293 n
# Gifs:- -1002111945338
# B/w:- -1002135195418 n
# Memes:- -1002002638378 n


@app.on_message(filters.new_chat_members)
async def welcome_message(client, message):
  for member in message.new_chat_members:
    # Send a private message to the new member
    await client.send_message(
        chat_id=member.id,
        text="Welcome to my bot",
        reply_markup=ReplyKeyboardMarkup(
            [["STUDY-MATERIAL", "VIDEOS", "EROTIC-VIDEOS"], ["INDIAN-VIDEOS"],
             ["STICKERS"], ["EROTIC-PICS"], ["ROMANTIC-GIFS"], ["SKETCH-PICS"],
             ['ROMANTIC-VIDEOS'], ['MEMES'], ['B/W-PICS'], ["GIFs"],
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


# rvideos.txt
@app.on_message(filters.regex("ROMANTIC-VIDEOS"))
async def rvideos(client, msg):
  await app.delete_messages(chat_id=msg.chat.id, message_ids=msg.id)
  channel_id = -1001967606455  # Example channel ID
  user_id = msg.from_user.id
  source = -1002141649293
  file_name = "rvideos.txt"

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


# bw
@app.on_message(filters.regex("B/W-PICS"))
async def bw(client, msg):
  await app.delete_messages(chat_id=msg.chat.id, message_ids=msg.id)
  channel_id = -1001967606455  # Example channel ID
  user_id = msg.from_user.id
  source = -1002135195418
  file_name = "bw.txt"

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


# memes
@app.on_message(filters.regex("MEMES"))
async def meme(client, msg):
  await app.delete_messages(chat_id=msg.chat.id, message_ids=msg.id)
  channel_id = -1001967606455  # Example channel ID
  user_id = msg.from_user.id
  source = -1002002638378
  file_name = "memes.txt"

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


# GIFs
@app.on_message(filters.regex("GIFs"))
async def gifs(client, msg):
  await app.delete_messages(chat_id=msg.chat.id, message_ids=msg.id)
  channel_id = -1001967606455  # Example channel ID
  user_id = msg.from_user.id
  source = -1002111945338
  file_name = "gifs.txt"

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


# SKETCH-PICS
@app.on_message(filters.regex("SKETCH-PICS"))
async def SKETCHPIC(client, msg):
  await app.delete_messages(chat_id=msg.chat.id, message_ids=msg.id)
  channel_id = -1001967606455  # Example channel ID
  user_id = msg.from_user.id
  source = -1002122885087
  file_name = "SKETCH.txt"

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


# ROMANTIC-GIFS
@app.on_message(filters.regex("ROMANTIC-GIFS"))
async def ROMANTICGIF(client, msg):
  await app.delete_messages(chat_id=msg.chat.id, message_ids=msg.id)
  channel_id = -1001967606455  # Example channel ID
  user_id = msg.from_user.id
  source = -1002079691484
  file_name = "ROMANTICgif.txt"

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


# EROTIC PICS
@app.on_message(filters.regex("EROTIC-PICS"))
async def EPICS(client, msg):
  await app.delete_messages(chat_id=msg.chat.id, message_ids=msg.id)
  channel_id = -1001967606455  # Example channel ID
  user_id = msg.from_user.id
  source = -1001797093743
  file_name = "EROTICPICS.txt"

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


# STICKRS
@app.on_message(filters.regex("STICKERS"))
async def STICKER(client, msg):
  await app.delete_messages(chat_id=msg.chat.id, message_ids=msg.id)
  channel_id = -1001967606455  # Example channel ID
  user_id = msg.from_user.id
  source = -1002045122639
  file_name = "STICKER.txt"

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
        InlineKeybo
