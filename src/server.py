import time
import struct
import threading
import socket
import pygame

class Server:
    #List of port numbers https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers
    #Anything between 49152-65535 should be fine
    def __init__(self, host='127.0.0.1', port = 65534):
        self.host = host
        self.port = port

        self.kill = False
        self.thread_count = 0
        self.players = []

    def connection_listen_loop(self):
        self.thread_count += 1
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
            s.bind((self.host,self.port))

            while not self.kill:
                s.settimeout(1)
                s.listen()
                try:
                    conn, addr = s.accept() #returns tuple
                    print(f"New Connection: {conn}, {addr}")
                    if len(self.players) < 2:
                        self.players.append(conn)
                        #spawn listener task
                except socket.timeout:
                    continue
                time.sleep(0.01)
        self.thread_count -= 1

    def await_kill(self): #Ends the server
        self.kill = True
        while self.thread_count: #Waits for threads to automatically end
            time.sleep(0.01)
        print("Server killed")

    def run_listener(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
            s.connect((self.host, self.port))
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, True)


    def run(self):
        threading.thread(target=self.connection_listen_loop).start() #Starts looking for players to join
        try:
            while True:
                time.sleep(0.05)
        except KeyboardInterrupt:
            self.await_kill()
            pass

Server().run()