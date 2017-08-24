class MinProduct:
    def findMin(self, amount, blank1, blank2):
        tmp_list = []
        for i in range(0, 10):
            for j in range(int(amount[i])):
                tmp_list.append(i)

        choose_from = tmp_list[:(blank1 + blank2)]

        A = min(blank1, blank2)
        B = max(blank1, blank2)

        A_list = []
        B_list = []
        while choose_from:
            if len(A_list) < A:
                A_list.append(choose_from.pop(0))

            B_list.append(choose_from.pop(0))
        A_list = [str(x) for x in A_list]
        B_list = [str(x) for x in B_list]
        A_num = int("".join(A_list))
        B_num = int("".join(B_list))

        return A_num * B_num
