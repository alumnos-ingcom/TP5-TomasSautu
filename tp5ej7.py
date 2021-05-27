################
# Tomás Sautú - @TomasSautu
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# def ingreso_real(mensaje):
#     """
#     Esta funcion muestra un mensaje para indicar el ingreso
#     de un número real.
#     """
#     ingreso = input(mensaje)
#     try:
#         real = float(ingreso)
#     except ValueError as err:
#         raise IngresoIncorrecto("No era un número genio!") from err
#     return real

from utilidades import ingreso_real

def distancia(numeroUno, numeroDos):
    distancia = 0
    if numeroUno > numeroDos:
        menor = numeroDos
        mayor = numeroUno
    else:
        menor = numeroUno
        mayor = numeroDos
    while menor < mayor:
        distancia = distancia + 0.1
        menor = menor + 0.1
    return distancia
    
        


def prueba():
    print("Ingrese dos números para medir la distancia entre el primero y el segundo")
    numero_1 = ingreso_real("Ingrese el primer número: ")
    numero_2 = ingreso_real("Ingrese el segundo número: ")
    resultado = distancia(numero_1, numero_2)
    print(f"La distancia entre {numero_1} y {numero_2} es de {resultado}")

if __name__ == "__main__":
    prueba()

