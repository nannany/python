#!/usr/bin/env python3
import binascii
import string

key = "ULsitTdR"


def mystery(s):
    r = ""
    for i, c in enumerate(s):
        r += chr(ord(c) ^ ((i * ord(key[i % len(key)])) % 256))
    return binascii.hexlify(bytes(r, "utf-8"))


print(mystery("easyctf{"))

enc = "652dc29542c2b3c3903e45c38bc3841fc3b12f2601c291336477c2b94fc2a1c2ac6bc2bc59c38b6e"

org_strs = string.ascii_letters + string.digits + '_'

for i in range(0,len(enc),2):
    if enc[i:i+2] != 'c2' and enc[i:i+2] != 'c3':
        for s in org_strs:


