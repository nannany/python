if __name__ == '__main__':
    S = input()

    S1 = S.replace("A", "")
    if S1 != "KIHBR":
        print("NO")
        exit()

    if not "KIH" in S:
        print("NO")
        exit()

    if S.find("AA") > -1:
        print("NO")
        exit()

    print("YES")
