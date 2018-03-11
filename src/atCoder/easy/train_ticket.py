if __name__ == '__main__':
    S = input()
    recur_num = (len(S) - 1) ** 2

    for i in range(recur_num):
        ope = []
        for j in range(len(S) - 1):
            if i & (2 ** j):
                ope.append("+")
            else:
                ope.append("-")

        if eval(S[0] + ope[0] + S[1] + ope[1] + S[2] + ope[2] + S[3]) == 7:
            print(S[0] + ope[0] + S[1] + ope[1] + S[2] + ope[2] + S[3] + "=7")
            break
