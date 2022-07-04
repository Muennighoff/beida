from flask import render_template, url_for, flash, redirect, request
from feixin import app, db, bcrypt, socketio
from feixin.forms import RegistrationForm, LoginForm, AddFriendForm, CreateRoomForm
from feixin.models import Friends, User, Rooms, RoomUsers
from flask_login import login_user, current_user, logout_user, login_required
from flask_socketio import SocketIO, send, join_room, leave_room, emit
import json
from time import localtime, strftime
import ftfy


@app.route("/")
@app.route("/home")
def home():
    if current_user.is_authenticated:
        # Only query friends
        friendsa = [
            User.query.filter_by(username=f.usernameb).all()[0]
            for f in Friends.query.filter_by(usernamea=current_user.username).all()
        ]
        friendsb = [
            User.query.filter_by(username=f.usernamea).all()[0]
            for f in Friends.query.filter_by(usernameb=current_user.username).all()
        ]
        # Get the Users
        userList = friendsa + friendsb

        # Get rooms of this user
        rooms = [
            room.roomname
            for room in RoomUsers.query.filter_by(username=current_user.username).all()
        ]
        return render_template("chat.html", roomList=rooms, room="global chat", userList=userList)
    return render_template("chat.html", roomList=[], room="global chat")


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("注册成功了！现在可以登录!", "success")
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("home"))
        else:
            flash("登录没有成功. 请再看你的电子邮件和密码。", "danger")
    return render_template("login.html", title="Login", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/addfriend", methods=["GET", "POST"])
@login_required
def addfriend():
    form = AddFriendForm()
    if form.validate_on_submit():
        friends = Friends(usernamea=current_user.username, usernameb=form.username.data)
        db.session.add(friends)
        db.session.commit()
        flash("加好友成功了。 现在可以聊天!", "success")
    return render_template("addfriend.html", title="Addfriend", form=form)


@app.route("/createroom", methods=["GET", "POST"])
@login_required
def createroom():
    form = CreateRoomForm()
    if form.validate_on_submit():
        room = Rooms.query.filter_by(roomname=form.roomname.data).first()
        # Create Room
        if not (room):
            room = Rooms(roomname=form.roomname.data)
            db.session.add(room)
            db.session.commit()
            # Add roomcreator
            room_users = RoomUsers(
                roomname=form.roomname.data,
                username=current_user.username,
            )
            db.session.add(room_users)
            db.session.commit()
            flash("创建组成功了!", "success")

        # Add Users
        room_users = RoomUsers(roomname=form.roomname.data, username=form.username.data)
        db.session.add(room_users)
        db.session.commit()
        flash("把朋友放到群里成功了!", "success")
    return render_template("createroom.html", title="Createroom", form=form)


### Socket.io ###


@socketio.on("message")
def handleMessage(msg):
    msgDict = json.loads(msg)
    print("\n\n{}\n\n".format(msgDict))
    # Handle mojibake
    msgDict["content"] = ftfy.fix_text(msgDict["content"])
    # msgDict["sender"] = ftfy.fix_text(msgDict["sender"])
    # msgDict["receiver"] = ftfy.fix_text(msgDict["receiver"])
    # msgDict["room"] = ftfy.fix_text(msgDict["room"])
    print("\n\n{}\n\n".format(msgDict))

    msgToDeliver = {
        "sender": msgDict["sender"],
        "receiver": msgDict["receiver"],
        "content": msgDict["content"],
        "timestamp": strftime("%I:%M %p", localtime()),
        "room": msgDict["room"],
    }

    rooms = [
        room.roomname for room in RoomUsers.query.filter_by(username=current_user.username).all()
    ]

    if msgDict["room"] == "GLOBAL" or "Global" in msgDict["room"]:
        send(json.dumps(msgToDeliver), broadcast=True)
    # Rooms
    elif msgDict["room"].lower() in rooms:
        send(json.dumps(msgToDeliver), room=msgToDeliver["room"])
    # One-to-one
    elif msgDict["room"].lower() not in rooms:
        row = Rooms.query.filter_by(roomname=msgDict["room"]).first()
        print("Message from {} to {}".format(msgDict["sender"], msgDict["receiver"]))
        if not (row):
            print("/nerror in handle message/n")
            return
        row.count = row.count + 1
        print("row.count:", row.count)
        print("row.message", row.message)
        dict1 = json.loads(row.message)

        dict1[row.count] = msgDict
        row.message = json.dumps(dict1)
        db.session.commit()
        send(json.dumps(msgToDeliver), room=msgToDeliver["room"])


@socketio.on("join")
def join(data):
    data = json.loads(data)
    print("\n\n", data)
    join_room(data["room"])
    msgToDeliver = {
        "sender": "SYSTEM",
        "content": "{} 加入了 {}".format(ftfy.fix_text(data["sender"]), ftfy.fix_text(data["room"])),
        "timestamp": strftime("%I:%M %p", localtime()),
    }
    send(json.dumps(msgToDeliver), room=data["room"])


@socketio.on("leave")
def leave(data):
    data = json.loads(data)
    print("\n\n", data)
    leave_room(data["room"])
    msgToDeliver = {
        "sender": "SYSTEM",
        "content": "{} 离开了 {}".format(ftfy.fix_text(data["sender"]), ftfy.fix_text(data["room"])),
        "timestamp": strftime("%I:%M %p", localtime()),
    }
    send(json.dumps(msgToDeliver), room=data["room"])


@socketio.on("connect")
def connect():
    if hasattr(current_user, "username"):
        user = User.query.filter_by(username=current_user.username).first()
        user.last_sid = request.sid
        db.session.commit()
        print("\n\n", user)


@socketio.on("request_for_connection")
def request_for_connection(request):
    request = json.loads(request)
    print("\n\n", request)
    # Search for recepient of request, named as recipient
    recipient = User.query.filter_by(username=request["to"]).first()
    print("\n\nIn request_for_connection:\n{}\n\n".format(recipient))
    emit("request_to_connect", json.dumps(request), room=recipient.last_sid)


@socketio.on("accept_request")
def accept_request(accept_msg):
    accept_msg = json.loads(accept_msg)
    print("\n\n", accept_msg)
    # Search for sender's entry and use his sid to deliver the request acceptance
    sender = User.query.filter_by(username=accept_msg["sender"]).first()
    emit("request_accepted", json.dumps(accept_msg), room=sender.last_sid)


@socketio.on("make_new_room")
def make_new_room(room_name):
    room_name = json.loads(room_name)
    row = Rooms.query.filter_by(roomname=room_name["room"]).first()
    if row:
        emit("load_history", row.message, room=row.roomname)
    else:
        row = Rooms(roomname=room_name["room"])
        db.session.add(row)
        db.session.commit()
