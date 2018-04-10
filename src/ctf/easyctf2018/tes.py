import binascii
key = "ULsitTdR"
def mystery(s):
    r = ""
    for i, c in enumerate(s):
        r += chr(ord(c) ^ ((i * ord(key[i % len(key)])) % 256))
    return binascii.hexlify(bytes(r, "utf-8"))

print(chr(0x95))
print(binascii.hexlify(bytes(chr(0xdd),"utf-8")))
print(binascii.hexlify(bytes(chr(0x8b),"utf-8")))