import os


class Stream:
    A = 37423
    B = 61781
    C = 34607

    def __init__(self, seed):
        self.seed = seed % self.C

    def __iter__(self):
        return self

    def next(self):
        self.seed = (self.A * self.seed + self.B) % self.C
        return self.seed


g = Stream(int(os.urandom(8).encode('hex'), 16))

encrypted_hex_data = "CE1E650C065F943A57491D17F517593F9C409D4A19318D263E51FD03CE525616"

