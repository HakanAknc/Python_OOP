# calculator project

class Clac(object):

    # init metodu
    def __init__(self, a, b):
        "initialize values"
        
        # attribute
        self.value1 = a
        self.value2 = b

    def add(self):
        "addition a+b = result -> return result"
        return self.value1 + self.value2

    def multiply(self):
        "multiplication a*b = result -> return result"
        return self.value1 * self.value2
    
    def bol(self):
        return self.value1 / self.value2

while True:    
    print("Choose add(1), multiply(2) Bol(3)")
    selection = input("select 1 or 2 or 3  :  ")

    v1 = int(input("first value: "))
    v2 = int(input("second value: "))

    c1 = Clac(v1,v2)

    if selection == "1":
        add_result = c1.add()
        print("Add: {}".format(add_result))
    elif selection == "2":
        multiply_result = c1.multiply()
        print("Multiply: {}".format(multiply_result))
    elif selection == "3":
        bol_result = c1.bol()
        print("Bölüm : ",format(bol_result))
    else:
        print("Yanlış seçim..")