#diket : p(t)=6*t**2+2*t+5, p(0)=50
#ditanya : p(5)
#jawab :
p0=50
def p(t):
    return 6*t**2+2*t+5
from sympy import *
t = Symbol("t")
pd = 6*t**2+2*t+5
integ = integrate(pd, t)
print("P'(t) = ", integ+p0)
from scipy import integrate
value = integrate.quad(p, 0, 5)
print("p(5) = ",value[0]+p0)
