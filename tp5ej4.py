################
# Tomás Sautú - @TomasSautu
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from utilidades import ingreso_entero

def num_perfecto(numero):
    perfecto = False
    suma = 0
    lista = []
    for i in range(1, numero):
        if numero % i == 0:
            lista.append(i)
            suma = suma + i
            
        
        if suma == numero:
            perfecto = 1
        else:
            perfecto = -1
    return perfecto, lista
            


def prueba():
    numero = ingreso_entero("Ingrese un número para saber si es un número perfecto o no: ")
    perfecto, lista= num_perfecto(numero)
    if perfecto == 1:
        print(f"El número {numero} es perfecto, la suma de sus divisores {lista} es igual a {numero}")
    else:
        print(f"El número {numero} no es perfecto")
    

if __name__ == "__main__":
    prueba()
