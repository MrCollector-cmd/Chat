from base64 import encode
import encodings
import socket

host = "localhost"
port = 5656

obSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

obSocket.connect((host, port))
print("cliente iniciando")

while True:
    enviar = input("cliente:")
    obSocket.send(enviar.encode(encoding="ascii", errors = "ignore"))
    recibido = obSocket.recv(1024)
    print("servidor: ", recibido.decode(encoding="ascii", errors= "ignore"))

obSocket.close()