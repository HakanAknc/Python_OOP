# 1'den n'e kadar olan sayılardan tek olanların toplamını bulunuz?
# n sayısı kullanıcıdan alınacaktır.

# n = int(input("n sayısı: "))

# # 1. yol mod alma
# toplam = 0

# for i in range(n):
#     if i%2 == 1:
#         toplam += i             # toplam = toplam + i

# print("Tek sayıların toplamı : ", toplam)



n = int(input("n sayısını giriniz: "))

toplam = 0

for i in range(n):
    toplam += i

print("Tek sayıların toplamı : " , toplam)