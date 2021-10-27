import string
import itertools
import hashlib

if __name__ == "__main__":
    my_salt = 'a0c58'
    my_pass = 'b6a69d59dd2313f6d1237f9e34ef68e466a1cdbe'
    options = string.ascii_lowercase + string.digits
    combinations = [''.join(x) for x in itertools.product(options, repeat=5)]
    for x in combinations:
       to_be_hashed = x+my_salt
       hash_object = hashlib.sha1(bytes(to_be_hashed, encoding='utf-8'))       
       hex_dig = hash_object.hexdigest()
       if (hex_dig == my_pass):
          print(x)
    print("Nothing found")