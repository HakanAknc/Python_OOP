from abc import ABC, abstractmethod
import math

class Sekil(ABC):
    @abstractmethod
    def alan(self):
        pass

class Dikdortgen(Sekil):
    def __init__(self, uzunluk, genislik):
        self.uzunluk = uzunluk
        self.genislik = genislik

    def alan(self):
        return self.uzunluk * self.genislik
    
class Daire(Sekil):
    def __init__(self,yaricap):
        self.yaricap = yaricap

    def alan(self):
        return math.pi * (self.yaricap ** 2)
    

# Diktörtgen nesnesi oluşturdum
diktortgen = Dikdortgen(10, 5)
print(f"Dikdörtgen Alanı: {diktortgen.alan()}")
print("-------------------------------------")
# Daire nesnesi oluşturma
daire = Daire(7)
print(f"Daire Alanı: {daire.alan()}")