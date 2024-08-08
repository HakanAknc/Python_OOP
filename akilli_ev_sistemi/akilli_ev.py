class AkilliCihaz:

    def __init__(self, oda):
        self.oda = oda
        self.acik = False

    def ac(self):
        self.acik = True

    def kapat(self):
        self.acik = False

class Isik(AkilliCihaz):

    def __init__(self, oda, renk):
        super().__init__(oda)
        self.renk = renk

    def renk_degistir(self, renk):
        self.renk = renk

class Klima(AkilliCihaz):

    def __init__(self, oda, sicaklik):
        super().__init__(oda)
        self.sicaklik = sicaklik

    def sicaklik_ayarla(self, sicaklik):
        self.sicaklik = sicaklik

class KahveMakinesi(AkilliCihaz):
    pass

class GuvenlikKamerasi(AkilliCihaz):

    def kayit_baslat(self):
        if not self.acik:
            self.acik = True
    
    def kayit_sonlandir(self):
        if self.acik:
            self.acik = False


salon_isigi = Isik("Salon", "Kirmizi")
klima = Klima("Oturma odasi", 22)
kahve_makinesi = KahveMakinesi("Mutfak")
kamera = GuvenlikKamerasi("Cocuk odasi")

klima.sicaklik_ayarla(24)
print(klima.sicaklik)

salon_isigi.renk_degistir("Beyaz")
print(salon_isigi.renk)

kahve_makinesi.ac()
print(kahve_makinesi.acik)

kamera.kayit_baslat()
print(kamera.acik)