class Sporcu:
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas
        self.antranmanprogrami = None
        self.saglikbilgileri = None

    def saglik_bilgileri_ata(self, saglik_bilgileri):
        self.saglikbilgileri = saglik_bilgileri

    def antrenman_programi_ata(self, antrenman_programi):
        self.antranmanprogrami = antrenman_programi

    def performansi_goster(self):
        return f"{self.isim} - {self.yas} - {self.antranmanprogrami} - {self.saglikbilgileri}"
    
class AntrenmanProgrami:
    def __init__(self, aktiviteler):
        self.aktiviteler = aktiviteler
    
    def __str__(self):
        return f"{', '.join(self.aktiviteler)}"   # Aktiviteleri virgülle ayrılmış bir liste olarak gösterir.
 
class SaglikBilgilerli:
    def __init__(self, kilo, boy, nabiz, kanbasinci):
        self.kilo = kilo
        self.boy = boy
        self.nabiz = nabiz
        self.kanbasinci = kanbasinci

    def __str__(self):
        return f"Kilo: {self.kilo}, Boy: {self.boy}, Nabiz: {self.nabiz}, Kan basinic: {self.kanbasinci}"
    

p1 = Sporcu("Hakan", 22)
# print(p1)

p1_antrenman_programi = AntrenmanProgrami(["Koşu", "Ağırlık Antrenmani", "Esneme Egzersizleri"])
p1_saglik_bilgileri = SaglikBilgilerli(80, 180, 70, "120/70")

p1.antrenman_programi_ata(p1_antrenman_programi)
p1.saglik_bilgileri_ata(p1_saglik_bilgileri)

print(p1.performansi_goster())