if __name__ == '__main__':
    target_list = [0x4d, 0xfa, 0x0b, 0x29, 0xbe, 0x36, 0xf8, 0xc9, 0x2f, 0x0f, 0x01, 0xf0, 0x05, 0xcf, 0x39, 0xcb, 0x2a,
                   0xfe, 0xd4, 0x3b, 0xd5, 0x2c, 0xd5, 0x21, 0xcc, 0x01, 0x4b]

    ans = ""

    ascii_num = 0
    for target in target_list:
        ascii_num += int(target)
        ascii_num %= 256

        ans += chr(ascii_num)

    print(ans)
