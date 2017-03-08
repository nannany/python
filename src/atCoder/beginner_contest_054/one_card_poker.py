cards = input().split()
alice = int(cards[0])
bob = int(cards[1])

if alice == bob:
    print("Draw")
elif alice == 1:
    print("Alice")
elif bob == 1:
    print("Bob")
elif alice < bob:
    print("Bob")
else :
    print("Alice")