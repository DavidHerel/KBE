import hashlib

from tls.task02.task02 import int_to_bytes
from tls.task03.task03 import decrypt, encrypt
from tls.task04.agent import Agent


class MITM(Agent):

    def __init__(self):
        super().__init__()
        self.public_keys = []

    def receive_public_key(self, public_key):
        if len(self.public_keys) == 0:
            self.public_keys.append(pow(public_key, self.private_key, self.p))
        else:
            self.public_keys.append(pow(public_key, self.private_key, self.p))

    def intercept_message(self, param):
        ans = hashlib.sha1(int_to_bytes(self.public_keys[0]))
        ans = ans.hexdigest()[:16]
        self.msg = decrypt(str.encode(ans), param[1], param[0])
        ans = hashlib.sha1(int_to_bytes(self.public_keys[1]))
        ans = ans.hexdigest()[:16]
        return [encrypt(str.encode(ans), param[1], self.msg), param[1]]