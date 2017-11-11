if __name__ == '__main__':
    hex1, hex2 = input().split()
    if int(hex1, 16) < int(hex2, 16):
        print('<')
    elif int(hex1, 16) > int(hex2, 16):
        print('>')
    else:
        print('=')
