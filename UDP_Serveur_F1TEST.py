import socket
from f1_2020_telemetry.packets import unpack_udp_packet


#UDP protocole
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

#listenning from any IP on default port 20777 / however, if not working, try the IP -"127.000.001"- 
IP = ""   
PORT = 20777
s.bind((IP, PORT))

#getting the informations:
buf_size = 2048

while True:
    udp_packet = s.recv(buf_size)
    packet = unpack_udp_packet(udp_packet)
    print("Received", packet)
    print()
