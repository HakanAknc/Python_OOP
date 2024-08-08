# sınıf ve nesne kavramı

class Ogrenci:

    ad = "Hakan"
    soyad = "Akinci"


    def yazdir(self):
        print(self.ad)
        print(self.soyad)

    def ortalama(self, vize, final):
        return (vize*0.4 + final*0.6)



nesne = Ogrenci()
# print(nesne)
# print(type(nesne))

print(nesne.ad)
print(nesne.soyad)

print()

nesne.yazdir()

print()

print("Ortalama:  " , nesne.ortalama(85,45))