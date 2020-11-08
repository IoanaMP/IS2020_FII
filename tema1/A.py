# client

import socket
import helpencrypt

host = "localhost"
port = 9006
file = open('input.txt', 'rb')
text = file.read()
mod_crypt = ["CBC", "OFB"]
key = "0123456789012345"
iv = b'abcdefghijklmnop'

if __name__ == '__main__':
    choose_mod = input("Alegeti un tip de criptare(CBC sau OFB): ")

    # send message to KM
    skm = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    skm.connect((host, 9002))
    try:
        # send mode to km
        skm.sendall(choose_mod.encode())
        # recv the key from k
        kmsg = skm.recv(16)
        while kmsg:
            print("msg" + kmsg.decode())
            kmsg = skm.recv(16)
        #decrypt key
        k1 = helpencrypt.aeskey(key).decrypt(kmsg)
        print("key from km", k1)
    finally:
        skm.close
    

    # send message to B
    sb = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sb.connect((host, port))
    try:
        sb.sendall(choose_mod.encode())
        msg = sb.recv(1024).decode()
        if msg != "Start":
            raise Exception("B nu incepe conexiunea")
        print("Message from B:", msg)
        sb.sendall(k1)
        i=0
        while i <= len(text)-16:
            block = text[i:i+16]
            print(block)
            encrtext = helpencrypt.encryption(block, choose_mod, k1, iv)
            sb.sendall(encrtext['c'])
            i = i+16
    finally:
        sb.close()
