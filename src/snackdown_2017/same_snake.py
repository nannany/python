T = int(input())
for i in range(T):
    x11, y11, x12, y12 = list(map(int, input().split()))
    x21, y21, x22, y22 = list(map(int, input().split()))

    # 交差しているかを確かめる
    min_x1 = min(x11, x12)
    min_x2 = min(x21, x22)
    max_x1 = max(x11, x12)
    max_x2 = max(x21, x22)
    min_y1 = min(y11, y12)
    min_y2 = min(y21, y22)
    max_y1 = max(y11, y12)
    max_y2 = max(y21, y22)
    if (min_x1 <= min_x2 <= max_x1 or min_x1 <= max_x2 <= max_x1 or (min_x2 <= min_x1 and max_x1 <= max_x2)) and (
                            min_y1 <= min_y2 <= max_y1 or min_y1 <= max_y2 <= max_y1 or (
                            min_y2 <= min_y1 and max_y1 <= max_y2)):
        pass
    else:
        print("no")
        continue

    """
    分岐がないか確かめる
    ・平行な場合
    """
    if (x11 == x12 and x21 == x22) or (y11 == y12 and y21 == y22):
        print("yes")
        continue

    """
    分岐がないか確かめる
    ・平行でない場合
    """
    if (x11 == x21 and y11 == y21) or (x11 == x22 and y11 == y22) or (x12 == x21 and y12 == y21) or (
                    x12 == x22 and y12 == y22):
        print("yes")
        continue
    else:
        print("no")
        continue
