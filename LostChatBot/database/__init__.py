from pymongo import MongoClient

import config

vickdb = MongoClient(config.MONGO_URL)
vick = LostChatBot["LostChatBot"]["LostChatBot"]

from .chats import *
from .users import *
