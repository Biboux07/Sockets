import socket
import time
import struct

#udp protocole
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

IP = socket.gethostname()
PORT = 12345
s.bind((IP, PORT))

BUFFER_SIZE = 4096
#Recevoir l'unique connection du client:
data, address = s.recvfrom(BUFFER_SIZE)
print(f"Connection from", address, "has been established!")
print(str(data))

#envoit au client de l'unique message du serveur: 
msg = (bytes("I am an UDP server!","utf-8"))
s.sendto(msg, address)

#Récupération des données "Télémétriques" + affichage
while True:
    data_pack, adresse = s.recvfrom(BUFFER_SIZE)
    data_unpack = struct.unpack('f', data_pack)
    print("Data pack:",data_pack)
    print("Data unpack:",data_unpack)
