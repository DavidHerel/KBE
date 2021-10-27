def bin2txt(input):
    ascii_string = "".join([chr(int(binary, 2)) for binary in input.split(" ")])
    return ascii_string

def bin2hex(input):
    ascii_string = "".join([hex(int(binary, 2)) for binary in input.split(" ")])
    return ascii_string

def txt2bin(input):
    return ' '.join(format(ord(x), 'b') for x in input)

def hex2bin(input):
    return "{0:08b}".format(int(input, 16))

def hex2txt(input):
    return bytearray.fromhex(input).decode()

def txt2hex(input):
    return input.encode('utf-8').hex()

print(bin2txt('1101000 1100101 1101100 1101100 1101111 100000 1110111 1101111 1110010 1101100 1100100'))
print(bin2hex('00011010'))
print(txt2bin("hello world"))
print(hex2bin('0x1a'))
print(hex2txt('7061756c'))
print(txt2hex('paul'))

