class Emp(object):

    age = 25
    salary = 1000

    def ageSalaryRatio(self):               # metot
        print("metot: " ,self.age / self.salary)

e1 = Emp()
print(e1.ageSalaryRatio())

# ----------------------------------------------------

def ageSalaryRatio(age, salary):            # fonksiyon
    a = age / salary
    print("fonksiyon: " ,a)

ageSalaryRatio(10,100)

