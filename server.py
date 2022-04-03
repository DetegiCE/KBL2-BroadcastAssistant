from websocket_server import WebsocketServer

def new_client(client, server):
    print('Client connected')

def on_message(client, server, message):
    server.send_message_to_all(message)

print('Running')

server = WebsocketServer(port=2589, host='127.0.0.1')
server.set_fn_new_client(new_client)
server.set_fn_message_received(on_message)
server.run_forever()
