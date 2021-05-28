################
# Tomás Sautú - @TomasSautu
# UNRN Andina - Introducción a la Ingenieria en Computación
################



def invertir_minus_mayus(texto):
    caracteres = []
    for i in range(len(texto)):
        if (texto[i].islower()):
            caracteres.append(texto[i].upper())
        else:
            caracteres.append(texto[i].lower())
    texto = "".join(caracteres)
    return texto
            


def prueba():
    texto = input("Coloque/escriba un texto para invertir sus mayúsculas y minúsculas: ")
    texto_invertido = invertir_minus_mayus(texto)
    print(f"El texto invertido es '{texto_invertido}'")

if __name__ == "__main__":
    prueba()

