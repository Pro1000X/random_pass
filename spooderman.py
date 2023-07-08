import random
password = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
kocok = int(input("berapa panjang anda ingin karakternya dibuat "))
lol = ""
for i in range(kocok):
    lol += random.choice(password)
print(lol)