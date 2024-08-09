# Kullanıcıdan alınan 3 sayının en büyüğünü bulan programı yazınız.

a = int(input("a sayısı: "))
b = int(input("b sayısı: "))
c = int(input("c sayısı: "))

if a > b and a > c:
    print("a büyüktür")
elif b > a and b > c:
    print("b büyüktür")
else:
    print("c büyüktür.")