n = int(input())
a = list(map(int, input().split()))
k = int(input())


def search(i, sum1):
    print(str(i) + ":::" + str(sum1))
    if i == n:
        return sum1 == k

    if search(i + 1, sum1):
        return True
    if search(i + 1, sum1 + a[i]):
        return True

    return False


if __name__ == '__main__':
    if search(0, 0):
        print("Yes")
    else:
        print("No")
