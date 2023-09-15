import socket
import pickle
import time
from Server import frame
import threading
from Client.client import receiver
from Server.server import server



server_thread=threading.Thread(target=server)
receiver_thread=threading.Thread(target=receiver)
server_thread.start()
receiver_thread.start()
server_thread.join()
receiver_thread.join()