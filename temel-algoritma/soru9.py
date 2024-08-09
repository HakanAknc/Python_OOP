# kullanıcıdan ismini alıp ekrana tersten yazan program kodunu yazınız?

# 1. yol
"""
while True:
    isim = input("isminiz: ")

    print("İsminizin tersten yazılışı : " , isim[::-1])
"""

# 2. yol
isim = input("İsminizi girin: ")
uzunluk = len(isim)
print(uzunluk)
ters = ""
for i in range(uzunluk-1,-1,-1):
    ters += isim[i]

print(ters)