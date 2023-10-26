import socket
def recieve(ip, port):
    HOST = (ip, port)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(HOST)  # коннект к серверу от созданного клиентского соккета
    msg = client.recv(1024)
    client.close()



# print('Connected to ', HOST)

# получаем данные от сервера (1024 байта - размер данного буфера)