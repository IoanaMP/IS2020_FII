#server
import socket
import helpencrypt

host ='localhost'
port = 9009
key = b'0123456789012345'
iv = b'abcdefghijklmnop'

if __name__=='__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1',port))
    s.listen(1)
    c, addr = s.accept()
    try:
        mode = c.recv(1024).decode()
        print("Modul de criptare trimis de A este: ", mode)
        msg = "Start"
        c.sendall(msg.encode())
        k1 = c.recv(1024)
        print("cheia primita k1")
        print(k1)
        #decrypt key
        k1 = helpencrypt.aeskey(key).decrypt(k1)
        print("cheia k1")
        print(k1)
        buff = b""
        text_block = c.recv(16)
        print(text_block)
        while text_block:
            buff += text_block 
            text_block  = c.recv(16)
            print("mesaj block:", text_block.decode())
            decry = helpencrypt.decryption(buff, k1, mode, iv)
            final = decry['ft']
            iv = decry['iv']
            print(final)
            print(decry['ft'])
    finally:
        c.close()
        s.close()
        

