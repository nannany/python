import codecs


def main():
    encryped_data = open('rule86.txt.enc', 'rb').read()
    decryped_data = open('rule86.txt', 'rb').read()

    global key
    key = []
    for enc, dec in zip(encryped_data, decryped_data):
        key.append(enc ^ dec)

    e_super_cipher = open('super_cipher.py.enc', 'rb').read()

    d_super_cipher = []
    for sc, k in zip(e_super_cipher, key):
        d_super_cipher.append(sc ^ k)

    tmp = list(map(chr, d_super_cipher))
    print("".join(tmp))

    # hint_gif()


def hint_gif():
    e_hint_gif_list = list(open('hint.gif.enc', 'rb').read())

    d_hind_gif_list = []

    for e, k in zip(e_hint_gif_list, key):
        d_hind_gif_list.append(e ^ k)

    gif = ""
    g = ""
    for d in d_hind_gif_list:
        g += str(hex(d))
        gif += str(hex(d))[2:]
    print(g)
    print(gif)
    open('hint.gif', 'wb').write(codecs.decode(gif, 'hex'))


if __name__ == '__main__':
    main()
