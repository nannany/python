if __name__ == '__main__':
    S = input()

    bit_num = 2 ** (len(S) - 1)

    ans = 0
    for i in range(bit_num):
        formula = S[0]
        for j in range(len(S) - 1):
            if i & 2 ** j:
                formula += "+"
            formula += S[j + 1]

        ans += eval(formula)

    print(ans)
