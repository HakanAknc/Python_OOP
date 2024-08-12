from abc import ABC, abstractmethod

# Temel Ürün sınıfı
class Urun(ABC):
    def __init__(self, isim, fiyat):
        self.isim = isim
        self.fiyat = fiyat
    
    @abstractmethod
    def fiyat_hesapla(self):
        pass

# Elektronik Ürün sınıfı
class ElektronikUrun(Urun):
    def __init__(self, isim, fiyat, garanti_suresi):
        super().__init__(isim, fiyat)
        self.garanti_suresi = garanti_suresi
    
    def fiyat_hesapla(self):
        # Basit bir fiyat hesaplama örneği
        return self.fiyat * 1.1  # Garanti süresi fiyatı etkiliyor

# Gıda Ürünleri sınıfı
class GidaUrun(Urun):
    def __init__(self, isim, fiyat, son_kullanim_tarihi):
        super().__init__(isim, fiyat)
        self.son_kullanim_tarihi = son_kullanim_tarihi
    
    def fiyat_hesapla(self):
        # Basit bir fiyat hesaplama örneği
        return self.fiyat * 0.9  # Son kullanım tarihi fiyatı etkiliyor

# Örnek Kullanım
elektronik_urun = ElektronikUrun("Laptop", 1000, "2 yıl")
gida_urun = GidaUrun("Ekmek", 5, "2024-08-10")

print(f"{elektronik_urun.isim} fiyatı: {elektronik_urun.fiyat_hesapla()} TL")
print(f"{gida_urun.isim} fiyatı: {gida_urun.fiyat_hesapla()} TL")
