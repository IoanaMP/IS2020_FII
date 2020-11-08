#server
import socket
import helpencrypt

host ='localhost'
port = 9008
key = b'0123456789012345'
iv = b'abcdefghijklmnop'

if __name__=='__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1',port))
    s.listen(1)
    c, addr = s.accept()
    while c:
        mode = c.recv(1024).decode()
        print("Modul de criptare trimis de A este: ", mode)
        msg = "Start"
        c.sendall(msg.encode())
        k1 = c.recv(1024)
        buff = b""
        Amsg = c.recv(1024)
        while Amsg:
            buff += Amsg
            Amsg = c.recv(1024)
        print("mesaj block:", Amsg.decode())
        decry = helpencrypt.decryption(buff, k1, mode, iv)
        print(decry)
    c.close()
    s.close()
        

# while mode:
#     print("xv" + mode.decode())
#     mode = c.recv(1024)

# mode = c.recv(1024)
# while mode:
#     print("key" + mode.decode())
#     mode = c.recv(1024)

# c.close
