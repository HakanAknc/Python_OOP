# n'den m'e kadar olan sayılardan 7'ye tam bölünenleri bulunuz?
# n başlangıç ve m bitiş sayısı kullanıcıdan alınacaktırç.

# while True:
#     n = int(input("Başlangıç sayısı giriniz: "))
#     m = int(input("Bitiş sayısı giriniz: "))
#     if n>=m:
#         print("Başlangıç sayısı daha küçük olmalı tekrar giriniz.")
#     else:
#         break

# toplam = 0

# for i in range(n, m):
#     if i%7 == 0:
#         toplam += i

# print("Yediye tam bölünenlerin toplamı: " ,toplam)

while True:
    n = int(input("Başlangıç sayısını giriniz: "))
    m = int(input("Bitiş sayısını giriniz: "))

    if n>=m:
        print("Başlanıç sayısı daha küçük olmalı, tekrar deneyiniz.")
    else:
        break

toplam = 0

for i in range(n, m):
    if i%7 == 0:
        toplam += i
    
print("Yediye tam bölünenlerin toplamı : " , toplam)
