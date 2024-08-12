class Hayvan:
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas

    def ses_cikar(self):
        return "Hayvan "
    
    def bilgileri_goster(self):
        return f"İsim: {self.isim}, Yaş: {self.yas}"
    
class Kedi(Hayvan):
    def __init__(self, isim, yas, cins):
        super().__init__(isim, yas)
        self.cins = cins

    def ses_cikar(self):
        return "Miyav"
    
    def bilgileri_goster(self):
        return f"İsim: {self.isim}, Yaş: {self.yas}, Cins: {self.cins}"
    
class Kopek(Hayvan):
    def __init__(self, isim, yas, cins):
        super().__init__(isim, yas)
        self.cins = cins

    def ses_cikar(self):
        return "Hav Hav"
    
    def bilgileri_goster(self):
        return f"İsim: {self.isim}, Yaş: {self.yas}, Cins: {self.cins}"
    

class Kus(Hayvan):
    def __init__(self, isim, yas, cins):
        super().__init__(isim, yas)
        self.cins = cins

    def ses_cikar(self):
        return "Cik Cik"
    
    def bilgileri_goster(self):
        return f"İsim: {self.isim}, Yaş: {self.yas}, Cins: {self.cins}"
    

kedi = Kedi("Minnal", 3, "Tekir")
kopek = Kopek("Karabaş", 5, "Golden Retriever")
kus = Kus("Maviş", 2, "Muhabbet Kuşu")

# Ses çıkarma ve bilgileri gösterme
print(kedi.ses_cikar())  # Miyav
print(kedi.bilgileri_goster())
print("-------------------------")
print(kopek.ses_cikar())
print(kopek.bilgileri_goster())
print("-------------------------")
print(kus.ses_cikar())
print(kus.bilgileri_goster())