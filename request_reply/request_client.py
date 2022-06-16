import threading

import zmq


def send():
    while True:
        input_message = input()
        req_socket.send_string(input_message)


def receive():
    while True:
        message = sub_socket.recv_string()
        print(message)


if __name__ == '__main__':
    context = zmq.Context()
    print("Connecting to server...")
    req_socket = context.socket(zmq.REQ)
    req_socket.connect("tcp://localhost:5558")

    sub_socket = context.socket(zmq.SUB)
    sub_socket.connect("tcp://localhost:5559")
    sub_socket.setsockopt_string(zmq.SUBSCRIBE, '123')

    send_thread = threading.Thread(target=send)
    send_thread.start()

    receive_thread = threading.Thread(target=receive)
    receive_thread.start()
