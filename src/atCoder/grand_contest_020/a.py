if __name__ == '__main__':
    N, A, B = map(int, input().split())
    if (A - B) % 2 == 1:
        print("Borys")
    else:
        print("Alice")
