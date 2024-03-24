from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", None))
API_HASH = getenv("API_HASH", None)
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = int(getenv("OWNER_ID", None))
MONGO_URL = getenv("MONGO_URL", None)
SUPPORT_GRP = getenv("SUPPORT_GRP", None)
UPDATE_CHNL = getenv("UPDATE_CHNL", None)
OWNER_USERNAME = getenv("OWNER_USERNAME", None)

IMG = [ ]

STICKER = [ ]

EMOJIOS = [ ]
