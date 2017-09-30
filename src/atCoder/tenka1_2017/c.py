if __name__ == '__main__':
    N = int(input())
    for h in range(1, 3501):
        for n in range(1, 3501):
            if 4 * h * n - N * (n + h) > 0 and (N * h * n) % (4 * h * n - N * (n + h)) == 0:
                w = (N * h * n) // (4 * h * n - N * (n + h))
                print(str(h) + " " + str(n) + " " + str(w))
                exit()

