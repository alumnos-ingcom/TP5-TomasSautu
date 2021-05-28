################
# Tomás Sautú - @TomasSautu
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def parentesis_balanceado(texto):
    parentesis_abierto = 0
    parentesis_cerrado = 0
    for i in range(len(texto)):
        if (ord(texto[i]) == 40):
            parentesis_abierto += 1
        elif (ord(texto[i]) == 41):
            parentesis_cerrado += 1
    if (parentesis_abierto + parentesis_cerrado) == 0:
        return "No Tiene"
    else:
        
        if parentesis_abierto == parentesis_cerrado:
            return "OK"
        else:
            return "NO OK"

def llaves_balanceadas(texto):
    llave_abierta = 0
    llave_cerrada = 0
    for i in range(len(texto)):
        if (ord(texto[i]) == 123):
            llave_abierta += 1
        elif (ord(texto[i]) == 125):
            llave_cerrada += 1
    if (llave_abierta + llave_cerrada)==0:
        return "No Tiene"
    else:
        
        if llave_abierta == llave_cerrada:
            return "OK"
        else:
            return "NO OK"

def corchetes_balanceados(texto):
    corchete_abierto = 0
    corchete_cerrado = 0
    for i in range(len(texto)):
        if (ord(texto[i]) == 91):
            corchete_abierto += 1
        elif (ord(texto[i]) == 93):
            corchete_cerrado += 1
    if (corchete_abierto + corchete_cerrado) == 0:
        return "No Tiene"
    else:
        
        if corchete_abierto == corchete_cerrado:
            return "OK"
        else:
            return "NO OK"


def prueba():
    print("""Este programa analizara un texto y le dira si los paréntesis, llaves o corchetes estan balanceados
(balanceado se refiere a que cada uno tiene su caracter de apertura y de cierre)""")
    texto = input("Ingrese el texto: ")
    respuesta_parentesis = parentesis_balanceado(texto)
    respuesta_llaves = llaves_balanceadas(texto)
    respuesta_corchetes = corchetes_balanceados(texto)
    print(f"Paréntesis: {respuesta_parentesis}")
    print(f"Llaves: {respuesta_llaves}")
    print(f"Corchetes: {respuesta_corchetes}")

if __name__ == "__main__":
    prueba()

