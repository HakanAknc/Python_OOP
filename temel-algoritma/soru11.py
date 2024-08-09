# 0 ile 1000 arasındaki Fibonacci sayılarını bulan programı yazınız?

# 1 - 1 - 2 - 3 - 5 - 8 - 13 - 21

a = 1
b = 1
c = 0

while c<1000:
    print(b)
    c = a + b
    a = b
    b = c