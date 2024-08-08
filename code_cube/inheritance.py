class Kus:                #super sınıf  - ana sınıf
    tur_ad = " "
    kus_ad = " "

    def isim_yaz(self):
        print("Tür ad: ", self.tur_ad)
        print("Kuş isim: ", self.kus_ad)

class Yirtici(Kus):      #subclass - alt sınıf
    kanat_uzunlugu = "0"
    agirlik = "0"

    def degerler(self):
        print("Kanat : ",self.kanat_uzunlugu)

class Kartal(Yirtici):
    alt_tür = " "


anadolu_kartali = Kartal()
anadolu_kartali.tur_ad = "Anatolya"
anadolu_kartali.kus_ad = "siyah kartal"

anadolu_kartali.kanat_uzunlugu = "1.5 m"
anadolu_kartali.agirlik = "6 kg"
anadolu_kartali.alt_tür = "mider east"

anadolu_kartali.isim_yaz()
anadolu_kartali.degerler()