# client

import socket
import helpencrypt

host = "localhost"
port = 9009
file = open('input.txt', 'rb')
text = file.read()
mod_crypt = ["CBC", "OFB"]
key = b'0123456789012345'
iv = b'abcdefghijklmnop'

def KM_key():
    # connect to km
    skm = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    skm.connect((host, 9004))
    # send mode to km
    skm.sendall(choose_mod.encode())
    # recv the key from km
    kmsg = skm.recv(16)
    print("kmsg in f")
    print(kmsg)
    skm.close()
    return kmsg

if __name__ == '__main__':
    choose_mod = input("Alegeti un tip de criptare(CBC sau OFB): ")
    k1 = KM_key()
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
        #decrypt key
        k1 = helpencrypt.aeskey(key).decrypt(k1)
        i=0
        while i <= len(text)-16:
            block = text[i:i+16]
            print(block)
            encrtext = helpencrypt.encryption(block, k1, choose_mod, iv)
            sb.sendall(encrtext['c'])
            print(encrtext['c'])
            iv=encrtext['iv']
            i = i+16
    finally:
        sb.close()
