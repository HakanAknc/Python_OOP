"""
Self: Burdaki selfin anlamı şu:
Ben bir obje oluşturdum ve bir de metot oluşturdum
o selfi kullanarak bu metotdun içinde objeme ait yani classıma ait 
variable'leri kullanmak istiyorsun.
"""
# edge = 5

class Square(object):

    edge = 5  # metre
    area = 0 

    def area1(self):
        self.area = self.edge * self.edge
        print("area: ", self.area)

s1 = Square()

print(s1)
print(s1.edge)
print(s1.area1())

s1.edge = 7
s1.area1()