from concurrent.futures import ThreadPoolExecutor
import socket
import os

def __handle_message(args_tuple):

    conn, addr, data_sum = args_tuple
    print('args_tuple')
    print(args_tuple)
    print(conn)
    while True:
        data = conn.recv(1024)
        data_sum = data_sum + data.decode('utf-8')

        if not data:
            break
    print('data_sum')
    print(data_sum)
    if data_sum != '':
        print(data_sum)

def __get_myip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    return s.getsockname()[0]

def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    executor = ThreadPoolExecutor(max_workers=os.cpu_count())

    myhost = __get_myip()
    print('my ip address is now ...', myhost)
    my_socket.bind((myhost, 50030))

    my_socket.listen(1)

    while True:
        print('Waiting for the connction ...')
        conn, addr = my_socket.accept()
        print("Connected by ..", addr)
        data_sum = ''
        executor.submit(__handle_message, (conn, addr, data_sum))

if __name__ == '__main__':
    main()