if __name__ == '__main__':
    N = input()
    harshad = 0
    for i in range(len(N)):
        harshad += int(N[i])

    # print(harshad)
    print("Yes" if int(N) % harshad == 0 else "No")
