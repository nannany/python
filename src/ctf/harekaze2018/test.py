import random
import base64

base64_ans = "7XDZk9F4ZI5WpcFOfej3Dbau3yc1kxUgqmRCPMkzgyYFGjsRJF9aMaLHyDU="
print(base64.b64decode(base64_ans))

# 最後のBASE64化された文字列のビット配列
enc_flag = ""
for tmp in base64.b64decode(base64_ans):
    enc_flag += bin(tmp)[2:].zfill(8)

# 最終的な暗号化されたフラグのビット文字列
print(enc_flag)

import sympy

# Sはランダム関数の種を生成する際に使う数
S = 4529255040439033800342855653030016000

# factors = sympy.factorint(S)
# print(factors)
# # Sと互いに素にならない数の個数
# not_tagainiso = 1
# for k, v in factors.items():
#     not_tagainiso *= (v + 1)
#
# print(not_tagainiso)
#
# seed = S - (not_tagainiso - 2)
#
#
# random.seed(str(seed).rstrip("0"))
#
# key = bytes([random.randint(0, 255) for _ in range(44)])
#
# print(key)

# key_hairetu = ""
# for tmp2 in key:
#     key_hairetu += bin(tmp2)[2:].zfill(8)
#
# print(key_hairetu)
# hirabun = ""
# for ango, key in zip(enc_flag, key_hairetu):
#     hirabun += str(int(ango) ^ int(key))
# print(hirabun)

# ans = ""
# for i in range(0, len(hirabun), 8):
#     ans += chr(int(hirabun[i:i + 8], 2))

partial_ans = "Hare"
partial_ans_bit_array = ""
for part in partial_ans:
    partial_ans_bit_array += bin(ord(part))[2:].zfill(8)
print(partial_ans_bit_array)

for i in range(10000000, 100000000):
    if str(i).find('0') > -1:
        continue
    random.seed(str(i))
    key = ([random.randint(0, 255) for _ in range(4)])
    tmp_array = ""
    for tmp in key:
        tmp_array += bin(tmp)[2:].zfill(8)

    tmp_decry_array = ""
    for enc, k in zip(enc_flag, tmp_array):
        tmp_decry_array += str(int(enc) ^ int(k))
    print(i)
    if tmp_decry_array == partial_ans_bit_array:
        print(i)
        ans_seed = i
        break
# ans_seed = 11128429
# print(ans_seed)
# random.seed(str(ans_seed))
# key_array_hex = ([random.randint(0, 255) for _ in range(44)])
#
# key_array = ""
# for j in key_array_hex:
#     key_array += bin(j)[2:].zfill(8)
#
# answer = ""
# print(enc_flag)
# print(key_array)
# for ango, k in zip(enc_flag, key_array):
#     answer += str(int(ango) ^ int(k))
# print(answer)
#
# ans = ""
# for i in range(0, len(answer), 8):
#     ans += chr(int(answer[i:i + 8], 2))
#     print(ans)
# print(ans)
