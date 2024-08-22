from abc import ABC, abstractmethod

class Personel(ABC):
    def __init__(self, isim, id_no):
        self.isim = isim
        self.id_no = id_no

    @abstractmethod
    def bilgi_goster(self):
        pass

class Ogretmen(Personel):
    def __init__(self, isim, id_no, brans):
        super().__init__(isim, id_no)
        self.brans = brans

    def bilgi_goster(self):
        return f"Öğretmen: {self.isim}, ID: {self.id_no}, Brans: {self.brans}"
    
class Ogrenci(Personel):
    def __init__(self, isim, id_no, sinif):
        super().__init__(isim, id_no)
        self.sinif = sinif

    def bilgi_goster(self):
        return f"Öğrenci: {self.isim}, ID: {self.id_no}, Sınıflar: {self.sinif}"
    
class EgitimKurumu:
    def __init__(self):
        self.personeller = []

    def personel_ekle(self, personel):
        self.personeller.append(personel)

    def personel_bilgilerini_goster(self):
        for personel in self.personeller:
            print(personel.bilgi_goster())


            # Örnek Kullanım
if __name__ == "__main__":
    kurum = EgitimKurumu()
    
    ogretmen1 = Ogretmen("Ahmet", "T001", "Matematik")
    ogrenci1 = Ogrenci("Ayşe", "S001", "10. Sınıf")
    
    kurum.personel_ekle(ogretmen1)
    kurum.personel_ekle(ogrenci1)
    
    kurum.personel_bilgilerini_goster()