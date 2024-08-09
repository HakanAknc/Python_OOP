from abc import ABC, abstractmethod

# Soyut sınıf
class Hayvan(ABC):
    @abstractmethod
    def ses_cikar(self):
        pass

    @abstractmethod
    def hareket_et(self):
        pass

# Alt sınıf: Hayvan sınıfından türetilmiştir
class Kedi(Hayvan):
    def ses_cikar(self):
        return "Miyav"

    def hareket_et(self):
        return "Zıplıyor"

# Alt sınıf: Hayvan sınıfından türetilmiştir
class Köpek(Hayvan):
    def ses_cikar(self):
        return "Hav"

    def hareket_et(self):
        return "Koşuyor"


def hayvan_sesi_al(hayvan):
    print(hayvan.ses_cikar())

def hayvan_hareketi_al(hayvan):
    print(hayvan.hareket_et())

kedi = Kedi()
köpek = Köpek()

hayvan_sesi_al(kedi)  # Miyav
hayvan_sesi_al(köpek) # Hav

hayvan_hareketi_al(kedi)  # Zıplıyor
hayvan_hareketi_al(köpek) # Koşuyor
