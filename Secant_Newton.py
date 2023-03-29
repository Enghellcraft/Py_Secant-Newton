import numpy as np
import sympy as sp
from sympy import *

#Symbol
x = symbols('x')

#Newton fun
def my_newton(f, x0, e):
    # output is an estimation of the root of f 
    # using the Newton method
    # recursive implementation
    df=diff(f,x,1)
    
    print(x0)
    
    if Abs((f.subs(x,x0)).evalf()) < e+0*I:
        return x0
    else:
       return my_newton(f, x0 - ((f/df).subs(x,x0).evalf()), e)
   
# Secant Fun
def my_secant(f,x0,x1,e,N):
    step = 1
    condition = True
    while condition:
        if (f.subs(x,x0)).evalf() == (f.subs(x,x1)).evalf():
            print('Divide by zero error!')
            break
        
        x2 = x0 - (x1-x0)*(f.subs(x,x0)).evalf()/( (f.subs(x,x1)).evalf() - (f.subs(x,x0)).evalf() ) 
        print('Iteration %d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, (f.subs(x,x2)).evalf()))
        x0 = x1
        x1 = x2
        step = step + 1
        
        if step > N:
            print('Not Convergent!')
            break
        
        condition = abs((f.subs(x,x2)).evalf()) > e
    return(x2)