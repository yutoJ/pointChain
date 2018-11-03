import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

my_socket.connect(('127.0.0.1', 50030))
my_text = "Hello, this is sample"
my_socket.sendall(my_text.encode('utf-8'))