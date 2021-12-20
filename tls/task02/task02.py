import hashlib
from tls.task01.task01 import vanilla_dh

def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')

def df_key():
    common_secret = vanilla_dh(45, 5)
    ans = hashlib.sha1(int_to_bytes(common_secret))
    return ans.hexdigest()[:16]