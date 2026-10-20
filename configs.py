# Don't Remove Credit Tg - @VJ_Bots
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "22876298"))
  API_HASH = os.environ.get("API_HASH", "cda7be15fbe283b5b97e8fb8c4233e36")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "8973404076:AAG4D365ocNheIwoNRcYMx2hTWDP5jlStl8")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "@KC_FILESBOT")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002462127875"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "8340629952"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Vishnuabhyantha_db:Baadshah@cluster0.fuxtgqk.mongodb.net/?appName=Cluster0")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1003797665459")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1004388805440"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [KC](https://telegram.me/Kannada_cinehub)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/Kannada_cinehub)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.
"""
