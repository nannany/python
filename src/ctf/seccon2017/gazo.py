data = open('tktk.jpg', "rb").read()
print(data.__class__)
print(data)
for i in range(0x263*8,0x273*8):
    print(data[:int(i/8)])
    print((data[int(i/8)]^1<<(i%8)).to_bytes(1,'big'))
    # fixディレクトリにいっぱいJPGファイルができる
    open("fix\\%d.jpg"%i, "wb").write(data[:int(i/8)]+(data[int(i/8)]^1<<(i%8)).to_bytes(1,'big')+data[int(i/8)+1:])

