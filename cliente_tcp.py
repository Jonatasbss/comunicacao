from socket import *

servidor = "127.0.0.1" #localhost
porta = 43210

msg = bytes(input("Digite algo: "), "utf-8")
#Criar o objeto socket, recebendo o tipo de identificação com servidor e recebendo a informação para trabalhar com o protocolo tcp
obj_socket = socket(AF_INET, SOCK_STREAM)
#Setar o servidor e porta de entrada.
obj_socket.connect((servidor, porta))
obj_socket.send(msg)
resposta = obj_socket.recv(1024)
print("Recebemos: ", resposta)
obj_socket.close()