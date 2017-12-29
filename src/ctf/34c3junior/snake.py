import string
import itertools
import hashlib


# x = input();
# e = lambda c, d: c + (d ^ 21);
# # a は辞書型。新ならcorrect、偽ならalmost
# a = {False: lambda: print('Almost!!'), True: lambda: print('Correct!')};
# a[[e(*b) for b in zip(list(map(ord, x)), list(map(ord, x))[::-1])][::-1] == [160, 155, 208, 160, 190, 215, 237, 134,
#                                                                              210, 126, 212, 222, 224, 238, 128, 240,
#                                                                              164, 213, 183, 192, 162, 178, 163,
#                                                                              162] and 'mo4r' in x and '34C3_' in x and
#   x.split('_')[3] == 'tzzzz']()
#
# # フラグは 34C3_mo4r    kes_tzzzz
# # 126, 212, 222, 224, 238, 128
# # 10～15までが不明


def main():
    candidate = string.ascii_letters + '0123456789_'
    print(candidate)
    one = []
    for str1, str2 in itertools.product(candidate, repeat=2):
        if ord(str1) + (ord(str2) ^ 21) == 128 and ord(str2) + (ord(str1) ^ 21) == 126:
            # print("str11:" + str1)
            # print("str12:" + str2)
            one.append((str1, str2))

    two = []
    for str1, str2 in itertools.product(candidate, repeat=2):
        if ord(str1) + (ord(str2) ^ 21) == 238 and ord(str2) + (ord(str1) ^ 21) == 212:
            # print("str21:" + str1)
            # print("str22:" + str2)
            two.append((str1, str2))

    three = []
    for str1, str2 in itertools.product(candidate, repeat=2):
        if ord(str1) + (ord(str2) ^ 21) == 224 and ord(str2) + (ord(str1) ^ 21) == 222:
            # print("str31:" + str1)
            # print("str32:" + str2)
            three.append((str1, str2))

    for str1, str6 in one:
        for str2, str5 in two:
            for str3, str4 in three:
                ans = "34C3_mo4r" + str1 + str2 + str3 + str4 + str5 + str6 + "kes_tzzzz"
                print(ans)
                if hashlib.md5(ans.encode()).hexdigest() == "5a76c600c2ca0f179b643a4fcd4bc7ac":
                    print(ans)


if __name__ == '__main__':
    main()
