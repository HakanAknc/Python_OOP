# Kullanıcıdan ismini ve soyismini alarak içersinde
# kaç adet sesli kaç adet sessiz harf olduğunu bulan programı yazınız.

yazi = input("Bir metin giriniz: ")

sesli = "aeiıoöuü"
sesli_sayac = 0

for harf in yazi:
    if harf in sesli:
        sesli_sayac += 1

print("Sesli harf sayısı : ",sesli_sayac)
print("Sessiz harf sayısı = ", len(yazi)-sesli_sayac)