from tls.task06.rsa_agent import RsaAgent

#int test
alice = RsaAgent()
bob = RsaAgent()
message = "I will not write crypto code myself, but defer to high-level libraries written by experts who took the right decisions for me".encode()
message = int.from_bytes(message, "big")
assert message == bob.decrypt_int(alice.encrypt_int(message, bob.n, bob.e))

#bytes test
message = "I will not write crypto code myself, but defer to high-level libraries written by experts who took the right decisions for me".encode()
dec_mess = bob.decrypt(alice.encrypt(message, bob.n, bob.e)).decode("utf-8")
dec_mess = dec_mess.replace('\x00', '').encode()
assert message == dec_mess

#inv mod test
desired = 701912218
got = alice.inv_mod(19, 1212393831)
assert desired == got