
from hashlib import md5
from base64 import b64decode
from base64 import b64encode

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


def encrypt(key, iv, msg):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return b64encode(iv + cipher.encrypt(pad(msg.encode('utf-8'),16)))

def decrypt(key, iv, msg):
    msg = b64decode(msg)
    cipher = AES.new(key, AES.MODE_CBC, iv[:16])
    return unpad(cipher.decrypt(msg[16:]), 16).decode('utf-8')