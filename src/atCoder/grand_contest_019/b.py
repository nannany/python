import string

if __name__ == '__main__':
    A = list(input())
    hist = {}
    for c in string.ascii_lowercase:
        hist[c] = A.count(c)

    # print(hist)

    same_when_reverse = 0
    for v in hist.values():
        same_when_reverse += v * (v - 1) // 2

    num_len = len(A)
    print((num_len * (num_len - 1) // 2 + 1) - same_when_reverse)
