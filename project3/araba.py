class Arac:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil

    def arac_bilgileri(self):
        return f"Marka: {self.marka}, Model: {self.model}, Yıl: {self.yil}"
    

class ElektrikliArac(Arac):
    def __init__(self, marka, model, yil, batarya_kapasitesi):
        super().__init__(marka, model, yil)
        self.batarya_kapasitesi = batarya_kapasitesi

    def arac_bilgileri(self):
        genel_bilgiler = super().arac_bilgileri()
        return f"{genel_bilgiler}, Batarya Kapasitesi: {self.batarya_kapasitesi} kwh"
    
arac = Arac("Toyota", "Corolla", 2020)
print(arac.arac_bilgileri())

print("-----------------------------------------------------")

elektrikli_arac = ElektrikliArac("Tesla", "Model S", 2022, 100)
print(elektrikli_arac.arac_bilgileri())