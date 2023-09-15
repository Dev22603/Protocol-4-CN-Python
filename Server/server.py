# import socket
# import pickle
# import time
# from frame import Frame



# def server():
#     # Define constants
#     MAX_SEQ = 1
#     FRAME_SIZE = 1024
#     FORMAT='utf-8'
#     # HEADER=64
#     PORT = 5050
#     SERVER=socket.gethostbyname(socket.gethostname())
#     ADDR=(SERVER,PORT)
#     # print(SERVER)
#     # DISCONNECT_MESSAGE= "!DISCONNECT"
#     server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     server.bind(ADDR)
#     server.listen()
#     print(f"Server is listening at {SERVER} ")
#     conn,addr=server.accept()
#     send_file=open("server_send.txt",'r')
#     receive_file=open("server_receive.txt",'a')

#     data=send_file.read()
#     data_list=data.split()



#     next_frame_to_send = 0
#     frame_expected = 0
#     i=0
#     # conn.send("fdsasdf".encode(FORMAT))
#     while i<len(data_list):
#         frame1=Frame(next_frame_to_send, 1 - frame_expected, data_list[i])
#         pickled_frame1=pickle.dumps(frame1)
#         conn.send(pickled_frame1)
#         print(pickle.loads(frame1))
#         i+=1


#     send_file.close()
#     receive_file.close()




# server()

































import socket
import pickle
import time
from .frame import Frame
import threading



def server():
    # Define constants
    MAX_SEQ = 1
    FRAME_SIZE = 1024
    FORMAT='utf-8'
    # HEADER=64
    PORT = 5050
    SERVER=socket.gethostbyname(socket.gethostname())
    ADDR=(SERVER,PORT)
    # print(SERVER)
    # DISCONNECT_MESSAGE= "!DISCONNECT"
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"Server is listening at {SERVER} ")
    conn,addr=server.accept()
    send_file=open("D:\College\B.Tech 3rd Year\Sem 5\CN\LAB\Practical_4\Python\Approach_3\Server\server_send.txt",'r')
    receive_file=open("D:\College\B.Tech 3rd Year\Sem 5\CN\LAB\Practical_4\Python\Approach_3\Server\server_receive.txt",'a')

    data=send_file.read()
    data_list=data.split()



    next_frame_to_send = 0
    frame_expected = 0
    i=0
    # conn.send("fdsasdf".encode(FORMAT))
    while i<len(data_list):
        frame1=Frame(next_frame_to_send, 1 - frame_expected, data_list[i])
        pickled_frame1=pickle.dumps(frame1)
        conn.send(pickled_frame1)
        print("Sending data frame: ",pickle.loads(pickled_frame1).data)
        time.sleep(1)
        ack_received = False
        while not ack_received:
            conn.settimeout(5)
            # server.settimeout(5)
            try:
                # ack_packet, addr = server.recvfrom(FRAME_SIZE)
                ack_packet = conn.recv(FRAME_SIZE)
                ack = pickle.loads(ack_packet)
                # print(ack.seq,ack.ack,ack.data)
                if ack.seq == next_frame_to_send:
                    ack_received = True
                    next_frame_to_send = (next_frame_to_send + 1) % (MAX_SEQ + 1)
                    print(f"Acknowledgment received for sequence {ack.seq}")
                    receive_file.write(ack.data+" ")    # modification for writing to 
                    i+=1
            except socket.timeout:
                print("Timeout. Resending...")
    server.close()
    send_file.close()
    receive_file.close()


# server()


