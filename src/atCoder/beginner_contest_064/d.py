if __name__ == '__main__':
    N = int(input())
    S = input()
    tmpS = S
    for i in range(50):
        tmpS = tmpS.replace("()", "")

    # print(tmpS)
    left_parenthesis_count = 0
    right_parenthesis_count = 0
    for moji in tmpS:
        if moji == "(":
            left_parenthesis_count += 1
        elif moji == ")":
            right_parenthesis_count += 1

    ans = S
    for i in range(right_parenthesis_count):
        ans = "(" + ans

    for i in range(left_parenthesis_count):
        ans += ")"

    print(ans)
