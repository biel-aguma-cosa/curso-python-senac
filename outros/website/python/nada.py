import asyncio
import json
import os
import websockets

dir = os.path.dirname(os.path.realpath(__file__))


def data_read():
    global dir
    with open(os.path.join(dir,'socket_data.json'),'r') as file:
        data = json.load(file)
        file.close()
    return data
def data_write(raw_data,target):
    global dir
    data = data_read()
    if target == 'users':
        data['users'][raw_data['index']] = raw_data['data']
    elif target == 'messages':
        data['messages'].append(raw_data['data'])
    
    with open(os.path.join(dir,'socket_data.json'),'w') as file:
        dump_data = json.dumps(data,indent=3)
        file.write(dump_data)
        file.close()
        

async def conn_handler(socket):
    print('[client connected]')
    try:
        async for message in socket:
            data = json.loads(message)
            match data['type']:
                case 'login':
                    if data['user']['username'] in data_read()['users']:
                        if data['user']['password'] == data_read()['users'][data['user']['username']]['password']:
                            await socket.send(json.dumps({
                                'type':'login',
                                'username':data['user']['username'],
                                'result': 'login'
                            }))
                    else:
                        data_write({
                            'data' : data['user'],
                            'index' : data['user']['username'],
                        },'users')
                        await socket.send(json.dumps({
                                'type':'login',
                                'username':data['user']['username'],
                                'result': 'register'
                            }))
                case 'message':
                    pass
                case 'reload':
                    await socket.send(json.dumps({
                                'type':'login',
                                'username':data['user']['username']
                            }))
                case 'update':
                    pass

    except websockets.ConnectionClosed:
        print("[connection closed]")
    finally:
        await socket.close()


async def main():
    async with websockets.serve(conn_handler,'localhost',55555):
        print('[server started]')
        await asyncio.Future()
asyncio.run(main())