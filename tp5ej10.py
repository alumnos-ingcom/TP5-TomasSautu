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


def prueba():
    numero = ingreso_entero("Ingrese un número entero positivo para convertirlo en binario: ")
    if numero >= 0:
        binario = numero_binario(numero)
        print(f"El número entero {numero} convertido en binario es: {binario}")
    else:
        print("El número tiene que ser un entero positivo")

if __name__ == "__main__":
    prueba()
