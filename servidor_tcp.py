from socket import *

servidor = "127.0.0.1" #localhost
porta = 43210

#Criar o objeto socket, recebendo o tipo de identificação com servidor e recebendo a informação para trabalhar com o protocolo tcp
obj_socket = socket(AF_INET, SOCK_STREAM)

#Setar o servidor e porta de entrada.
obj_socket.bind((servidor,porta))

#Quantidade de clientes que seram atendidos.
obj_socket.listen(2)

print("Aguardando cliente....")

while True:
    con, cliente = obj_socket.accept()
    print("Conectado com: ", cliente)
    while True:
        msg_recebida = str(con.recv(1024))
        print("Recebemos: ", msg_recebida)
        msg_enviada = b'Ola Cliente'
        con.send(msg_enviada)
        break
    con.close()
