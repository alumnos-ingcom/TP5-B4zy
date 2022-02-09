################
# Tomás Gadea - @B4zy
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def codificar_cesar(texto, cifrado):
    texto = list(texto)
    texto_cesar = []
    for i in range(len(texto)):
        numero = ord(texto[i])
        numero_cifrado = numero + cifrado
        letra_cifrada = chr(numero_cifrado)
        texto_cesar.append(letra_cifrada)
    return "".join(texto_cesar)

def decodificar_cesar(texto, cifrado):
    texto = list(texto)
    texto_cesar = []
    for i in range(len(texto)):
        numero = ord(texto[i])
        numero_cifrado = numero - cifrado
        letra_cifrada = chr(numero_cifrado)
        texto_cesar.append(letra_cifrada)
    return "".join(texto_cesar)
        
def prueba():
    from soporte import recuadro
    from soporte import ingreso_entero
    recuadro(" [1] Decodificar  [2] Codificar ")
    while True:
        mensaje_ingreso = "Ingrese un numero: "
        mensaje_error = "Oops, eso no era un numero"
        seleccion = ingreso_entero(mensaje_ingreso, mensaje_error)
        if seleccion == 1 or seleccion == 2:
            break
        else:
            print("Unicamente se admiten los valores [1] o [2]")
            
    if seleccion == 1:
        texto = input("Ingrese un texto a decodificar: ")
        while True:
            mensaje_ingreso = "Ingrese un cifrado: "
            mensaje_error = "El cifrado debe ser un numero"
            cifrado = ingreso_entero(mensaje_ingreso, mensaje_error)
            if cifrado != 0:
                break
            else:
                print("No se admite el 0 como cifrado")
    else:
        texto = input("Ingrese un texto a codificar: ")
        while True:
            mensaje_ingreso = "Ingrese un cifrado: "
            mensaje_error = "El cifrado debe ser un numero"
            cifrado = ingreso_entero(mensaje_ingreso, mensaje_error)
            if cifrado != 0:
                break
            else:
                print("No se admite el 0 como cifrado")
                
    if seleccion == 1:
        mostrar = decodificar_cesar(texto, cifrado)
        print(f"Su texto decodificado con ROT{cifrado} es '{mostrar}'")
    else:
        mostrar = codificar_cesar(texto, cifrado)
        print(f"Su texto codificado con ROT{cifrado} es '{mostrar}'")
            
if __name__ == "__main__":
    prueba()