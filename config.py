# 数据库配置
from pymongo import MongoClient
from redis import Redis

client = MongoClient(host="127.0.0.1", port=27017)
DB = client["Chat"]

RDB = Redis(host="127.0.0.1", port=6379, db=0)

# 返回值格式
RET = {
    "CODE": 0,
    "MSG": "",
    "DATA": {}
}

# 文件路径
AVATAR = "avatar"
RECOFILE_PATH = "reco"
MUSIC_PATH = "music"

# APIKEY
APP_ID = ""
API_KEY = ""
SECRET_KEY = ""
TL_API_KEY = ""