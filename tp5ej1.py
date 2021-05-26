################
# Tomás Sautú - @TomasSautu
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from utilidades import ingreso_entero

def par_impar(numero):
    while numero > 0:
        numero = numero - 2
    if numero == 0:
        return 1
    else:
        return -1
    


def prueba():
    numero = ingreso_entero("Ingrese un número, el programa le dirá si es par o impar: ")
    resultado = par_impar(numero)
    if resultado == 1:
        print(f"El número {numero} es PAR")
    else:
        print(f"El número {numero} es IMPAR")

if __name__ == "__main__":
    prueba()

