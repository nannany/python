if __name__ == '__main__':
    nums = sorted(list(map(int, input().split())))

    ans = 0
    l_s = nums[2] - nums[0]
    l_m = nums[2] - nums[1]
    ans += l_s // 2 + l_m // 2
    nums[0] += 2 * (l_s // 2)
    nums[1] += 2 * (l_m // 2)

    # print(ans)
    # print(nums)
    if nums[0] == nums[1] and nums[0] == nums[2]:
        print(ans)
    elif nums[0] == nums[1] and nums[1] != nums[2]:
        print(ans + 1)
    else:
        print(ans + 2)
