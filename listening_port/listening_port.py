"""
A module to check if a listening port is open on an ipaddr

"""

import socket


def is_listening_port(ipaddr:str, port:int)-> bool:
    """
    Check a listening port is open on an ipaddr return boolean if open or not

    :param ipaddr: The ipaddr to check
    :param port: The port number to check
    :return: Boolean True if port is open, False otherwise
    """
    """
    Check a listening port is open on an ipaddr return boolean if open or not

    :param ipaddr: The ipaddr to check (str)
    :param port: The port number to check (int)
    :return: Boolean (bool) True if port is open, False otherwise
    """
    s:socket = socket.socket(family=socket.AF_INET,type= socket.SOCK_STREAM)
    try:
        s.connect((ipaddr, port))
        s.shutdown(2)
        return True
    except socket.error:
        return False
