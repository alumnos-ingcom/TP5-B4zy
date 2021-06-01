################
# Tomás Gadea - @B4zy
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def es_perfecto(numero):
    lista = []
    for i in range(1, numero):
        if numero % i == 0:
            i = int(i)
            lista.append(i)
    if numero == sum(lista):
        return True
    else:
        return False


def prueba():
    while True:
        numero_ingresado = input("Ingrese un numero: ")
        try:
            numero_ingresado = int(numero_ingresado)
            break
        except ValueError:
            print("Oops, eso no era un numero")
            
    mostrar = es_perfecto(numero_ingresado)
    
    if mostrar == True:
        print(f"El numero [{numero_ingresado}] es perfécto.")
    else:
        print(f"El numero [{numero_ingresado}] no es perfécto")
        
prueba()