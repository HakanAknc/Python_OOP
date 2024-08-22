class Etkinlik:
    def __init__(self, isim, tarih, yer):
        self.isim = isim
        self.tarih = tarih
        self.yer = yer
        self.biletler = []

    def bilet_ekle(self, bilet):
        self.biletler.append(bilet)

    def biletleri_goster(self):
        for bilet in self.biletler:
            print(bilet)

class Bilet:
    def __init__(self, kategori, fiyat, isim):
        self.kategori = kategori
        self.fiyat = fiyat
        self.rezerve_eden = isim

    def __str__(self):
        return f"{self.kategori} - {self.fiyat}, Rezerve eden: {self.rezerve_eden}"
    

konser = Etkinlik("Konser", "12.12.2024", "Ankara")
print(konser.isim)
print(konser.tarih)
print(konser.yer)

bilet1 = Bilet("VIP", 250, "Hakan Akıncı")
bilet2 = Bilet("VIP", 250, "Evren Akıncı")
print(bilet1)
print(bilet2)
