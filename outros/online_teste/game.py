import socket, pygame, math, threading, json, time

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('localhost',55555))

clients = []

objects = []

colors = {
    '000' : 'black',
    '001' : 'blue',
    '010' : 'green',
    '011' : 'cyan',
    '100' : 'red',
    '101' : 'magenta',
    '110' : 'yellow',
    '111' : 'white'
}

players = {
}

def broadcast(data):
    if clients != []:
        for client in clients.copy():
            client.send(json.dumps(data).encode())

def physics():
    pass

def valid_colors(client):
    invalids = []
    check = players.copy()
    for player in check:
        invalids.append(check['player']['color'])
    data = json.dumps({'type':'valid','colors':invalids})
    client.send(data.encode())

def move(address,data):
    players[address]['dir'] = data['dir']

def shoot(address,data):
    pass

def enter_game(address,data):
    invalids = []
    check = players.copy()
    for player in check:
        invalids.append(check['player']['color'])
    if data['color'] in colors and not (data['color'] in invalids):
        players[address] = {
            'rect' : pygame.rect.Rect(0,0,16,16),
            'dir'  : (0,0),
            'angle': 0,
            'color': data['color'],
        }

def handler(client,address):
    while True:
        try:
            thread = None
            string_data = server.recv(1024).decode()
            if string_data:
                data = json.loads(string_data)
                match data['type']:
                    case 'valid':
                        thread = threading.Thread(target=valid_colors,args=[client])
                    case 'move':
                        thread = threading.Thread(target=move,args=[address,data])
                    case 'shoot':
                        thread = threading.Thread(target=shoot,args=[address,data])
                    case 'enter':
                        thread = threading.Thread(target=enter_game,args=[address,data])
                thread.start() if thread else print(end='')
        except:
            try: clients.remove(client)
            except: pass
            try: del players[address]
            except: pass
            


server.listen(8)

while True:
    client, address = server.accept()
    thread = threading.Thread(target=handler,args=[client,address])
    thread.start()

