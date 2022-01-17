import socket

host = "localhost"
port = 5656

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.bind((host, port))
servidor.listen(1)
print("server en espera")

active, addr= servidor.accept()

while True:
    recibido = active.recv(1024)
    print("cliente: ", recibido.decode(encoding = "ascii", errors = "ignore"))
    enviar = input("server: ")
    active.send(enviar.encode(encoding = "ascii", errors = "ignore"))

active.close()