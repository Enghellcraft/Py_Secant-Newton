import numpy as np
import sympy as sp
from sympy import *

#Symbol
x = symbols('x')

#Newton fun

def my_newton(f, x0, e, step):
    # output es un estimado de la raiz de la funcion ingresada
    # Tiene implementada la funcion como recursiva
    # f = funcion ingresada
    # X0 = valor de inicio para la funcion (ideal cercano a la raiz)
    # e = epsilon o margen de error permitido
    
    step = step + 1
    
    df=diff(f,x,1)
    
    if df == 0:
        print("No congerge o lo hara con gran error ya que la derivada de la funcion es Cero")
    
    print("El valor encontrado en el paso ", step, "es", x0, ". \n El valor de la funcion con ese valor es:", (f.subs(x,x0)).evalf())
    
    if Abs((f.subs(x,x0)).evalf()) < e+0*I:
        return x0
    else:
       return my_newton(f, x0 - ((f/df).subs(x,x0).evalf()), e)
   
# Secant Fun
def my_secant(f,x0,x1,e, step):
    # output es un estimado de la raiz de la funcion ingresada
    # Tiene implementada la funcion como recursiva
    # f = funcion ingresada
    # X0 = valor de inicial para la funcion
    # X1 = valor de final para la funcion
    # e = epsilon o margen de error permitido

    step = step + 1

    condition = True
    while condition:
        if (f.subs(x,x0)).evalf() == (f.subs(x,x1)).evalf():
            print('No puede dividir por cero!')
            break
        
        x2 = x0 - (x1-x0)*(f.subs(x,x0)).evalf()/( (f.subs(x,x1)).evalf() - (f.subs(x,x0)).evalf() ) 
        
        print('Iteration %d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, (f.subs(x,x2)).evalf()))
        print("El valor encontrado en el paso ", step, "es", x2, ". \n El valor de la funcion con ese valor es:", (f.subs(x,x2)).evalf())
        
        x0 = x1
        x1 = x2

        condition = abs((f.subs(x,x2)).evalf()) > e
    return(x2)

# Changing Methods Fun


#Input - User
print("*******************************************")
print("Bienvenido al Programa de Busqueda de Ceros")
print("*******************************************")
option = input("¿Desea comenzar por el Metodo Secante (Presione 1) \n o por el Metodo de Newton (Presione 2)")
while option != 1 | option != 2:
    step = 1
    if option == 1:
        print("Ud selecciono el Metodo Secante")
    elif option == 2:
        print("Ud selecciono el Metodo Newton")
    else :  
        print("Ud ingreso un caracter invalido")
fun = input("Ingrese su funcion")
epsilonChange = print("El margen de error ha sido definido en 3 decimales, si desea cambiarlo ingrese 0, sino ingrse 1")
if epsilonChange == 0 : 
    while option != 1 | option != 2:
        epsilonChange = print("El margen de error puede cambiarse a 2 decimales Opcion 1, o 4 decimales Opcion 2")
        if option == 1:
            print("Ud selecciono 2 decimales")
            epsilon = 0.001
        elif option == 2:
            print("Ud selecciono 4 decimales")
            epsilon = 0.00001
        else :  
            print("Ud ingreso un caracter invalido")
else :
    epsilon = 0.0001