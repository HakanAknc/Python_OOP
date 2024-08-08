# initializer or constructor = __init__


class Animal(object):

    

    def __init__(self, a, b):   # (name, age) = ("dog", 2)
        self.name  = a
        self.age = b

    def getAge(self):
        return self.age
    
    def getName(self):
        print(self.name)
    
a1 = Animal("dog",2)
a2 = Animal("cat",4)
a3 = Animal("bird",6)

a1.getName()
a2.getName()
a3.getName()