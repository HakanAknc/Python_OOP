
# ! 3. Miras (Inheritance)
# ! Miras, bir sınıfın başka bir sınıfın özelliklerini ve metotlarını devralmasını sağlar. 
# ! Bu sayede kod tekrarından kaçınılır ve esneklik sağlanır.

# # Temel bir Araç sınıfı tanımlayalım
class Arac:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
    
    def bilgi(self):
        return f"{self.marka} {self.model}"
    
# Araba sınıfı, Araç sınıfından miras alır.
class Araba(Arac):
    def __init__(self, marka, model, renk):
        super().__init__(marka, model)   # Üst sınıfın yapıcısını çağırır
        self.renk = renk

    def bilgi(self):
        return f"{self.marka} {self.model} {self.renk}"
    
# Motosiklet sınıfı, Araç sınıfından miras alır
class Motosiklet(Arac):
    def __init__(self, marka, model, cc):
        super().__init__(marka, model)
        self.cc = cc

    def bilgi(self):
        return f"{self.marka} {self.model} {self.cc}cc"
    
# Araba ve Motosiklet nesneleri oluşturalım
araba1 = Araba("Ford", "Mustanga", "Siyah")
motosiklet1 = Motosiklet("Yamaha", "R1", 998)

print(araba1.bilgi())
print(motosiklet1.bilgi())
