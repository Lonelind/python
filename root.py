import cmath

n = input("Input n: ")
pi = cmath.pi
d = 0

for i in range (0,n) :
    a = complex(cmath.cos(2*pi*i/n),-cmath.sin(2*pi*i/n))
    print a
