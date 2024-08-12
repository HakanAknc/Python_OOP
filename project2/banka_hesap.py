class BankaHesabi:
    def __init__(self, isim, baslangic_bakiyesi):
        self.isim = isim
        self.__bakiye = baslangic_bakiyesi     # Kapsülleme (__ ile korunuyor)

    def para_yatir(self, miktar):
        if miktar > 0:
            self.__bakiye += miktar
            print(f"{miktar} TL yatırıldı")
        else:
            print("Yatırılacak miktar sıfırdan büyük olmalı.")

    def para_cekme(self, miktar):
        if miktar > 0:
            if miktar <= self.__bakiye:
                self.__bakiye -= miktar
                print(f"{miktar} TL çekildi.")
            else:
                print("Yetersiz bakiye.")
        else:
            print("Çekilecek miktar sıfırdan büyük olmalı.")

    def bakiye_goster(self):
        return f"Hesap Sahibi: {self.isim}, Bakiye: {self.__bakiye} TL"
    
hesap = BankaHesabi("Hakan", 1000)

hesap.para_yatir(500)
print(hesap.bakiye_goster())

hesap.para_cekme(300)
print(hesap.bakiye_goster())

hesap.para_cekme(1500)
print(hesap.bakiye_goster())
