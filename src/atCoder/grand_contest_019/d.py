if __name__ == '__main__':
    A = list(input())
    B = list(input())
    if B.count("1") == 0:
        if A.count("1") == 0:
            print(0)
        else:
            print(-1)
    n = len(A)
    for d in range(0, n):
        reverse_count = 0
        for i in range(0, n):
            if A[i] != B[(i + d) % n]:
                reverse_count += 1
        x=[]
        y=[]
        for i in range(0,n):
            if 