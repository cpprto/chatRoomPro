import os
from uuid import uuid4

from flask import Blueprint
from flask import request
from flask import jsonify
from flask import send_file

from config import RET
from config import RECOFILE_PATH
from config import MUSIC_PATH
from utils.media_utils import a2t, nlp_no1

media_bp = Blueprint("media_bp", __name__)


@media_bp.route("/media_uploader", methods=["POST"])
def media_uploader():
    file = request.files.get("media")
    filename = request.form.get("src")
    filename = filename.split("/")[-1].replace('"', "")
    file_path = os.path.join(RECOFILE_PATH, f"{filename}.wav")
    file.save(file_path)

    RET["CODE"] = 0
    RET["MSG"] = "发送成功"
    RET["DATA"] = {}

    return jsonify(RET)


@media_bp.route("/ai_uploader", methods=["POST"])
def ai_uploader():
    file = request.files.get("media")
    q_path = os.path.join(RECOFILE_PATH, f"{uuid4()}.wav")
    file.save(q_path)

    text = a2t(q_path)  # 将语音消息转换为文字

    res = nlp_no1(text)  # 通过 NLP 进行处理

    return res


# 获取提示信息
@media_bp.route("/get_music/<filename>")
def get_music(filename):
    music_path = os.path.join(MUSIC_PATH, filename)

    return send_file(music_path)


# 获取语音消息
@media_bp.route("/<src>")
def get_msg(src):
    src = src.split("/")[-1]
    file_path = os.path.join(RECOFILE_PATH, src)
    return send_file(file_path)


# 处理 AI 对话语音消息
@media_bp.route("/get_chat/<chat_name>")
def get_chat(chat_name):
    chat_path = os.path.join(RECOFILE_PATH, chat_name)
    return send_file(chat_path)
