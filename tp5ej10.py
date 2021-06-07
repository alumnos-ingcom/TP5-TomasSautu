################
# Tomás Sautú - @TomasSautu
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from utilidades import ingreso_entero

def numero_binario(numero):
    binario = []
    if numero > 0:
        while numero > 0:
            num_binario = numero % 2
            text_binario = str(num_binario)
            binario.append(text_binario)
            numero = numero // 2
    else:
        binario.append("0")
    binario = "".join(binario[::-1])
    return binario

def binario_numero(binario):
    cifras = []
    binarioTxt = str(binario)
    suma = 0
    for i in binarioTxt:
        cifras.append(i)
    cifras.reverse()
    for i in range(len(cifras)):
        if cifras[i] == '1':
            suma += 2**i
    return suma

def prueba():
    funcion = ingreso_entero(""""Si quiere convertir un número entero positivo a binario ingrese 1
Si quiere convertir un binario a número entero ingrese 2

#""")
    if funcion == 1 or funcion == 2:
        if funcion == 1:
            numero = ingreso_entero("Ingrese un número entero positivo para convertirlo en binario: ")
            if numero >= 0:
                binario = numero_binario(numero)
                print(f"El número entero {numero} convertido en binario es: {binario}")
            else:
                print("El número tiene que ser un entero positivo")
        else:
            binario = ingreso_entero("Ingrese el número binario para convertirlo a número entero: ")
            numero = binario_numero(binario)
            print(f"El número binario {binario} convertido es {numero}")
            
    else:
        print("No es una opción para el programa")

if __name__ == "__main__":
    prueba()
