document.addEventListener('DOMContentLoaded', () => {
    // Connecting
    var socket = io.connect('http://' + document.domain + ':' + location.port);
    var username = document.querySelector(".username").innerHTML;

    // Get list of public chat rooms
    publicRooms = [];
    document.querySelectorAll('.room-opt').forEach(li => {
        publicRooms.push(li.innerHTML);
    })

    console.log(publicRooms);

    // Display received message
    socket.on('message', (msg) => {
        console.log(`Message received: ${msg}`);
        msg = JSON.parse(msg);
        if (msg['room'] !== roomName) {
            console.log("I don't know what to do");
        }
        if (msg['sender'] === 'SYSTEM') {
            let msgDisplay = document.createElement('h4');
            msgDisplay.innerHTML = msg['content'];
            let listItem = document.createElement('div');
            listItem.appendChild(msgDisplay);
            listItem.classList.add('themActivity');
            document.getElementById('messages-list').appendChild(listItem);

        }
        else if (msg['room'] === roomName) {
            let msgDisplay = document.createElement('h4');
            // msgDisplay.innerText = `${msg["sender"]} (${msg["timestamp"]}): ${msg["content"]}`;
            msgDisplay.innerHTML = msg['content'];
            let timestamp = document.createElement('h6');
            timestamp.innerHTML = msg['timestamp'];
            let listItem = document.createElement('div');
            listItem.appendChild(msgDisplay);
            listItem.appendChild(timestamp);
            if (msg['sender'] === username) {
                listItem.classList.add('meActivity');
            }
            else {
                listItem.classList.add('themActivity');
            }

            document.getElementById('messages-list').appendChild(listItem);
        }
        scrollDownChatWindow();
    });

    // Select user input field and send button from DOM
    let sendButton = document.querySelector('#send-btn');
    let userInput = document.querySelector('#user-input');

    // Function to send a message
    sendMessage = () => {
        if (userInput.value !== '') {
            msg = {
                'sender': username,
                'content': userInput.value,
                'room': roomName
            };
            if (publicRooms.includes(roomName)) {
                console.log('sending on public chatroom')
                msg['receiver'] = null;
            }
            else if (roomName === 'GLOBAL') {
                msg['receiver'] = null;
                console.log('sending to global chat');
            }
            else {
                msg['receiver'] = document.querySelector('#room-name').innerHTML;
                console.log(`sending to ${msg['receiver']}`)
            }
            socket.send(JSON.stringify(msg));
            userInput.value = "";
        }
    };

    // Listener for send action: Enter key
    userInput.addEventListener("keyup", (e) => {
        if (e.keyCode === 13) {
            if (userInput === document.activeElement) {
                e.preventDefault();
                sendMessage();
            }
        }
    });

    // Listener for send action: Send button clicked
    sendButton.onclick = () => {
        sendMessage();
    };

    // Listener for room-opt clicks
    document.querySelectorAll('.room-opt').forEach(li => {

        li.onclick = () => {

            let newRoom = li.innerHTML;
            if (newRoom === roomName) {  // User already in that room
                console.log(`User already in ${roomName}`); // Write alert code later
            }
            else {
                leaveRoom(roomName);
                joinRoom(newRoom);
                roomName = newRoom;
                document.querySelector('#room-name').innerHTML = newRoom;
            }
        }
    });

    // Function for leaving a room
    leaveRoom = (oldRoom) => {
        leave_msg = {
            'sender': username,
            'room': oldRoom
        }
        socket.emit('leave', JSON.stringify(leave_msg));
    }

    // Function for joining a room
    joinRoom = (newRoom) => {
        join_msg = {
            'sender': username,
            'room': newRoom
        }
        socket.emit('join', JSON.stringify(join_msg));
        document.querySelector('#messages-list').innerHTML = '';
    }

    document.querySelectorAll('.user-list-item').forEach(li => {
        li.onclick = () => {
            if (username < li.innerHTML) {
                newRoom = `${username}_${li.innerHTML}`;
            }
            else {
                newRoom = `${li.innerHTML}_${username}`;
            }
            msg = {
                'sender': username,
                'receiver': li.innerHTML,
                'room': newRoom
            };

            leaveRoom(roomName);
            joinRoom(newRoom);
            console.log(`Joining room ${newRoom}`);
            roomName = newRoom;
            document.querySelector('#room-name').innerHTML = li.innerHTML;
            socket.emit('make_new_room', JSON.stringify(msg));
        }

    })

    socket.on('load_history', (msgHistory) => {
        msgHistory = JSON.parse(msgHistory);
        for (msgKey in msgHistory) {
            if (msgKey === '0') {
                continue;
            }
            else if (msgKey === '1') {
                if (roomName === msgHistory[msgKey]['room']) {
                    // Correct case, continue
                    if (document.querySelector('#messages-list').childElementCount === 1) {
                        // Load history
                        console.log('Chatroom just opened, load history');
                    }
                    else {
                        // History is already present
                        console.log(`History already present, don't load history`);
                        return;
                    }
                }
                else {
                    // Incorrect
                    console.log('History received was not of current room')
                    break;
                }
            }
            let msgDisplay = document.createElement('h4');
            msgDisplay.innerHTML = msgHistory[msgKey]['content'];
            let timestamp = document.createElement('h6');
            timestamp = msgHistory[msgKey]['timestamp'];
            let listItem = document.createElement('div');
            listItem.appendChild(msgDisplay);
            document.getElementById('messages-list').appendChild(listItem);

            if (msgHistory[msgKey]['sender'] === username) {
                listItem.classList.add('meActivity');
            }
            // 
            else {
                listItem.classList.add('themActivity');
            }

        }
        scrollDownChatWindow();
    });

    function scrollDownChatWindow() {
        const chatWindow = document.querySelector("#rightid");
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }
});
