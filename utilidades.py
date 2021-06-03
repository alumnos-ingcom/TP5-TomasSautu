def ingreso_entero(mensaje):
    """
    Esta funcion muestra un mensaje para indicar el ingreso
    de un número entero.
    """
    ingreso = input(mensaje)
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("No era un número genio!") from err
    return entero

def ingreso_real(mensaje):
    """
    Esta funcion muestra un mensaje para indicar el ingreso
    de un número real.
    """
    ingreso = input(mensaje)
    try:
        real = float(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("No era un número genio!") from err
    return real

def ingreso_entero_reintento(mensaje, cantidad_reintentos= 5):
    """Esta función sirva para ingresar un número entero, si lo ingresasado
    da error, se le da otro intento hasta un máximo de 5 veces.
    """
    intentos = cantidad_reintentos
    while intentos >= 0:
        try: 
            return ingreso_entero(mensaje)        
        except:
            print(f"Te quedan {intentos} champion")
            intentos = intentos - 1
    raise IngresoIncorrecto("No era un número titan!")

def ingreso_entero_restringido(mensaje, valor_minimo=0, valor_maximo=50):
    """Esta función pide el ingreso de un número entero pero restringido
    entre el número 0 y el 50.
    """
    entero = ingreso_entero(mensaje)
    if (entero >= valor_minimo and entero <= valor_maximo):
        return entero
    else:
        raise IngresoIncorrecto(f"{entero} no era un número entre 0 y 50 fiera")
    
class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass

def es_primo(numero):
    """Esta función sirve para saber si un
    número es primo, si lo es retorna True,
    caso contrario, retorna False.
    """
    for i in range(2,numero):
        if numero % i == 0 :
            return False
        else:
            return True
        
def factores_primos(numero):
    """Función que descompone un número entero
    en sus factore primos.
    """
    factores = []
    
    if numero > 0 :
        for i in range(2,numero+1):
            while numero % i == 0:
                factores.append(i)
                numero = numero / i
        return factores
    else:
        return False

import random

def lista_aleatoria(cantidad_numeros):
    lista = []
    for i in range(cantidad_numeros):
        lista.append(random.randint(0, 200))
    return lista