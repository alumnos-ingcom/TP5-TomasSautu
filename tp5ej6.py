################
# Tomás Sautú - @TomasSautu
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def balanceado(texto):
    parentesis_abierto = 0
    parentesis_cerrado = 0
    llave_abierta = 0
    llave_cerrada = 0
    corchete_abierto = 0
    corchete_cerrado = 0
    for i in range(len(texto)):
        if (texto[i] == "("):
            parentesis_abierto += 1
        elif (texto[i] == ")"):
            parentesis_cerrado += 1
        elif (texto[i] == "{"):
            llave_abierta += 1
        elif (texto[i] == "}"):
            llave_cerrada += 1
        elif (texto[i] == "["):
            corchete_abierto += 1
        elif (texto[i] == "]"):
            corchete_cerrado += 1
    if (parentesis_abierto + parentesis_cerrado) == 0:
        parentesis = ("No Tiene")
    else:
        
        if parentesis_abierto == parentesis_cerrado:
            parentesis = ("OK")
        else:
            parentesis = ("NO OK")
        
    if (llave_abierta + llave_cerrada)==0:
        llaves = ("No Tiene")
    else:
        
        if llave_abierta == llave_cerrada:
            llaves = ("OK")
        else:
            llaves = ("NO OK")
    if (corchete_abierto + corchete_cerrado) == 0:
        corchetes = ("No Tiene")
    else:
        
        if corchete_abierto == corchete_cerrado:
            corchetes = ("OK")
        else:
            corchetes = ("NO OK")
    return parentesis,llaves, corchetes

def prueba():
    print("""Este programa analizara un texto y le dira si los paréntesis, llaves o corchetes estan balanceados
(balanceado se refiere a que cada uno tiene su caracter de apertura y de cierre)""")
    texto = input("Ingrese el texto: ")
    parentesis, llaves, corchetes = balanceado(texto)
    print(f"Paréntesis: {parentesis}")
    print(f"Llaves: {llaves}")
    print(f"Corchetes: {corchetes}")

if __name__ == "__main__":
    prueba()

