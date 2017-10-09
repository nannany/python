if __name__ == '__main__':
    N = int(input())
    s = input()

    ans = 0
    one_accumulate = 0
    for i in range(N):
        if s[i:i + 3] == "101":
            ans += 1 + one_accumulate
            s = s[:i] + "010" + s[(i + 3):]
            one_accumulate = 0
            print(s)
        else:
            if s[i] == "1":
                one_accumulate += 1
            elif s[i] == "0":
                one_accumulate = 0

    print(ans)
