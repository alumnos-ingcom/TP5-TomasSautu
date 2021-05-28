################
# Tomás Sautú - @TomasSautu
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from utilidades import ingreso_entero

def tribonacci(numero):
    termino_1 = 1
    termino_2 = 1
    termino_3 = 1
    lista = [termino_1, termino_2, termino_3]
    n_esimo = numero - 2
    for i in range(n_esimo-1):
        lista.append(lista[-1]+lista[-2]+lista[-3])
        resultado = lista[-1]
        
    return (lista, resultado)



def prueba():
    print("""Este programa sirve para calcular el n-esimo termino de la sucesión de Fibonacci que usted quiera.
El número debe ser un entero positivo mayor a 3.
    """)
    numero = ingreso_entero("Ingrese un número para calcular su n-esimo termino de Fibonacci: ")
    if numero > 3:
        lista, resultado = tribonacci(numero)
        print(f"El resultado es {resultado}, la sucesión es {lista}")
    else:
        print(f"El número {numero} no es mayor a 3.")

if __name__ == "__main__":
    prueba()

