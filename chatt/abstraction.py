
# ! 5. Soyutlama (Abstraction)
# ! Soyutlama, gereksiz detayları gizleyip sadece önemli kısımları ortaya çıkarma işlemidir. 
# ! Python'da soyut sınıflar ABC (Abstract Base Class) modülü kullanılarak tanımlanabilir.

"""
Abstraction (Soyutlama), bir nesnenin ya da sistemin içsel detaylarını gizleyerek, yalnızca önemli ve gerekli
 özellikleri dışa sunma işlemidir.
"""

from abc import ABC, abstractmethod

class Sekil(ABC):
    @abstractmethod
    def alan_hesapla(self):
        pass

class Dikdortgen(Sekil):
    def __init__(self, genislik, yukseklik):
        self.genislik = genislik
        self.yukseklik = yukseklik

    def alan_hesapla(self):
        return self.genislik * self.yukseklik
    
class Daire(Sekil):
    def __init__(self, yaricap):
        self.yaricap = yaricap

    def alan_hesapla(self):
        return 3.14 * (self.yaricap ** 2)
    

# Şekil nesneleri olusturalım
dikdortgen = Dikdortgen(5, 7)
daire = Daire(3)

print(dikdortgen.alan_hesapla())  # Çıktı: 35
print(daire.alan_hesapla())  # Çıktı: 28.26