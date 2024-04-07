from pyrogram.client import Client
from config import api_id, api_hash, session

class UserBot(Client):
    def __init__(self):
        super().__init__(
            "userbot",
            api_id=api_id,
            api_hash=api_hash,
            session_string=session
        )

print("User Connected Successfully!")
