if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = list(map(int, input().split()))
        u = []
        v = []
        for j in range(m):
            inputs = list(map(int, input().split()))
            u.append(inputs[0])
            v.append(inputs[1])
        if n % 2 == 0:
            print("yes")
        else:
            print("no")
