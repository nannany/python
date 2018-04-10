seed = [226, 147, 117, 181, 251, 144, 241, 112]
tmp = ""
for s in seed:
    tmp += hex(s)[2:]
tmp_x = int(tmp, 16)
print(tmp_x)
RULE = [86 >> i & 1 for i in range(8)]
N_BYTES = 32
# N = 256
N = 8 * N_BYTES


def next(x):
    x = (x & 1) << N + 1 | x << 1 | x >> N - 1
    y = 0
    for i in range(N):
        y |= RULE[(x >> i) & 7] << i
    return y


# Bootstrap the PNRG
keystream = int.from_bytes(tmp_x.to_bytes(8,'little'), 'little')
print(keystream)
for i in range(N // 2):
    keystream = next(keystream)

print(keystream)
print(keystream.to_bytes(32,'big'))

# [214, 184, 140, 152, 192, 213, 191, 186]が次