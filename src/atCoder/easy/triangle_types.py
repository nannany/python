if __name__ == '__main__':

    triangle_count = 0
    right_count = 0
    acute_count = 0
    obtuse_count = 0
    while True:
        sides = sorted(list(map(int, input().split())))

        if sides[0] + sides[1] <= sides[2]:
            break

        triangle_count += 1

        judge = sides[2] ** 2 - (sides[0] ** 2 + sides[1] ** 2)
        if judge > 0:
            obtuse_count += 1
        elif judge == 0:
            right_count += 1
        else:
            acute_count += 1

    print(str(triangle_count) + " " + str(right_count) + " " + str(acute_count) + " " + str(obtuse_count) + " ")
    print()