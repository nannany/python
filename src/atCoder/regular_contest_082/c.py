if __name__ == '__main__':
    N = int(input())
    a = list(map(int, input().split()))

    result_counter = [0 for i in range(100001)]
    for number in a:
        if number == 0:
            result_counter[0] += 1
            result_counter[1] += 1
        else:
            result_counter[number - 1] += 1
            result_counter[number] += 1
            result_counter[number + 1] += 1

    print(max(result_counter))
