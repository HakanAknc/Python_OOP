class Urun:

    def __init__(self):
        self.__fiyat = 1000  # fiyat değişkeni __ ile kapsulleme yapılmış oldu

    def fiyat_yaz(self):
        print("Ürün fiyati : ", self.__fiyat)

    def set_fiyat(self,fiyat):
        self.__fiyat = fiyat

    
u = Urun()
u.fiyat_yaz()
u.__fiyat = 900
u.fiyat_yaz()

u.set_fiyat(500)
u.fiyat_yaz()