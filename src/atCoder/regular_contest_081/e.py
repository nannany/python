import string

if __name__ == '__main__':
    A = input()

    # 一番最初に該当のアルファベットが出てくるindexを保持。
    p = {}
    for x in string.ascii_lowercase:
        p[x] = len(A)
    # print(p)
    '''
    tb
    1つ目：以降にa~zがいくつ存在するか+1
    2つ目：アルファベット
    3つ目：次のSの最初の文字があるindex
    '''
    tb = [(0, 0, 0)] * len(A)
    tb.append((1, 0, 0))
    tb.append((0, 0, 0))
    # print(tb)
    for i, x in reversed(list(enumerate(A))):
        p[x] = i
        tb[i] = min([(tb[p[c] + 1][0] + 1, c, p[c] + 1) for c in string.ascii_lowercase])
        print(tb)
    i = 0
    ans = []
    while i < len(A):
        ans.append(tb[i][1])
        i = tb[i][2]

    print("".join(ans))
