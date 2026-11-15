import time
import struct
import threading
import socket

class Server:
    #List of port numbers https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers
    #Anything between 49152-65535 should be fine
    def __init__(self, host='127.0.0.1', port = 65534):
        pass