from kitap import Kitap

class Kutuphane:
    def __init__(self):
        self.kitaplar = []

    def kitap_ekle(self, kitap):
        self.kitaplar.append(kitap)
        print(f"Kitap eklendi: {kitap.kitap_bilgisi()}")

    def kitaplari_listele(self):
        if not self.kitaplar:
            print("Kütüphanede kitap yok.")
        else:
            for kitap in self.kitaplar:
                print(kitap.kitap_bilgisi())

    def kitap_bul(self, baslik):
        for kitap in self.kitaplar:
            if kitap.baslik == baslik:
                return kitap
        return None