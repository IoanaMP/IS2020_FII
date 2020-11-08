import socket
import helpencrypt

host = "127.0.0.1"
port = 9002
K = b"0123456789012345"
# # key = helpencrypt.aeskey(K)
# key = helpencrypt.key_generator()
# print(key)
skm = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
skm.bind((host,port))
skm.listen(1)
while True:
    con, adr = skm.accept()
    try:
        while True:
            msg = con.recv(1024)
            k1 = helpencrypt.key_generator()
            key = helpencrypt.aeskey(K).encrypt(k1)
            con.sendall(key)
    finally:
        con.close()
# while msg:
#     print("msg" +msg.decode())
#     msg = skm.recv(1024)
# con.sendall(key.encode())
# con.close()
