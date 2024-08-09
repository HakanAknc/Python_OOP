"""
super() Fonksiyonu
super() fonksiyonu, bir alt sınıfın (subclass) üst sınıfının (superclass) metodlarına erişmesini sağlar.
Genellikle alt sınıfta __init__ metodunu yeniden tanımlarken, üst sınıfın __init__ metodunu da çağırmak için kullanılır. 
Bu sayede, üst sınıfın özellikleri ve davranışları alt sınıfa aktarılabilir ve yeniden kullanılabilir.
"""

class Arac:                                 # superclass
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

class Araba(Arac):                          # subclass
    def __init__(self, marka, model, yil):
        super().__init__(marka, model)      # Üst sınıfın __init__'ini çağır yani tekrar "self.marka = marka" ve " self.model = model" tanımlamaya ihtiyaç duymuyoruz
        self.yil = yil

# Araba sınıfından bir nesne oluşturalım
araba1 = Araba("Honda", "Civic", 2019)

# Nesnenin özelliklerine erişelim
print(araba1.marka)  # Honda
print(araba1.model)  # Civic
print(araba1.yil)    # 2019


"""
u örnekte, Araba sınıfı Arac sınıfından türetilmiştir. Araba sınıfında super().__init__(marka, model) ifadesi ile 
Arac sınıfının __init__ metodu çağrılır, böylece marka ve model özellikleri Arac sınıfında tanımlanmış olur. 
Daha sonra Araba sınıfında yil özelliği eklenir.
"""