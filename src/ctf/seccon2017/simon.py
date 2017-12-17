import itertools
import bitstring
import string


def key_expansion():
    for i in range(m, T):
        tmp = k[i -1]
        tmp = k[i-1].ror(3)


if __name__ == '__main__':
    z = [0b11111010001001010110000111001101111101000100101011000011100110,
         0b10001110111110010011000010110101000111011111001001100001011010,
         0b10101111011100000011010010011000101000010001111110010110110011,
         0b11011011101011000110010111100000010010001010011100110100001111,
         0b11010001111001101011011000100000010111000011001010010011101111]
    T, j = 42, 2
    n, m = 32, 3
    plain = bitstring.BitArray('0x6d564d37426e6e71')
    print(plain.bin)
    cipher = bitstring.BitArray('0xbb5d12ba422834b5')
    k = [0 for _ in range(3)]
    k[2] = bitstring.BitArray(bytes('SECC', 'UTF-8'))

    # 全部は出せなそう
    target_strings = string.ascii_uppercase
    print(target_strings)
    target_binaries = []
    for pair in itertools.product(target_strings, repeat=4):
        k1 = 'ON{' + pair[0]
        k2 = pair[1] + pair[2] + pair[3] + "}"
        k[1] = bitstring.BitArray(bytes(k1, 'UTF-8'))
        k[0] = bitstring.BitArray(bytes(k2, 'UTF-8'))
        key_expansion()
