import socket
import helpencrypt
import traceback

host = "127.0.0.1"
port = 9003
K = b"0123456789012345"

# k = helpencrypt.key_generator()
# print(k)
# key = helpencrypt.aeskey(K).encrypt(k)
# print(key)
# k1 = helpencrypt.aeskey(K).decrypt(key)
# print(k1)
skm = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
skm.bind((host,port))
skm.listen(1)
try:
    con, adr = skm.accept()
    msg = con.recv(1024)
    k1 = helpencrypt.key_generator()
    key = helpencrypt.aeskey(K).encrypt(k1)
    con.sendall(key)
except Exception:
    print(traceback.format_exc())
con.close()
skm.close()

