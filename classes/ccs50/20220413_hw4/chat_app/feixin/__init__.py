import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_socketio import send, SocketIO
from flask_sqlalchemy import SQLAlchemy

cur_dir = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)
app.config["SECRET_KEY"] = "5391628bb0b13ce0c676dfde280ba245"
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{cur_dir}/db/chat.db"
app.config["SQLALCHEMY_BINDS"] = {
    "rooms": f"sqlite:///{cur_dir}/db/rooms.db",
    "friends": f"sqlite:///{cur_dir}/db/friends.db",
    "roomusers": f"sqlite:///{cur_dir}/db/roomusers.db",
}

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"

socketio = SocketIO(app)

# Required for flask to work
from feixin import routes, models


if not os.path.exists(f"{cur_dir}/db/chat.db"):
    db.create_all()
