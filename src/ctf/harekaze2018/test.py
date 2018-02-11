import itertools
import functools
import operator
import random
import base64

base64_ans = "7XDZk9F4ZI5WpcFOfej3Dbau3yc1kxUgqmRCPMkzgyYFGjsRJF9aMaLHyDU="
# print(base64.b64decode(base64_ans))

# 最後のBASE64化された文字列のビット配列
enc_flag_bit_array = ""
for tmp in base64.b64decode(base64_ans):
    enc_flag_bit_array += bin(tmp)[2:].zfill(8)

# 最終的な暗号化されたフラグのビット文字列
# print(enc_flag)

import sympy

# Sはランダム関数の種を生成する際に使う数
S = 4529255040439033800342855653030016000

factors = sympy.factorint(S)

# 包除原理を用いて解く
prime_factors_list = [p for p, _ in factors.items()]
# print(prime_factors_list)

# for tup in itertools.combinations(prime_factors_list,2):
#     print(tup)

# Sと互いに素にならない数の個数
not_tagainiso = 0

for i in range(1, len(prime_factors_list) + 1):
    for tup in itertools.combinations(prime_factors_list, i):
        if i & 1:
            not_tagainiso += S // functools.reduce(operator.mul, tup)
        else:
            not_tagainiso -= S // functools.reduce(operator.mul, tup)
seed = S - not_tagainiso
random.seed(str(seed).rstrip("0"))
key = bytes([random.randint(0, 255) for _ in range(45)])

key_bit_array = ""
for i in key:
    key_bit_array += bin(i)[2:].zfill(8)

ans_bit_array = ""
for e, k in zip(enc_flag_bit_array, key_bit_array):
    ans_bit_array += str(int(e) ^ int(k))

ans = ""
for j in range(0, len(enc_flag_bit_array), 8):
    ans += chr(int(ans_bit_array[j:j + 8], 2))

print(ans)
