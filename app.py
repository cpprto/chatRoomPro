from flask import Flask

from serv.users import users_bp
from serv.media_chat import media_bp

app = Flask(__name__)
app.register_blueprint(users_bp)
app.register_blueprint(media_bp)

if __name__ == "__main__":
    app.run("0.0.0.0", 9527)
