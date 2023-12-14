import random
sifre_uzunlugu = int(input("Şifreniz Hangi Uzunlukta Olsun?"))
sifre = []
for i in range(sifre_uzunlugu):
    sifre.append(random.choice("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"))
print(sifre)