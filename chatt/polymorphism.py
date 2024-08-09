
# ! 4. Çok Biçimlilik (Polymorphism)
# ! Çok biçimlilik, aynı metodun farklı sınıflar tarafından farklı şekillerde uygulanabilmesini sağlar.
# ! Polymorphism, aynı isimdeki metotların veya işlevlerin, farklı sınıflarda farklı şekillerde çalışabilmesini sağlar.
class Kus:
    def ses_cikar(self):
        return "Kuş cıvıldıyor"

class Serce(Kus):
    def ses_cikar(self):
        return "Serçe cıvıldıyor"

class Kartal(Kus):
    def ses_cikar(self):
        return "Kartal çığlık atıyor"

def ses_dinle(kus):
    print(kus.ses_cikar())

serce = Serce()
kartal = Kartal()

# Serçe ve Kartal sınıfları farklı ses çıkarır
ses_dinle(serce)  # Serçe cıvıldıyor
ses_dinle(kartal) # Kartal çığlık atıyor