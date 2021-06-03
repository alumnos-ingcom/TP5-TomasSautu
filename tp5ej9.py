################
# Tomás Sautú - @TomasSautu
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from time import time

def factorial(numero):
    resultados = []
    cifras = []
    numeros = str(numero)
    for i in numeros:
        cifras.append(i)
    for i in cifras:
        producto = 1
        numero_cifra = int(i)
        for i in range(1, numero_cifra+1):
            producto *= i
        resultados.append(producto)
    return resultados

def factorion():
    factorion = []
    for i in range(1499999):
        resultados = factorial(i)
        suma = 0
        for j in resultados:
            suma += j
        if suma == i:
            factorion.append(i)
    return factorion
        

def prueba():
    tiempo = time()
    resultado = factorion()
    tiempo = round(time() - tiempo, 1)
    print(f" los factoriones menores a 1.499.999 son {resultado}, este programa se tardó {tiempo}s en calcularlo")

if __name__ == "__main__":
    prueba()

