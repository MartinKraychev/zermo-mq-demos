import zmq

context = zmq.Context()
server_rep = context.socket(zmq.REP)
server_rep.bind("tcp://*:5558")

server_pub = context.socket(zmq.PUB)
server_pub.bind("tcp://*:5559")
print('Server is running...')

while True:

    #  Wait for next request from client
    message = server_rep.recv()
    print(f"Received request: {message.decode()}")

    server_pub.send_string(f'123 {message}')
