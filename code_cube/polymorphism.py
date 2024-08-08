class Kedi:
    def ses(self):
        print("miyav")

class Kopek:
    def ses(self):
        print("hav hav")

class Kus:
    def ses(self):
        print("cik cik")

def hayvan_sesi(hayvan):
    hayvan.ses()


ke = Kedi()
ko = Kopek()
ku = Kus()


hayvan_sesi(ke)
hayvan_sesi(ko)
hayvan_sesi(ku)


# sınıf içinde ortak isimle taımladığım metotlar yada fosnkiyonları ana alanda tanımladığım bir fonksiyonla kullanabiliyorum