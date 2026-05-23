import socket

def is_listening(host: str, port: int) -> bool:
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
        s.settimeout(5)
        result = s.connect_ex((host, port))
        return result == 0
