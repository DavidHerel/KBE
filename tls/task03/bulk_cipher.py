import random
import string
import os

from tls.task03.task03 import decrypt, encrypt

BLOCK_SIZE = 16

key = os.urandom(BLOCK_SIZE)
iv = os.urandom(BLOCK_SIZE)
msg = ''.join(random.choice(string.ascii_lowercase) for i in range(1024))
print(encrypt(key, iv, msg))
print(decrypt(key, iv, encrypt(key, iv, msg)))
assert decrypt(key, iv, encrypt(key, iv, msg)) == msg