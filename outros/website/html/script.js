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
    const dummy = ['K','F','C']
    switch (index) {
        case 0:
            globalThis.temp_vals.C = Number(globalThis.targets[type].C.value)
            globalThis.temp_vals.K = globalThis.temp_vals.C + 273.15  
            globalThis.temp_vals.F = globalThis.temp_vals.C * 9/5 + 32
            break
        case 1:
            globalThis.temp_vals.K = Number(globalThis.targets[type].K.value)
            globalThis.temp_vals.C = globalThis.temp_vals.K - 273.15    
            globalThis.temp_vals.F = (globalThis.temp_vals.C * 1.8) + 32
            break
        case 2:
            globalThis.temp_vals.F = Number(globalThis.targets[type].F.value)
            globalThis.temp_vals.C = (globalThis.temp_vals.F - 32)*5/9
            globalThis.temp_vals.K = globalThis.temp_vals.C + 273.15  
            break
    }
    for (let i of dummy) {
        globalThis.targets.num[i].value    = parseFloat(globalThis.temp_vals[i]).toFixed(2)
        globalThis.targets.slider[i].value = parseFloat(globalThis.temp_vals[i]).toFixed(2)
    }
}
function message(data,type,sender) {
    let _div = document.createElement('div')
    let div = document.createElement('div')
    let text = document.createElement('p')
    let user = document.createElement('p')

    _div.style.backgroundColor = 'rgba(102, 127, 207, 0.48)'
    div.className = 'bubble'+type
    user.className = 'user'+type

    user.innerText = sender
    text.innerText = data

    div.appendChild(text)
    _div.appendChild(user)
    
    globalThis.sock.text_field.appendChild(_div)
    globalThis.sock.text_field.appendChild(div)
}
function speak() {
    let entry = globalThis.sock.entry_field.value

    if (
        globalThis.user.name &&
        globalThis.user.password &&
        globalThis.socket.readyState == WebSocket.OPEN
    ) {
        globalThis.socket.send(JSON.stringify(
            {
                'type' : 'message',
                'message' : entry,
                'user' : globalThis.user
            }
        ))
    }
}

function message_handler(data) {
        switch (data.type) {
            case 'message':
                if (data.sender == globalThis.user.name) {
                    message(
                        data.message,
                        '',
                        data.sender
                    )
                }else{
                    message(
                        data.message,
                        ' server',
                        data.sender
                    )
                }
                break
            case 'login':
                globalThis.user.name     = data.user.name
                globalThis.user.password = data.user.password
                for (let msg of data.data) {
                    if (msg.sender == globalThis.user.name) {
                        message(
                            msg.message,
                            '',
                            msg.sender
                        )}else{
                        message(
                            msg.message,
                            ' server',
                            msg.sender
                        )}}
                break
            case 'error':
                message('ERRO!',' server','server')
            default:
                break
        }
}

function login() {
    globalThis.socket = new WebSocket("ws://192.168.1.4:52007")

    console.log(globalThis.user)
    globalThis.socket.onopen = function () {
        globalThis.socket.send(JSON.stringify(
            {
                'type' : 'login',
                'user' : globalThis.user
            }
        ))
    }
    globalThis.socket.onmessage = function (event) {
        console.log('message received!')
        const reader = new FileReader()

        reader.onload = function () {
            message_handler(JSON.parse(reader.result))
        }
        reader.readAsText(event.data)
        
    }
}

function login_submission_handler(event) {
    event.preventDefault()
    const data = new FormData(event.target)
    globalThis.user = {
        'name' : data.get('username'),
        'password': data.get('password')
    }

    login()
}

function main() {
    globalThis.reader = new FileReader()

    globalThis.targets = {
        "slider" : {
            "K" : document.getElementById('K_slider'),
            "F" : document.getElementById('F_slider'),
            "C" : document.getElementById('C_slider')},
        "num" : {
            'K': document.getElementById('K_num'),
            'F': document.getElementById('F_num'),
            'C': document.getElementById('C_num')},
        "index" : {
            'C': 0,
            'K': 1,
            'F': 2}}
    globalThis.sock = {'text_field' : document.getElementById('sock_field'),    'entry_field': document.getElementById('sock_text')}

    globalThis.temp_vals = {"K" : 0,        "F" : 0,        "C" : 0    }
    globalThis.dummy = ['C','K','F'];
    globalThis.user = {'name' : null,'password' : null}

    globalThis.socket_tab = document.getElementById('socket_tab')
    globalThis.form = document.getElementById('login_form');

    document.getElementById('default').click()

    form.addEventListener('submit',login_submission_handler)

    document.addEventListener('keydown', function (event) {
        if (event.key == 'Enter') {
            if (socket_tab.className.includes('active')) {speak()}
        }
    })
}