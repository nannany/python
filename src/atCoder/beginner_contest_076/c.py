if __name__ == '__main__':
    S = list(input())
    T = list(input())

    num = -1
    for i in range(len(S) - len(T)):
        flg = True
        for j in range(1, len(T) + 1):
            if S[-(i + j)] == "?":
                continue
            if S[-(i + j)] == T[-j]:
                continue
            flg = False
            break

        if flg:
            num = i
            break

    if num == -1:
        print("UNRESTORABLE")
    else:
        start = len(S) - (len(T) + num)
        end = len(S) - num
        S[start:end] = T
        mojiretu = "".join(S)
        ans = mojiretu.replace("?", "a")
        print(ans)