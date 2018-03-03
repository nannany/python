if __name__ == '__main__':
    N = input()
    if len(N) == 1:
        print(N)
    else:
        cand_1 = sum([int(_) for _ in N])
        cand_2 = 9 * (len(N) - 1) + int(N[0]) - 1

        if cand_1 > cand_2:
            print(cand_1)
        else:
            print(cand_2)
