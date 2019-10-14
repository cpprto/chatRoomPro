import json

from flask import Flask
from flask import request
from geventwebsocket.server import WSGIServer
from geventwebsocket.handler import WebSocketHandler
from geventwebsocket.websocket import WebSocket

app = Flask(__name__)
userO2m_socket_dict = {}
userO2o_socket_dict = {}


# 获取在线人数及明细
@app.route("/get_user_info")
def get_user_info():
    user_socket = request.environ.get("wsgi.websocket")
    while user_socket:
        user_socket.receive()
        data = {"online": online, "detail": detail}
        data = json.dumps(data)
        user_socket.send(data)


# 群聊
@app.route("/o2m/<username>")
def o2m(username):
    global online, detail
    user_socket = request.environ.get("wsgi.websocket")  # type: WebSocket
    if user_socket:
        userO2m_socket_dict[username] = user_socket

    while True:
        try:
            online = len(userO2m_socket_dict)
            detail = list(userO2m_socket_dict.keys())
            msg = user_socket.receive()
            for user in userO2m_socket_dict.values():
                user.send(msg)
        except:
            del userO2m_socket_dict[username]
            continue


# 私聊
@app.route("/o2o/<username>")
def o2o(username):
    user_socket = request.environ.get("wsgi.websocket")  # type: WebSocket
    if user_socket:
        userO2o_socket_dict[username] = user_socket

    while True:
        try:
            msg = user_socket.receive()
            msg_dict = json.loads(msg)

            to_user_link = msg_dict.get("toUser")
            from_user_link = msg_dict.get("fromUser")

            to_user_socket = userO2o_socket_dict.get(to_user_link)
            from_user_socket = userO2o_socket_dict.get(from_user_link)

            to_user_socket.send(msg)
            from_user_socket.send(msg)
        except:
            del userO2o_socket_dict[username]
            continue


if __name__ == "__main__":
    server = WSGIServer(("0.0.0.0", 8527), app, handler_class=WebSocketHandler)
    server.serve_forever()
