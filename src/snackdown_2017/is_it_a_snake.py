if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        plate = [list(input()) for j in range(2)]
        """
       ##
       ##
       の部分をなくす
       """
        while True:
            for j in range(0, len(plate[0]) - 1):
                if plate[0][j] == "#" and plate[0][j + 1] == "#" and plate[1][j] == "#" and plate[1][j + 1] == "#":
                    plate[0].pop(j)
                    plate[0].pop(j)
                    plate[1].pop(j)
                    plate[1].pop(j)
                    break
            else:
                break

        sharp_count = plate[0].count("#") + plate[1].count("#")
        virtical_conn_count = 0
        for j in range(0, len(plate[0])):
            if plate[0][j] == "#" and plate[1][j] == "#":
                virtical_conn_count += 1

        horizontal_conn_count = 0
        for j in range(0, len(plate[0]) - 1):
            if plate[0][j] == "#" and plate[0][j + 1] == "#":
                horizontal_conn_count += 1

            if plate[1][j] == "#" and plate[1][j + 1] == "#":
                horizontal_conn_count += 1

        if sharp_count - (virtical_conn_count + horizontal_conn_count) != 1 and sharp_count != 0:
            print("no")
            continue

        is_branched = False
        for j in range(0, len(plate[0]) - 2):
            if (plate[0][j] == "#" and plate[0][j + 1] == "#" and plate[0][j + 2] == "#" and plate[1][j] == "." and
                        plate[1][j + 1] == "#" and plate[1][j + 2] == ".") or (
                                            plate[0][j] == "." and plate[0][j + 1] == "#" and plate[0][j + 2] == "." and
                                    plate[1][j] == "#" and plate[1][j + 1] == "#" and plate[1][j + 2] == "#"):
                is_branched = True

        if is_branched:
            print("no")
        else:
            print("yes")
