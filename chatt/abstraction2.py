"""
Soyutlama (Abstraction) Nedir?
Soyutlama, karmaşık sistemlerin veya nesnelerin iç detaylarını gizleyerek, sadece gerekli ve önemli bilgileri sunmaktır. 
"""

"""
Basit Bir Örnek
Gerçek Hayat Örneği: Araba
Bir arabanın içinde birçok karmaşık parça ve mekanizma vardır: motor, şanzıman, frenler vb. Ancak, arabanın içini bilmek zorunda kalmadan, sadece direksiyonunu çevirir, gaz pedalına basar ve fren yaparsınız.

Soyutlama: Arabanın iç detayları sizin için soyutlanmış durumda. Sadece arabayı nasıl kullanacağınızı bilmeniz yeterlidir.
Detaylar: Motorun nasıl çalıştığı, şanzımanın nasıl dişlendiği gibi detayları bilmenize gerek yoktur.
"""

from abc import ABC, abstractmethod

# Soyut sınıf
class Hayvan(ABC):
    @abstractmethod
    def ses_cikar(self):
        pass

# Alt sınıf: Hayvan sınıfından türetilmiş
class Kedi(Hayvan):
    def ses_cikar(self):
        return "Miyav"

# Alt sınıf: Hayvan sınıfından türetilmiş
class Köpek(Hayvan):
    def ses_cikar(self):
        return "Hav"


def hayvan_sesi_al(hayvan):
    print(hayvan.ses_cikar())

kedi = Kedi()
köpek = Köpek()

hayvan_sesi_al(kedi)  # Miyav
hayvan_sesi_al(köpek) # Hav
