from abc import ABC, abstractmethod

class Calisan(ABC):
    def __init__(self, isim, id_no, maas):
        self.isim = isim
        self.id_no = id_no
        self._maas = maas  # Kapsüllenmiş özellik

    @abstractmethod
    def bilgi_goster(self):
        pass

    @abstractmethod
    def maas_hesapla(self):
        pass

    def __str__(self):
        return f"İsim: {self.isim}, ID: {self.id_no}"


class Yonetici(Calisan):
    def __init__(self, isim, id_no, maas, departman):
        super().__init__(isim, id_no, maas)
        self.departman = departman
        self._yonetim_kapsaminda = []  # Yönettiği çalışanlar

    def bilgi_goster(self):
        return f"Yönetici: {self.isim}, ID: {self.id_no}, Departman: {self.departman}"

    def maas_hesapla(self):
        return self._maas * 1.2  # Yönetici maaşı %20 artışlı

    def calisan_ekle(self, calisan):
        self._yonetim_kapsaminda.append(calisan)

    def calisanlari_goster(self):
        for calisan in self._yonetim_kapsaminda:
            print(calisan)

class Yazilimci(Calisan):
    def __init__(self, isim, id_no, maas, projeler):
        super().__init__(isim, id_no, maas)
        self.projeler = projeler

    def bilgi_goster(self):
        return f"Yazılımcı: {self.isim}, ID: {self.id_no}, Projeler: {', '.join(self.projeler)}"

    def maas_hesapla(self):
        return self._maas  # Yazılımcı maaşı sabit

class Tasarimci(Calisan):
    def __init__(self, isim, id_no, maas, tasarim_stili):
        super().__init__(isim, id_no, maas)
        self.tasarim_stili = tasarim_stili

    def bilgi_goster(self):
        return f"Tasarımcı: {self.isim}, ID: {self.id_no}, Tasarım Stili: {self.tasarim_stili}"

    def maas_hesapla(self):
        return self._maas * 1.1  # Tasarımcı maaşı %10 artışlı

class CalisanYonetimi:
    def __init__(self):
        self.calisanlar = []

    def calisan_ekle(self, calisan):
        self.calisanlar.append(calisan)

    def calisan_bilgilerini_goster(self):
        for calisan in self.calisanlar:
            print(calisan.bilgi_goster())

    def calisan_maaslarini_goster(self):
        for calisan in self.calisanlar:
            print(f"{calisan.isim}: {calisan.maas_hesapla()} TL")

# Örnek Kullanım
if __name__ == "__main__":
    yonetici1 = Yonetici("Ayşe", "Y001", 8000, "Yazılım")
    yazilimci1 = Yazilimci("Mehmet", "Y002", 6000, ["Proje A", "Proje B"])
    tasarimci1 = Tasarimci("Ali", "T001", 5000, "Modern")

    yonetici1.calisan_ekle(yazilimci1)
    yonetici1.calisan_ekle(tasarimci1)

    yonetim = CalisanYonetimi()
    yonetim.calisan_ekle(yonetici1)
    yonetim.calisan_ekle(yazilimci1)
    yonetim.calisan_ekle(tasarimci1)

    print("Çalışan Bilgileri:")
    yonetim.calisan_bilgilerini_goster()

    print("\nÇalışan Maaşları:")
    yonetim.calisan_maaslarini_goster()
