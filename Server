import socket

HOST = ('192.168.43.18', 10000)  # (Значение хоста(локальный хост), порт))
# если есть IP сервера юзать его

# (Ip адрес,TCP отвечающее за порт)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# создание endpoint'а на серверной части
# пишем сервер
# чтобы не было проблем с пересоздание сервера (проблема с timeout'ом)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(HOST)  # связка IP/порта с EndPoint'ом

s.listen()  # ставим серверный сокет на прослушку, чтобы он ожидал входящее TCP подключение

turn = False


while True:  # принимаем входящее подключение
    # conn - клинетский соккет
    # addr - адрес клиента
    conn, addr = s.accept()  # принимаем входящее подключение от какого-либо клиента
    if turn:
        print("Лампа горит!")
    else:
        print("Лампа не горит")

    if turn:
        res = b'Button_on'  # тут хранится byte строка
        turn = False
    else:
        res = b'Button_off'
        turn = True
    conn.send(res)  # отправляем данные клиенту
