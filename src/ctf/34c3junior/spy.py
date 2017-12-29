import base64

if __name__ == '__main__':
    f = open('spydata.txt')
    data1 = f.read()  # ファイル終端まで全て読んだデータを返す
    f.close()
    print(data1)
    ascii_list = list(map(int, data1.split(",")))
    print(ascii_list)

    base64_str =""
    for ele in ascii_list:
        base64_str += chr(ele)

    print(base64_str)

    print(base64.b64decode(base64_str))