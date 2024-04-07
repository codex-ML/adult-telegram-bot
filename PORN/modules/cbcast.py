from pyrogram.client import Client
from pyrogram import Client, filters
from config import api_id, api_hash, bot_token,OWNER_ID
from PORN import app
from pyrogram.errors import FloodWait
from pyrogram.types import Message
from PORN.core.db import add_user, add_group, all_users, all_groups, users, remove_user

@app.on_message(filters.command("bcast") & filters.user(OWNER_ID))
async def bcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"Successfull to `{success}` users.\nFaild to `{failed}` users.\nFound `{blocked}` Blocked users \nFound `{deactivated}` Deactivated users.")
