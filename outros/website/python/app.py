import websockets
import asyncio
import json

#server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#server.bind(('10.12.156.183',55555))
#
#print(f'HOST NAME: {socket.gethostname()}')

async def broadcast(dict):
    global clients
    if len(clients):
        for client in clients.copy():
            try:
                data = json.dumps(dict).encode()
                await client.send(data)
                print(f'[data [{data}] broadcasted]')
            except websockets.ConnectionClosed:
                pass
async def send(client,dict):
    try:
        data = json.dumps(dict).encode()
        await client.send(data)
        print(f'[data [{data}] sent]')
    except websockets.ConnectionClosed:
        pass

async def handler(socket):
    global clients, client_data, all_data, public_data
    logged = False
    while True:
        try:
            do_broadcast = False
            async for _rdata in socket:
                rdata = json.loads(_rdata)
                for thing in rdata:
                    print(thing,':',rdata[thing])
                match rdata['type']:
                    case 'login':
                        if rdata['user']['name'] in client_data:
                            if rdata['user']['password'] == client_data[rdata['user']['name']]['password']:
                                logged = True
                            else:
                                data = {'type':'error'}
                        else:
                            client_data[rdata['user']['name']] = rdata['user']
                            logged = True
                        if logged:
                            data = {'type':'login','user':rdata['user'],'data':public_data}
                            await send(socket,data)
                            socket_data[socket] = rdata['user']
                            if socket not in clients:
                                    clients.add(socket)
                            data = {'type':'message','sender':rdata['user']['name'],'message':f'{rdata['user']['name']} logged in'}
                            do_broadcast = True
                                            
                            socket_data[socket] = rdata['user']
                    case 'message':
                        if rdata['user']['name'] in client_data:
                            if rdata['user']['password'] == client_data[rdata['user']['name']]['password']:
                                data = {'type':'message','sender':rdata['user']['name'],'message':rdata['message']}
                                do_broadcast = True
                    case _:
                        data = {'type':'error'}
                all_data.append(data)
                if do_broadcast:
                    public_data.append(data)
                    await broadcast(data)
                else:
                    await send(socket,data)
        except websockets.ConnectionClosed:
            if socket in clients:
                clients.remove(socket)
                data = {'type':'message','sender':'server','message':f'{socket_data[socket]['name']} desconectou-se'}
                await broadcast(data)
            break
async def main():
    global clients, client_data, public_data, all_data, socket_data

    clients = set()
    socket_data = {}
    client_data = {}
    public_data = []
    all_data = []

    async with websockets.serve(handler,'192.168.1.4',52007):
            print('[server started]')
            await asyncio.Future()

asyncio.run(main())

