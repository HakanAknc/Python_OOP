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
    

konser = Etkinlik("Konser", "12.12.2023", "Ankara")
# print(konser.isim)
# print(konser.tarih) 
# print(konser.yer)

# bilet1 = Bilet("VIP", 250, "Ali Demir")
# bilet2 = Bilet("Normal", 150, "Caner Ak")

# print(bilet1.kategori, bilet1.fiyat, bilet1.rezerve_eden)
# print(bilet2.kategori, bilet2.fiyat, bilet2.rezerve_eden)

# konser.bilet_ekle(bilet1)
# konser.bilet_ekle(bilet2)
konser.biletleri_goster()