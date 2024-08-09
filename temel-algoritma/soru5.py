# vizenin notunun %40'ını, Final notunun %60'ını alarak ortalama notunu hesaplayın
# ortalama 50 den büyükse "Geçti", küçükse "Kaldı" yazan programı yazınız?

vize = int(input("vize notunuz: "))
final = int(input("final notunuz: "))

ortalama = vize*0.40 + final*0.60
print("Ortalama : " ,ortalama)

if ortalama > 50:
    print("Geçti")
else:
    print("Kaldı")