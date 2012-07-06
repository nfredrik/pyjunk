import asyncore
import logging
import socket

from asynchat_echo_handler import EchoHandler

class EchoServer(asyncore.dispatcher):
    """Receives connections and establishes handlers for each client.
    """
    
    def __init__(self, address):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind(address)
        self.ip, self.port = self.socket.getsockname()
        self.listen(1)
        return
    
    def get_ip(self):
        return self.ip
    
    def get_port(self):
        return self.port

    def handle_accept(self):
        # Called when a client connects to our socket
        #client_info = self.accept()
        socket, remoteaddr = self.accept()
        #EchoHandler(sock=client_info[0])
        EchoHandler(sock=socket)
        # We only want to deal with one client at a time,
        # so close as soon as we set up the handler.
        # Normally you would not do this and the server
        # would run forever or until it received instructions
        # to stop.
        self.handle_close()
        return
    
    def handle_close(self):
        self.close()