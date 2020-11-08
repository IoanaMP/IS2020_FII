from Crypto import Random
from Crypto.Cipher import AES
import binascii

iv = b'nu stiu ce contine'

def aeskey(kknown):
    var = AES.new(kknown, AES.MODE_CBC)
    return var

def key_generator():
    return Random.get_random_bytes(16)

def xor_function(a,b):
    var = binascii.hexlify(a)
    key = binascii.hexlify(b)
    enint = int(key, 16) ^ int(var, 16)
    hexen = "{:x}".format(enint)
    bincript = binascii.unhexlify(hexen)
    return bincript

# def padd(text):
#     blk = (16-len(text)%16)%16
#     text += chr(0).encode("utf8") * blk
#     return text

# def str_bt(msg):
#     if type(msg) is str:
#         return msg.encode("utf8")
#     return msg

def encryption(block_msg, key, type, iv):
    aes = aeskey(key)
    if type == "CBC":
       var = xor_function(block_msg, iv)
       en = aes.encrypt(var)
    if type == "OFB":
        var= aes.encrypt(iv)
        en = xor_function(block_msg, var)
    return {'c': en, 'iv': en}

def decryption(block_msg, key, type, iv):
    aes = aeskey(key)
    if type == "CBC":
        var = aes.decrypt(block_msg)
        dec = xor_function(var, iv)
        
    if type == "OFB":
        var = aes.decrypt(iv)
        dec = xor_function(var, block_msg)
    return {'ft': dec, 'iv': dec}
