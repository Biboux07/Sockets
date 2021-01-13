import socket
import time
import struct

#Connection UDP protocole
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

msg = (bytes("Hi Server, I'm a connected Client", "utf-8"))

#envoit du msg de connection au serveur:
IP = socket.gethostname()
PORT = 12345
s.sendto((msg), (IP, PORT))


#Recevoir l'unique réponse:
BUFFER_SIZE = 4096
data, adresse = s.recvfrom(BUFFER_SIZE)
print(str(data))


#envoyer des données "Télémétriques":
#msg2 = (bytes("F1-data", "utf-8"))
data_unpack = 3.1425368798458
data_pack = struct.pack("f", data_unpack)

while True:
        time.sleep(3)
        #send
        s.sendto(data_pack, (IP, PORT))



s.close()




#Beffersize: 4096