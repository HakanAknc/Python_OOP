class Etkinlik:
    def __init__(self, isim, tarih, year):
        self.isim = isim
        self.tarih = tarih
        self.year = year
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
    
    def __str__(self) -> str:
        return f"{self.kategori} - {self.fiyat}, Rezerve eden : {self.rezerve_eden}"
    

konser = Etkinlik("Konser", "12.12.2024", "Ankara")
# print(konser.isim)
# print()
bilet1 = Bilet("VIP", 250, "Ali Demir")
bilet2 = Bilet("Normal", 150, "Mehmet Veli")
bilet3 = Bilet("VIP", 350, "Hakan Akinci")

konser.bilet_ekle(bilet1)
konser.bilet_ekle(bilet2)
konser.bilet_ekle(bilet3)

konser.biletleri_goster()
