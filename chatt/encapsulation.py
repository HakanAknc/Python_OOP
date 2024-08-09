
# ! 2. Kapsülleme (Encapsulation)
# ! Kapsülleme, bir nesnenin durumunu (değişkenler) ve davranışlarını (metotlar) saklamayı ve dışarıdan erişimi sınırlamayı sağlar. 
# ! Python'da, değişken ve metotları gizlemek için __ (çift alt çizgi) kullanılır.

class Araba:
    def __init__(self, marka, model, renk):
        self.__marka = marka       # Gizle (private) özellik
        self.model = model
        self.renk = renk


    def get_marka(self):          # Gizli özelliği almak için bir metot
        return self.__marka
    
    def set_marka(self, marka):   # Gizli özelliğe ulaşmak için bir metot
        self.__marka = marka

# Araba nesnesi oluşturalım
araba1 = Araba("Honda", "Civciv" ,"Kirmiz")
print(araba1.get_marka())   # Çıktı : Honda

# araba2 = Araba("Mercedes", "G63", "Siyah")
# print(araba2.get_marka())

araba1.__marka = "BMW"
araba1.get_marka()

print("Yeni Araç")

araba1.set_marka("Fiat")
print(araba1.get_marka())