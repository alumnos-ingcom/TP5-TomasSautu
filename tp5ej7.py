################
# Tomás Sautú - @TomasSautu
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from utilidades import ingreso_real

def distancia(numeroUno, numeroDos):
    distancia = 0
    if numeroUno > numeroDos:
        menor = numeroDos
        mayor = numeroUno
    else:
        menor = numeroUno
        mayor = numeroDos
    
    distancia = mayor - menor
    distancia = round(distancia, 1)
    
    return distancia
    
        


def prueba():
    print("Ingrese dos números para medir la distancia entre el primero y el segundo")
    numero_1 = ingreso_real("Ingrese el primer número: ")
    numero_2 = ingreso_real("Ingrese el segundo número: ")
    resultado = distancia(numero_1, numero_2)
    print(f"La distancia entre {numero_1} y {numero_2} es de {resultado}")

if __name__ == "__main__":
    prueba()

