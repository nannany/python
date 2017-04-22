A = input()
B = input()
if A == B:
    print("EQUAL")

if len(B) < len(A):
    print("GREATER")
elif len(A) < len(B):
    print("LESS")
else:
    for i in range(0, len(A)):
        if int(B[i]) < int(A[i]):
            print("GREATER")
            break
        elif int(A[i]) < int(B[i]):
            print("LESS")
            break
