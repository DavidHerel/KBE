import hashlib
import binascii

from tls.task02.task02 import int_to_bytes
from tls.task07.task07 import cube_root


class RsaAgent():

    def __init__(self, p=13604067676942311473880378997445560402287533018336255431768131877166265134668090936142489291434933287603794968158158703560092550835351613469384724860663783, q = 20711176938531842977036011179660439609300527493811127966259264079533873844612186164429520631818559067891139294434808806132282696875534951083307822997248459, e=3):
        self.p = p
        self.q = q
        self.e = e
        self.n = self.p * self.q
        self.mod = (self.p-1)*(self.q-1)
        self.d = self.inv_mod(self.e, self.mod)
        self.msg = None

    def inv_mod(self, a, m):
        return pow(a, -1, m)

    def encrypt(self, msg, n, e):
        msg = int.from_bytes(msg, "big")
        enc_msg = pow(msg, e, n)
        return int_to_bytes(enc_msg)

    def decrypt(self, msg):
        msg = int.from_bytes(msg, "big")
        dc_msg = pow(msg, self.d, self.n)
        self.msg = dc_msg
        return int_to_bytes(self.msg)

    def encrypt_int(self,  msg, n, e):
        enc_msg = pow(msg, e, n)
        return enc_msg

    def decrypt_int(self, msg):
        dc_msg = pow(msg, self.d, self.n)
        self.msg = dc_msg
        return self.msg

    def generate_message_hash(self, message):
        return hashlib.sha1(message).digest()

    def generate_signature(self, msg_sha1):
        f_counter = self.n.bit_length()//8 - len(msg_sha1) - 3
        output = bytes(b'\00\01') + f_counter*bytes(b'\xff') + (b'\00') + msg_sha1
        return self.decrypt(output)

    def verify_signature(self, signature, msg_sha1):
        encrypted = bytes(b'\x00') + self.encrypt(signature, self.n, self.e)

        #can not use this, cuz we need shitty implementation
        #f_counter = self.n.bit_length()//8 - len(msg_sha1) - 3

        index_0 = encrypted[2:].index(bytes(b'\00'))

        if encrypted[0:2] != bytes(b'\00\01'):
            return False

        #can not check this or attack will not work :))
        # elif encrypted[2:2+f_counter] != f_counter*bytes(b'\xff'):
        #     print("Error F ")
        #     return False

        elif encrypted[index_0+3:index_0+3+len(msg_sha1)] != msg_sha1:
            return False
        else:
            return True

    def fake_signature(self, msg_sha1):
        f_count = self.n.bit_length()//8 - len(msg_sha1) - 4
        sig = bytes(b'\x00\x01\xFF\x00') + msg_sha1 + bytes(b'\xFF') * f_count
        sig = int.from_bytes(sig, "big")

        return int_to_bytes(cube_root(sig))
