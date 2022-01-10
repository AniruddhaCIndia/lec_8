print('we are going to evaluate the integral of 10-x^2')
print('provide the lower limit of integration')
a=float(input())
print('provide the upper limit of integration')
b=float(input())
h=(b-a)/100
def f(x):
    return (10-x**2)
f1=(f(a)+f(b))*h/2
f2=0
for i in range(100):
    f2=f2+f(a+i*h)*h
print(f1+f2)
