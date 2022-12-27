from math import*

def Trapezoid(a,b,f):
    n = 1000
    def trapezoid(f,a,b,n=1000):
        h=(b-a)/n
        sum = 0.0
        for i in range (1,n):
            x = a+i*h
            sum = sum +f(x)
        integral = (h/2)*(f(a)+2*sum+f(b))
        return integral
    integral = trapezoid(f,a,b,n)
    print(a,",",b,",",round(integral,2))

for i in range(0,3):
    Trapezoid(i+1,i+4,lambda x : x**4*2*5+7)

for i in range(0,1):
    Trapezoid(i+1,i+4,lambda x : 4*x*2*2+12)

for i in range(0,5):
    Trapezoid(i+1,i+4,lambda x : x**4*2*1+4)

for i in range(0,2):
    Trapezoid(i+1,i+4,lambda x : x**2*2*5+11)

for i in range(0,4):
    Trapezoid(i+1,i+4,lambda x : 4*x**2*5+5)

for i in range(0,2):
    Trapezoid(i+1,i+4,lambda x : x**6*2*5+3)

for i in range(0,1):
    Trapezoid(i+1,i+4,lambda x : 4*x**2*2*5+2)

for i in range(0,3):
    Trapezoid(i+1,i+4,lambda x : 2*x**5+1)

for i in range(0,1):
    Trapezoid(i+1,i+4,lambda x : 5*x**2*4+4)

for i in range(0,1):
    Trapezoid(i+1,i+4,lambda x : 2*2*x**5+6)
