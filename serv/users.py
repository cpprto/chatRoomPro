import os
import hashlib
from uuid import uuid4

from flask import Blueprint
from flask import request
from flask import render_template
from flask import redirect
from flask import send_file

from config import DB
from config import RET
from config import AVATAR

users_bp = Blueprint("users_bp", __name__)


# 登录
@users_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        user_data = request.form.to_dict()
        user_data["password"] = hashlib.md5(user_data["password"].encode()).hexdigest()
        user_info = DB.Chatusers.find_one(user_data)
        if user_info:
            RET["CODE"] = 0
            RET["MSG"] = "登录成功"
            RET["DATA"] = {"username": user_data["username"], "avatar": user_info["avatar"]}

            return render_template("index.html", RET=RET)
        else:

            return redirect("login.html")


# 注册
@users_bp.route("/reg", methods=["GET", "POST"])
def reg():
    if request.method == "GET":
        return render_template("reg.html")
    else:
        user_data = request.form.to_dict()
        user_data["password"] = hashlib.md5(user_data["password"].encode()).hexdigest()
        avatar = request.files.get("avatar")

        avatar_name = f"{uuid4()}.jpg"
        avatar_path = os.path.join(AVATAR, avatar_name)
        avatar.save(avatar_path)
        user_data["avatar"] = avatar_name

        DB.Chatusers.insert_one(user_data)

        RET["CODE"] = 0
        RET["MSG"] = "注册成功"
        RET["DATA"] = {"username": user_data["username"]}

        return redirect("login")


# 获取用户头像
@users_bp.route("/avatar/<avatar>")
def get_avatar(avatar):
    avatar_path = os.path.join(AVATAR, avatar)

    return send_file(avatar_path)
