import pygame, socket, json, threading, copy

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('10.144.36.139',52007))

def cook(arg=None,**kwargs):
    if arg:
        data = json.dumps(arg   )+'\n'
    else:
        data = json.dumps(kwargs)+'\n'
    return data.encode()
def send(arg=None,**kwargs):
    if arg:
        data = json.dumps(arg   )+'\n'
    else:
        data = json.dumps(kwargs)+'\n'
    client.send(data.encode())
def uncook(data):
    return json.loads(data.decode())

direction = [0,0]
SCREEN = (600,400)
index = 0
offset = [0,0]
COLOR = None
self = None

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

send(type='valid')
beep = uncook(client.recv(1024))
print(f'beep: {beep}')
print('VALID COLORS:')
for color in beep['colors']:
    del colors[color]
for color in colors:
    print(f' - {colors[color]} | index: {color}')
COLOR = input('select color index: ')
send(type='enter',color=COLOR)

running = True
clock = pygame.Clock()
dt = 0 

pygame.init()
screen = pygame.display.set_mode(SCREEN)

players = []
#(list[player]['pos'],list[player]['angle'],list[player]['color']

def handler():
    global client, running, COLOR, index, players
    buffer = ''
    while running:
        raw_data = client.recv(1024).decode()
        buffer += raw_data
        while '\n' in buffer:
            string_data, buffer = buffer.split('\n',1)
            if string_data:
                data = json.loads(string_data)
                if data:
                    match data['type']:
                        case 'physics':
                            if COLOR:
                                with lock:
                                    players = data['data']
                                    for i, player in enumerate(players):
                                        if player[2] == COLOR:
                                            index = i
                        case _:
                            pass
def send_direction():
    global direction, running
    while running:
        send(type='move',dir=direction)
        pygame.time.delay(int(1000/15))

key_translate = {
    True  : {True: 0,False:-1},
    False : {True: 1,False: 0}
}

lock = threading.Lock()
handler_thread   = threading.Thread(target=handler  )
direction_thread = threading.Thread(target=send_direction)
handler_thread  .start()
direction_thread.start()

while running:
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(pygame.color.Color(70,30,30))


    direction = [key_translate[key[pygame.K_a]][key[pygame.K_d]],key_translate[key[pygame.K_w]][key[pygame.K_s]]]

    with lock:
        current_players = players.copy()

    for player in current_players:
        try:
            pygame.draw.rect(screen,color=colors[player[2]],rect=pygame.Rect(player[0][0],player[0][1],16,16))
        except:
            print(player)
    
    pygame.display.flip()
    dt = clock.tick(30)/1000
handler_thread  .join()
direction_thread.join()
print('Client Ended')