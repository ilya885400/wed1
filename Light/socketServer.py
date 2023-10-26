import socket
from tkinter import *
import threading
from Lamp import tkloop, toggle_image


def serverloop():
    turn = b"0"

    while True:  # принимаем входящее подключение
    # conn - клинетский соккет
    # addr - адрес клиента
        conn, addr = s.accept()  # принимаем входящее подключение от какого-либо клиента

        if turn == b"1":
            # res = b'Button_on'  # Поменять на on
            turn = b"0"
        else:
            # res = b'Button_off'  # поменять на off
            turn = b"1"
        conn.send(turn)  #
        toggle_image()


ip = input('ip: ')
port = int(input('port: '))




HOST = (ip, port)  # (Значение хоста(локальный хост), порт))
# если есть IP сервера юзать его

# (Ip адрес,TCP отвечающее за порт)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# создание endpoint'а на серверной части
# пишем сервер
# чтобы не было проблем с пересоздание сервера (проблема с timeout'ом)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(HOST)  # связка IP/порта с EndPoint'ом

s.listen()  # ставим серверный сокет на прослушку, чтобы он ожидал входящее TCP подключение

thr = threading.Thread(target=serverloop)
thr.daemon = True
thr.start()
tkloop()