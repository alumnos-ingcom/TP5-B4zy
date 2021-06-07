################
# Tomás Gadea - @B4zy
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def codificar_cesar(texto, cifrado):
    texto = list(texto)
    texto_cesar = []
    conversion_a_numero = []
    for i in range(len(texto)):
        numero = ord(texto[i])
        numero_cifrado = numero + cifrado
        letra_cifrada = chr(numero_cifrado)
        texto_cesar.append(letra_cifrada)
    return "".join(texto_cesar)


def decodificar_cesar(texto, cifrado):
    texto = list(texto)
    texto_cesar = []
    conversion_a_numero = []
    for i in range(len(texto)):
        numero = ord(texto[i])
        numero_cifrado = numero - cifrado
        letra_cifrada = chr(numero_cifrado)
        texto_cesar.append(letra_cifrada)
    return "".join(texto_cesar)
        
def prueba():
    print('''
===============================================================================================
    [1] Descifrar texto
    [2] Cifrar texto
===============================================================================================''')
    while True:
        seleccion = input("Ingrese que quiere hacer [1] o [2]: ")
        try:
            seleccion = int(seleccion)
            if seleccion == 1 or seleccion == 2:
                break
            else:
                print("Unicamente se admiten los valores [1] o [2]")
        except ValueError:
            print("Oops, eso no era un numero")
            
    if seleccion == 1:
        texto = input("Ingrese un texto a decodificar: ")
        while True:
            cifrado = input("Ingrese el cifrado: ")
            try:
                cifrado = int(cifrado)
                break
            except ValueError:
                print("El cifrado debe ser un numero")
    else:
        texto = input("Ingrese un texto a codificar: ")
        while True:
            cifrado = input("Ingrese el cifrado: ")
            try:
                cifrado = int(cifrado)
                break
            except ValueError:
                print("El cifrado debe ser un numero")

    if seleccion == 1:
        mostrar = decodificar_cesar(texto, cifrado)
        print(f"Su texto decodificado con ROT{cifrado} es {mostrar}")
    else:
        mostrar = codificar_cesar(texto, cifrado)
        print(f"Su texto codificado con ROT{cifrado} es {mostrar}")
            
if __name__ == "__main__":
    prueba()