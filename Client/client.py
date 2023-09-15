import socket
import pickle
import time
import threading
from .frame import Frame
# Define constants
MAX_SEQ = 1
FRAME_SIZE = 1024
HEADER = 64
PORT = 5050


def receiver():

    SERVER = socket.gethostbyname(socket.gethostname())
    ADDR = (SERVER, PORT)
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = "!DISCONNECT"

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    frame_expected = 0
    # while True:
    #     data_packet, addr = receiver_socket.recvfrom(FRAME_SIZE)
    #     packet = pickle.loads(data_packet)

    #     if packet.seq == frame_expected:
    #         print(f"Received: {packet.data}")
    #         ack = Packet(frame_expected, packet.seq, "")
    #         receiver_socket.sendto(pickle.dumps(ack), ('localhost', 12345))
    #         frame_expected = (frame_expected + 1) % (MAX_SEQ + 1)
    # send_file = open("client_send.txt", 'r')
    # send_file = open("D:\College\B.Tech 3rd Year\Sem 5\CN\LAB\Practical_4\Python\Approach_3\Client\client_send.txt", 'a')
    while True:
        receive_file = open("D:\College\B.Tech 3rd Year\Sem 5\CN\LAB\Practical_4\Python\Approach_3\Client\client_receive.txt", 'a')
        receive_pickled = client.recv(1024)
        if receive_pickled:
            receive = pickle.loads(receive_pickled)
        else:
            break
        if receive.seq == frame_expected:
            print(f"Received: {receive.data}")
            receive_file.write(receive.data+" ")
            receive_file.close()
            ack = Frame(frame_expected, receive.seq, "")
            client.send(pickle.dumps(ack))
            # print(pickle.dumps(ack))
            frame_expected = (frame_expected + 1) % (MAX_SEQ + 1)
            time.sleep(1)





# receiver_thread = threading.Thread(target=receiver)
# receiver_thread.start()

# receiver()