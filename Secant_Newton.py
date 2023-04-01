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
    
    epsilon = e
    
    step = step + 1

    x = symbols("x")
    
    funcion = sympify(f)
    
    #Der Fun
    df=funcion.diff(x)
    
    if df == 0:
        return print("No converge o lo hara con gran error ya que la derivada de la funcion es Cero")
    
    print("Newton: El valor encontrado en el paso ", step, "es", "%.4f" % x0, ". \n El valor de la funcion con ese valor es:", "~%.4f" % (funcion.subs({x: x0})).evalf())

    if Abs(funcion.subs({x: x0}).evalf()) <= epsilon+0*I:
        return print("La raiz es : ", "%.4f" % x0, ". Evaluada en la funcion es: ", "~%.4f" % (funcion.subs({x: x0})).evalf(), ". \n En: ", step, "pasos." )
    else:
        x1 = x0 + 1
        return my_secant(f, x0 - ((funcion/df).subs({x: x0}).evalf()), x0, epsilon, step)
   
# Secant Fun
def my_secant(f,x0,x1,e, step):
    # output es un estimado de la raiz de la funcion ingresada
    # Tiene implementada la funcion como recursiva
    # f = funcion ingresada
    # X0 = valor de inicial para la funcion
    # X1 = valor de final para la funcion
    # e = epsilon o margen de error permitido

    epsilon = e

    step = step + 1

    x = symbols("x")

    funcion = sympify(f)

    if (funcion.subs(x,x0)).evalf() == (funcion.subs(x,x1)).evalf():
        return print('No puede dividir por cero!')
    else: 
        x2 = x0 - (x1-x0)*(funcion.subs(x,x0)).evalf()/( (funcion.subs(x,x1)).evalf() - (funcion.subs(x,x0)).evalf() ) 
        
        # x0 = x1
        # x1 = x2
    
        print("Secante: El valor encontrado en el paso ", step, "es", "%.4f" % x2, ". \n El valor de la funcion con ese valor es:", "~%.4f" % (funcion.subs(x,x2)).evalf())

        if abs((funcion.subs(x,x2)).evalf()) <= e :
            return print("La raiz es : ", "%.4f" % x2, ". Evaluada en la funcion es: ", "~%.4f" % (funcion.subs(x,x2)).evalf(), ". \n En: ", step, "pasos.")
        else :
            return my_newton(f, x0, epsilon, step)


#Input - User
print("*******************************************")
print("Bienvenido al Programa de Busqueda de Ceros")
print("*******************************************")
option = -1
while (option != 1 and option != 2):
    option = int(input("¿Desea comenzar por el Metodo Newton (Presione 1) \n o por el Metodo de Secante (Presione 2) \n"))
    if option == 1:
        print("Ud selecciono el Metodo Newton \n")
    elif option == 2:
        print("Ud selecciono el Metodo Secante \n")       
    else:
        print("Ud ingreso un caracter invalido \n")
step = 0
fun = input("Ingrese su funcion \n")
epsilon = 0.0001
epsilonChange = -1
while epsilonChange != 0 and epsilonChange != 1:
    epsilonChange = int(input("El margen de error ha sido definido en 3 decimales, si desea cambiarlo ingrese 0, sino ingrese 1 \n"))
    if epsilonChange == 1 :
        epsilonOption = 0
        while epsilonOption != 1 and epsilonOption != 2:
            epsilonOption = int(input("El margen de error puede cambiarse a 2 decimales Opcion 1, o 4 decimales Opcion 2 \n"))
            if epsilonOption == 1:
                print("Ud selecciono 2 decimales \n")
                epsilon = 0.001
            elif epsilonOption == 2:
                print("Ud selecciono 4 decimales \n")
                epsilon = 0.00001
            else :  
                print("Ud ingreso un caracter invalido \n")
    elif epsilonChange == 0:
        epsilon = 0.0001
    else :  
        print("Ud ingreso un caracter invalido \n")
    
if option == 1: 
    input_x0 = int(input ("Ingrese un valor X0 para comenzar \n"))
elif option == 2:
    input_x0 = int(input ("Ingrese un valor X0 inicial para comenzar \n"))
    input_x1 = int(input ("Ingrese un valor X1 final para comenzar \n"))

#Ingreso de funcion a los Metodos
if option == 1: 
    my_newton(fun, input_x0, epsilon, step)
elif option == 2:
    my_secant(fun, input_x0, input_x1, epsilon, step)