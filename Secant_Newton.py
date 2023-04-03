from sympy import *

# Symbol
x = symbols('x')

MAX_STEPS_ALLOWED = 30


def no_roots_found(f, x0, f_x0, step):
    return print(
        "\n\t[ERROR] No se pudo encontrar una raíz para la función \" %s \" " % f +
        "luego de %d pasos." % step +
        "\n\t\t* Último valor x analizado: %.4f" % x0 +
        "\n\t\t* Ultimo f(x): %.4f" % f_x0
    )


# Newton fun
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

    # Der Fun
    df = funcion.diff(x)

    if df == 0:
        return print("No converge o lo hara con gran error ya que la derivada de la funcion es Cero")

    f_x0 = funcion.subs({x: x0}).evalf()

    print(
        "\tNewton:\n"
        "\t\tEl valor encontrado en el paso %d" % step + " es %.4f" % x0 + ".\n" +
        "\t\tEl valor de la funcion con ese valor es: ~%.4f" % f_x0 +
        "\n"
    )

    if Abs(funcion.subs({x: x0}).evalf()) <= epsilon + 0 * I:
        return print("La raiz es : ", "%.4f" % x0, ". Evaluada en la funcion es: ",
                     "~%.4f" % f_x0, ". \n En: ", step, "pasos.")
    else:
        if step >= MAX_STEPS_ALLOWED:
            return no_roots_found(f, x0, f_x0, step)
        x1 = x0 + 1
        return my_secant(f, x0 - ((funcion / df).subs({x: x0}).evalf()), x0, epsilon, step)


# Secant Fun
def my_secant(f, x0, x1, e, step):
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

    if (funcion.subs(x, x0)).evalf() == (funcion.subs(x, x1)).evalf():
        return print('No puede dividir por cero!')
    else:
        x2 = x0 - (x1 - x0) * (funcion.subs(x, x0)).evalf() / (
                (funcion.subs(x, x1)).evalf() - (funcion.subs(x, x0)).evalf())

        # x0 = x1
        # x1 = x2

        f_x2 = funcion.subs(x, x2).evalf()

        print(
            "\tSecante:\n"
            "\t\tEl valor encontrado en el paso %d" % step + " es %.4f" % x2 + "\n" +
            "\t\tEl valor de la funcion con ese valor es: ~%.4f" % f_x2 +
            "\n"
        )


        if abs((funcion.subs(x, x2)).evalf()) <= e:
            return print("La raiz es : ", "%.4f" % x2, ". Evaluada en la funcion es: ",
                         "~%.4f" % f_x2, ". \n En: ", step, "pasos.")
        else:
            if step >= MAX_STEPS_ALLOWED:
                return no_roots_found(f, x0, f_x2, step)
            return my_newton(f, x0, epsilon, step)


# Input - User
print("*******************************************")
print("Bienvenido al Programa de Busqueda de Ceros")
print("*******************************************")
option = -1
while option != 1 and option != 2:
    option = int(input("¿Con qué metodo desea comenzar?\n"
                       "\tComenzar por el Metodo Newton (Presione 1)\n"
                       "\tComenzar por el Metodo de Secante (Presione 2)\n"))
    if option == 1:
        print("Ud selecciono el Metodo Newton \n")
    elif option == 2:
        print("Ud selecciono el Metodo Secante \n")
    else:
        print("Ud ingreso un caracter invalido \n")
step = 0
fun = input("Ingrese su funcion \n")
epsilon = 0.0001
epsilonChange = 0
while epsilonChange != 1 and epsilonChange != 2:
    epsilonChange = int(input("El margen de error ha sido definido en 3 decimales:\n"
                              "\tCambiarlo (Presione 1)\n"
                              "\tDejarlo como está (Presione 2)\n"))
    if epsilonChange == 1:
        epsilonOption = 0
        while epsilonOption != 1 and epsilonOption != 2:
            epsilonOption = int(input("El margen de error puede cambiarse a:\n"
                                      "\t2 decimales (Presione 1)\n"
                                      "\t4 decimales (Presione 2)\n"))
            if epsilonOption == 1:
                print("Ud selecciono 2 decimales. \n")
                epsilon = 0.001
            elif epsilonOption == 2:
                print("Ud selecciono 4 decimales. \n")
                epsilon = 0.00001
            else:
                print("Ud ingreso un caracter invalido. \n")
    elif epsilonChange == 2:
        epsilon = 0.0001
    else:
        print("Ud ingreso un caracter invalido. \n")

input_x0 = None
input_x1 = None

if option == 1:
    while input_x0 is None:
        input_x0 = int(input("\nIngrese un valor X0 para comenzar: "))
elif option == 2:
    while input_x0 is None:
        input_x0 = int(input("\nIngrese un valor X0 inicial para comenzar: "))
    while input_x1 is None:
        input_x1 = int(input("\nIngrese un valor X1 final para comenzar: "))
print("")

# Ingreso de funcion a los Metodos
if option == 1:
    my_newton(fun, input_x0, epsilon, step)
elif option == 2:
    my_secant(fun, input_x0, input_x1, epsilon, step)
