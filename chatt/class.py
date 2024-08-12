
# ! 1. Sınıflar ve Nesneler
# ! Sınıf (Class): Python'da sınıf, bir nesnenin özelliklerini ve davranışlarını tanımlayan bir yapıdır. 
# ! Örneğin, bir Araba sınıfı, bir arabanın marka, model, renk gibi özelliklerini ve hızlanma gibi davranışlarını tanımlayabilir.

# ! Nesne (Object): Sınıftan türetilen somut örnektir. Bir sınıf, bir kalıp olarak düşünülebilir ve nesne, bu kalıptan üretilen bir varlıktır.




class Araba:
    def __init__(self, id, marka, seri, renk, yil, yakit, durum, kilometre, motor_gucu):   # Yapıcı metod (constructor)
        self.id = id
        self.marka = marka
        self.seri = seri
        self.renk = renk
        self.yil = yil 
        self.yakit = yakit
        self.durum = durum
        self.kilometre = kilometre
        self.motor_gucu = motor_gucu

    def araba_bilgi(self):
        return f"{self.id} {self.marka} {self.seri} {self.renk} {self.yil} {self.yakit} {self.durum} {self.kilometre} {self.motor_gucu}"


# Araba sınıfından bir nesne oluşturalım
araba1 = Araba("1 - ", "Mercedes-Benz - ","G Serisi - ","Siyah - ","2023 - ","Benzin - ","İkinci el - "," 6.475 - "," 585 hp - ")
print(araba1)
print(type(araba1))

print(araba1.araba_bilgi())   # Çıktı