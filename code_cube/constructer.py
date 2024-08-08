# Constructer yapıcı fonksiyonlar

class Cokgen:
    def __init__(self,g,y):
        self.genislik = g
        self.yukseklik = y

    def alan(self):
        return self.genislik * self.yukseklik


diktortgen = Cokgen(20,10)
# print(diktortgen)

print(diktortgen.genislik , " - ", diktortgen.yukseklik)
print(diktortgen.alan())
diktortgen.alan()