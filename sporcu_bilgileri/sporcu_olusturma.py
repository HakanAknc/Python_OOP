class Sporcu:
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas
        self.antrenmanprogrami = None
        self.saglikbilgileri = None

    def saglik_bilgileri_ata(self, saglik_bilgileri):
        self.saglikbilgileri = saglik_bilgileri

    def antrenman_programi_ata(self, antrenman_programi):
        self.antrenmanprogrami = antrenman_programi

    def performansi_goster(self):
        return f"{self.isim} - {self.yas} - {self.antrenmanprogrami} - {self.saglikbilgileri}"
    
class AntrenmanProgrami:
    def __init__(self, aktiviteler):
        self.aktiviteler = aktiviteler
    
    def __str__(self):
        return f"{', '.join(self.aktiviteler)}"

class SaglikBilgileri:
    def __init__(self, kilo, boy, nabiz, kanbasinci):
        self.kilo = kilo
        self.boy = boy
        self.nabiz = nabiz
        self.kanbasinci = kanbasinci
    
    def __str__(self):
        return f"Kilo: {self.kilo}, Boy: {self.boy}, Nabiz: {self.nabiz}, Kan basinci: {self.kanbasinci}"

ahmet = Sporcu("Ahmet", 30)
ahmetin_antrenman_programi = AntrenmanProgrami(["Kosu", "Agirlik Antrenmani", "Esneme Egzersizleri"])
ahmetin_saglik_bilgileri = SaglikBilgileri(80, 180, 70, "120/70")

ahmet.saglik_bilgileri_ata(ahmetin_saglik_bilgileri)
ahmet.antrenman_programi_ata(ahmetin_antrenman_programi)

print(ahmet.performansi_goster())