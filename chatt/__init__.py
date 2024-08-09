"""
 ? __init__ Metodu
__init__ metodu, Python'da bir sınıfın kurucu (constructor) metodudur. 
Bir sınıftan yeni bir örnek (instance) oluşturulduğunda otomatik olarak çağrılır.
Bu metodun amacı, sınıfın örneği oluşturulduktan sonra gerekli olan başlangıç değerlerini ayarlamaktır. 
Genellikle, bu metodun içinde sınıfın özellikleri (attributes) tanımlanır ve başlangıç değerleri atanır.

"""

class Araba:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil

# Araba sınıfından bir nesne oluşturalım
araba1 = Araba("Toyota", "Corolla", 2020)

# Nesnenin özelliklerine erişelim
print(araba1.marka)  # Toyota
print(araba1.model)  # Corolla
print(araba1.yil)    # 2020


"""
Bu örnekte, Araba sınıfından bir nesne oluşturulduğunda, __init__ metodu çalışır ve marka, model, yil gibi özellikler 
belirtilen değerlerle başlatılır.
"""