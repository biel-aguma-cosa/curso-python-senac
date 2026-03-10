const sock = {
    'text_field' : document.getElementById('sock_field'),
    'entry_field': document.getElementById('sock_text')
}
const targets = {
        "slider" : {
            "K" : document.getElementById('K_slider'),
            "F" : document.getElementById('F_slider'),
            "C" : document.getElementById('C_slider')
        },
        "num" : {
            'K': document.getElementById('K_num'),
            'F': document.getElementById('F_num'),
            'C': document.getElementById('C_num')
        },
        "index" : {
            'C': 0,
            'K': 1,
            'F': 2
        }
    }
const temp_vals = {
        "K" : 0,
        "F" : 0,
        "C" : 0
    }
const dummy = ['C','K','F'];
        

function open_tab(event,tab) {
    let i, tab_content, tab_buttons
    tab_content = document.getElementsByClassName('content');
    tab_buttons = document.getElementsByClassName('tab_b');
    let target = document.getElementById(tab);
    let button = event.currentTarget
    
    for (i=0; (i < tab_content.length) && (i < tab_content.length); i++) {
        tab_content[i].style.display = 'none';
        tab_buttons[i].className = tab_buttons[i].className.replace(' active','')
    };
    target.style.display = 'block'
    button.className += ' active'
}
function temperature(type,index) {
    switch (index) {
        case 0:
            temp_vals.C = Number(targets[type].C.value)
            temp_vals.K = Math.round(temp_vals.C + 273.15)
            temp_vals.F = Math.round(temp_vals.C * 9/5 + 32)
            break
        case 1:
            temp_vals.K = Number(targets[type].K.value)
            temp_vals.C = Math.round(temp_vals.K - 273.15)
            temp_vals.F = Math.round((temp_vals.C * 1.8) + 32)
            break
        case 2:
            temp_vals.F = Number(targets[type].F.value)
            temp_vals.C = Math.round((temp_vals.F - 32)*5/9)
            temp_vals.K = Math.round(temp_vals.C + 273.15)
            break
    }
    for (let i of dummy) {
        targets.num[i].value = temp_vals[i]
        targets.slider[i].value = temp_vals[i]
    }
}
function message(data,type,sender) {
    let _div = document.createElement('div')
    let text = document.createElement('p')
    let user = document.createElement('p')
    _div.style.height = '15px'
    div.className = 'bubble'+type
    user.innerText = sender
    user.className = 'username'+type
    text.innerText = data
    div.appendChild(text)
    _div.appendChild(user)
    
    text_field.appendChild(div)
    text_field.appendChild(_div)
}
function speak() {
    let entry = sock.entry.value
    if (user_data.username && user_data.password) {
        socket.send(JSON.stringify(
            {
                type : 'message',
                message : entry,
                user_data : user_data
            }
        ))
    }
}

function login() {
    const socket = new WebSocket("ws://localhost:55555")

    socket.onopen = function () {
        socket.send(JSON.stringify(
            {
                'type' : 'login',
                'user' : user_data
            }
        ))
    }
    socket.onmessage = function (event) {
        const data = JSON.parse(event.data)
        switch (data.type) {
            case 'message':
                if (data.username != username) {
                    message(data.message,' server',data.username)
                }
                break
            case 'reload':
                for (let child of sock.text_field.childNodes) {
                    child.remove()
                }
                for (let text of data.messages) {
                    if (text.sender != username) {
                        message(text.message,'',text.sender)
                    }
                }
                break
            case 'accepted':
                sock.entry_field.value = ''
                message(data.message,'',sender)
                break
            case 'login':
                if (data.username == username) {
                    message(
                        username+' entrou',
                        '',
                        username)
                }else{
                    message(
                        data.username+' entrou',
                        ' server',
                        data.username)
                }
                break
        }
    }
}

function login_submission_handler(event) {
    event.preventDefault()
    const data = new FormData(event.target)
    user = {
        'username' : data.get('username'),
        'password': data.get('password')
    }

    login()
}

function main() {
    const user_data = {
        'username' : null,
        'password' : null
    }

    const socket_tab = document.getElementById('socket_tab')
    const form = document.getElementById('login_form');

    document.getElementById('default').click()

    form.addEventListener('submit',login_submission_handler)


    document.addEventListener('keydown', function (event) {
        if (event.key == 'Enter') {
            if (socket_tab.className.includes('active')) {speak()}
        }
    })
}