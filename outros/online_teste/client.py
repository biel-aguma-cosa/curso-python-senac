import pygame, socket, json, threading

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('localhost',52007))

def cook(arg=None,**kwargs):
    if arg:
        return json.dumps(arg).encode() + b'\n'
    else:
        return json.dumps(kwargs).encode() + b'\n'
def send(arg=None,**kwargs):
    if arg:
        data = json.dumps(arg).encode() + b'\n'
    else:
        data = json.dumps(kwargs).encode() + b'\n'
    client.send(data)
def uncook(data):
    return json.loads(data.decode().strip())

SCREEN = (600,400)
INDEX = 0
OFFSET = [0,0]
COLOR = None
SELF = None

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
color = input('select color index: ')
send(type='enter',color=color)

running = True
clock = pygame.Clock()
dt = 0

pygame.init()
screen = pygame.display.set_mode(SCREEN)

players = []
#(list[player]['pos'],list[player]['angle'],list[player]['color']

def handler():
    global client, running
    while running:
        raw_data = client.recv(1024).decode().strip()
        buffer += raw_data
        while '\n' in buffer:
            string_data, buffer = buffer.split('\n',1)
            if string_data:
                data = json.loads(string_data)
                print(data)
                match data['type']:
                    case 'players':
                        if COLOR:
                            players = data['data']
                            for i, player in enumerate(players):
                                if player[2] == COLOR:
                                    INDEX = i
                    case _:
                        pass

key_translate = {
    True  : {True: 0,False:-1},
    False : {True: 1,False: 0}
}

threading.Thread(target=handler).start()

while running:
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(pygame.color.Color(70,30,30))


    direction = [key_translate[key[pygame.K_a]][key[pygame.K_d]],key_translate[key[pygame.K_w]][key[pygame.K_s]]]
    send(type='move',dir=direction)


    for player in players:
        pygame.draw.rect(screen,player[2],pygame.Rect(player[0][0],player[0][1],16,16))
    
    pygame.display.flip()
    dt = clock.tick(30)/1000