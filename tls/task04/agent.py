import hashlib
import os
import random

from tls.task02.task02 import int_to_bytes
from tls.task03.task03 import encrypt, decrypt


class Agent:

    def __init__(self, msg=None):
        self.p, self.g = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF, 2
        self.msg = msg
        self.secret = None
        #choose a random number from 0 to P (Zp)
        self.private_key = random.randint(0, self.p)
        self.block_size = 16

    def send_public_data(self):
        return self.p, self.g

    def receive_public_data(self, p, g):
        self.p, self.g = p, g

    def send_public_key(self):
        public_key = pow(self.g, self.private_key, self.p)
        return public_key

    def receive_public_key(self, public_key):
        self.secret = pow(public_key, self.private_key, self.p)

    def send_message(self):
        iv = os.urandom(self.block_size)
        ans = hashlib.sha1(int_to_bytes(self.secret))
        ans = ans.hexdigest()[:16]
        return [encrypt(str.encode(ans), iv, self.msg), iv]

    def receive_message(self, arr):
        ans = hashlib.sha1(int_to_bytes(self.secret))
        ans = ans.hexdigest()[:16]
        self.msg = decrypt(str.encode(ans), arr[1], arr[0])




