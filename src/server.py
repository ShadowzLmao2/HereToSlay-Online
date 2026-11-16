import time
import struct
import threading
import socket

class Server:
    #List of port numbers https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers
    #Anything between 49152-65535 should be fine
    def __init__(self, host='127.0.0.1', port = 65534):
        self.host = host
        self.port = port

        self.kill = False
        self.thread_count = 0

    def connection_listen_loop(self):
        self.thread_count += 1
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        self.thread_count -= 1

    def run(self):
        try:
            while True:
                time.sleep(0.05)
        except KeyboardInterrupt:
            pass

Server().run()