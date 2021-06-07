################
# Tomás Sautú - @TomasSautu
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from utilidades import ingreso_entero
import random

def lista_aleatoria(cantidad_numeros):
    lista = []
    for i in range(cantidad_numeros):
        lista.append(random.randint(0, 200))
    return lista

def promedio_movil(listaNum, cantidad_promedio_valores):
    lista_numeros = []
    lista_promedio = [listaNum[0]]
    cantidad_calculos = (len(listaNum) - cantidad_promedio_valores) + 1
    for i in range(cantidad_calculos):
        promedio = 0
        for j in range(cantidad_promedio_valores):
            promedio += listaNum[i+j]
        promedio = promedio / cantidad_promedio_valores
        lista_promedio.append(promedio)
    for i in lista_promedio:
        lista_numeros.append(round(i,2))
    return lista_numeros
        


def prueba():
    print("""Este programa hará un promedio de una lista aleatoria, con la cantidad que usted quiera de números enteros
(tener en cuenta que se necesitan por la misma cantidad de números que la cantidad de valores que quiere promediar)""")
    cantidad_numeros = ingreso_entero("Cuantos números quiere en la lista aleatoria?: ")
    lista_numeros = lista_aleatoria(cantidad_numeros)
    cantidad_valores = ingreso_entero("Que cantidad de valores quiere promediar: ")
    if cantidad_numeros >= cantidad_valores:
        lista_promedios = promedio_movil(lista_numeros, cantidad_valores)
        print(f"El promedio de la lista {lista_numeros} (promediando de a {cantidad_valores} valores) es {lista_promedios}")
    else:
        print(f"Se necesitan por lo menos {cantidad_valores} números para poder promediar de a {cantidad_valores} valores.") 

if __name__ == "__main__":
    prueba()