# Kullanıcıdan iki sayı alarak bunların toplamını ekran yazdıran ve
# ortalamsını ekrana yazan programı yazınız.

sayi1 = int(input("İlk sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))

toplam = sayi1 + sayi2
ortalama = ((sayi1 + sayi2) / 2)

print("Toplam : " , toplam)
print("Ortalama : ", ortalama)