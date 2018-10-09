import sympy as sp 
from sympy import exp

x   = sp.symbols('x')
exp = sp.symbols('exp')

f = (exp)^(2*x) + (x)^(3) + 3

print(sp.diff(f,x,exp))
