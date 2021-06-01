################
# Tomás Gadea - @B4zy
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def invertir_mayusculas(texto):
    return texto.swapcase()


def prueba():
    while True:
        texto_ingresado = input("Ingrese un texto: ")
        if any(map(str.isalpha, texto_ingresado)) == True:
            break
        else:
            print("Debe contener al menos una letra...")

    mostrar = invertir_mayusculas(texto_ingresado)
    print(f"Mayusculas invertidas [{mostrar}]")
    
prueba()