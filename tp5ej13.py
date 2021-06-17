################
# Tomás Gadea - @B4zy
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def buscar(texto, palabra):
    return texto.find(palabra)



def prueba():
    texto = input("Ingresa un texto: ")
    palabra = input("Ingresa una palabra a buscar: ")
    mostrar = buscar(texto, palabra)
    print(f"La palabra '{palabra}' se encuentra en la posicion: {mostrar}")
    
if __name__ == "__main__":
    prueba()