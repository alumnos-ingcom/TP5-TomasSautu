################
# Tomás Sautú - @TomasSautu
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from utilidades import ingreso_entero, IngresoIncorrecto

def codificar_cifrado_cesar(rotacion, texto):
    texto_encriptado_lista = []
    for i in texto:
        dato_texto = ord(i)
        if dato_texto >= 65 and dato_texto <= 90:
            dato_texto_mayuscula = dato_texto + rotacion
            if dato_texto_mayuscula > 90:
                while dato_texto_mayuscula > 90:
                    dato_texto_mayuscula -= 26
                dato_texto = chr(dato_texto_mayuscula)
            elif dato_texto_mayuscula < 65:
                while dato_texto_mayuscula < 65:
                    dato_texto_mayuscula += 26
                dato_texto = chr(dato_texto_mayuscula)
            else:
                dato_texto = chr(dato_texto_mayuscula)
        elif dato_texto >= 97 and dato_texto <= 122:
            dato_texto_minuscula = dato_texto + rotacion
            if dato_texto_minuscula > 122:
                while dato_texto_minuscula > 122:
                    dato_texto_minuscula -= 26
                dato_texto = chr(dato_texto_minuscula)
            elif dato_texto_minuscula < 97:
                while dato_texto_minuscula < 97:
                    dato_texto_minuscula += 26
                dato_texto = chr(dato_texto_minuscula)
            else:
                dato_texto = chr(dato_texto_minuscula)
        elif dato_texto >= 48 and dato_texto <= 57:
            dato_texto_numero = dato_texto + rotacion
            if dato_texto_numero > 57:
                while dato_texto_numero > 57:
                    dato_texto_numero -= 10
                dato_texto = chr(dato_texto_numero)
            elif dato_texto_numero < 48:
                while dato_texto_numero < 48:
                    dato_texto_numero += 10
                dato_texto = chr(dato_texto_numero)
            else:
                dato_texto = chr(dato_texto_numero)
        else:
            dato_texto = chr(dato_texto)
        texto_encriptado_lista.append(dato_texto)
    texto_encriptado = "".join(texto_encriptado_lista)
    return texto_encriptado

def decodificar_cifrado_cesar(rotacion, texto):
    texto_encriptado_lista = []
    for i in texto:
        dato_texto = ord(i)
        if dato_texto >= 65 and dato_texto <= 90:
            dato_texto_mayuscula = dato_texto - rotacion
            if dato_texto_mayuscula > 90:
                while dato_texto_mayuscula > 90:
                    dato_texto_mayuscula -= 26
                dato_texto = chr(dato_texto_mayuscula)
            elif dato_texto_mayuscula < 65:
                while dato_texto_mayuscula < 65:
                    dato_texto_mayuscula += 26
                dato_texto = chr(dato_texto_mayuscula)
            else:
                dato_texto = chr(dato_texto_mayuscula)
        elif dato_texto >= 97 and dato_texto <= 122:
            dato_texto_minuscula = dato_texto - rotacion
            if dato_texto_minuscula > 122:
                while dato_texto_minuscula > 122:
                    dato_texto_minuscula -= 26
                dato_texto = chr(dato_texto_minuscula)
            elif dato_texto_minuscula < 97:
                while dato_texto_minuscula < 97:
                    dato_texto_minuscula += 26
                dato_texto = chr(dato_texto_minuscula)
            else:
                dato_texto = chr(dato_texto_minuscula)
        elif dato_texto >= 48 and dato_texto <= 57:
            dato_texto_numero = dato_texto - rotacion
            if dato_texto_numero > 57:
                while dato_texto_numero > 57:
                    dato_texto_numero -= 10
                dato_texto = chr(dato_texto_numero)
            elif dato_texto_numero < 48:
                while dato_texto_numero < 48:
                    dato_texto_numero += 10
                dato_texto = chr(dato_texto_numero)
            else:
                dato_texto = chr(dato_texto_numero)
        else:
            dato_texto = chr(dato_texto)
        texto_encriptado_lista.append(dato_texto)
    texto_encriptado = "".join(texto_encriptado_lista)
    return texto_encriptado

def prueba():
    utilidad = True
    utilidad = ingreso_entero("""Este programa le permitirá hacer una encriptación o desencriptacion cesar con la rotación y mensaje que usted ingrese
Usted quiere Encriptar o Desencriptar?
Encriptar = 1
Desencriptar = 2
""")
    if utilidad == 1:
        utilidad = True
    elif utilidad == 2:
        utilidad = False
    else:
        raise IngresoIncorrecto("No era una opcion")
        
    if utilidad:
        print("""Este programa hará una ENCRIPTACIÓN con Cifrado Cesar con la rotación y mensaje que usted ingrese
    (¡tener en cuentan que las tildes darán un error de encriptación!)""")
        rotacion = ingreso_entero("Ingrese la rotación con la que quiere encriptar: ")
        texto = input("Ingrese el texto que quiere encriptar: ")
        encriptado = codificar_cifrado_cesar(rotacion, texto)
        print(f'El texto encripatado con una rotación de {rotacion} es: "{encriptado}"')
    else:
        print("""Este programa hará una DESENCRIPTACIÓN con Cifrado Cesar con la rotación y mensaje que usted ingrese
    (¡tener en cuenta que las tildes darán un error de encriptación!)""")
        rotacion = ingreso_entero("Ingrese la rotación con la que quiere encriptar: ")
        texto = input("Ingrese el texto que quiere encriptar: ")
        encriptado = decodificar_cifrado_cesar(rotacion, texto)
        print(f'El texto encripatado con una rotación de {rotacion} es: "{encriptado}"')

if __name__ == "__main__":
    prueba()

