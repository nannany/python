# genlto
def genOdd():
    i = 1
    while i <= 30:
        yield i
        i += 2


it = genOdd()
for v in it:
    print(v, end=",")

print()

# genPrime
def genPrime():
    i = 2
    while i < 100:
        if i // 2 == 1:
            yield i
            i += 1
            continue
        j = 2
        while j <= (i // 2):
            if i % j == 0:
                i += 1
                break
            j += 1
        else:
            yield i
            i += 1


it2 = genPrime()
for v in it2:
    print(v, end=",")
