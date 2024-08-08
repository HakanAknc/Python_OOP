class BankAccount(object):

    def __init__(self, name, money, address):
        self.name = name       # global
        self.__money = money     # private  = __money dersen gizler
        self.address = address
    
    # get and set
    def getMoney(self):
        return self.__money

    def setMoney(self, amount):
        self.__money = amount

p1 = BankAccount("messi",1000,"barcelona")
p2 = BankAccount("neymar",2000,"paris")

print("get method: ",p1.getMoney())
p1.setMoney(5000)
print("set method: ",p1.getMoney())