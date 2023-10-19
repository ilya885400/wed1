import socket

HOST = ('192.168.43.18', 10000)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(HOST)  # коннект к серверу от созданного клиентского соккета

# print('Connected to ', HOST)

# получаем данные от сервера (1024 байта - размер данного буфера)
msg = client.recv(1024)

print(msg.decode('UTF-8'))
