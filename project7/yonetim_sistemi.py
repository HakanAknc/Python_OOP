from abc import ABC, abstractmethod

# Soyut Sınıf
class Calisan(ABC):
    def __init__(self, isim, saatlik_ucret):
        self.isim = isim
        self.saatlik_ucret = saatlik_ucret

    @abstractmethod
    def maas_hesapla(self):
        pass

# Tam Zamanlı Çalışan Sınıfı
class TamZamanliCalisan(Calisan):
    def __init__(self, isim, saatlik_ucret, aylik_saat):
        super().__init__(isim, saatlik_ucret)
        self.aylik_saat = aylik_saat

    def maas_hesapla(self):
        return self.saatlik_ucret * self.aylik_saat

# Yarı Zamanlı Çalışan Sınıfı
class YarimZamanliCalisan(Calisan):
    def __init__(self, isim, saatlik_ucret, calisma_saatleri):
        super().__init__(isim, saatlik_ucret)
        self.calisma_saatleri = calisma_saatleri

    def maas_hesapla(self):
        toplam_saat = sum(self.calisma_saatleri)
        return self.saatlik_ucret * toplam_saat

# Örnek Kullanım
if __name__ == "__main__":
    # Tam zamanlı çalışan
    tam_zamanli = TamZamanliCalisan("Ali", 50, 160)  # 160 saat çalışıyor
    # Yarı zamanlı çalışan
    yarim_zamanli = YarimZamanliCalisan("Ayşe", 30, [20, 25, 15, 30])  # Haftalık çalışma saatleri

    print(f"{tam_zamanli.isim}'in maaşı: {tam_zamanli.maas_hesapla()} TL")
    print(f"{yarim_zamanli.isim}'in maaşı: {yarim_zamanli.maas_hesapla()} TL")
