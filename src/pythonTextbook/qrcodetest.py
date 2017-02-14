import qrcode

img = qrcode.make("http://kujirahand.com/")
img.save("qrcode-test.jpg")
