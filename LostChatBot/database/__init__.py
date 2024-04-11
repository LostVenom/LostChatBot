from pymongo import MongoClient

import config

lostdb = MongoClient(config.MONGO_URL)
lost = lostdb["LostDb"]["Lost"]

from .chats import *
from .users import *
