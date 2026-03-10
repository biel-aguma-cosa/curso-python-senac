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
def data_write(data,target):
    global dir
    file = data_read()
    file[target][data['index']]

print(data_read())

async def conn_handler(socket):
    print('[client connected]')
    try:
        async for message in socket:
            print(message)
            if message.lower() == 'stop':
                return
            await socket.send('ping')
    except websockets.ConnectionClosed:
        print("[connection closed]")
    finally:
        await socket.close()


async def main():
    async with websockets.serve(conn_handler,'localhost',55555):
        print('[server started]')
        await asyncio.Future()
asyncio.run(main())