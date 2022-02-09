################
# Tomás Gadea - @B4zy
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def es_par(numero):
    comprobacion = numero / 2
    return comprobacion - int(comprobacion) == 0
        
        
def prueba():
    while True:
        numero_ingresado = input("Ingrese un numero: ")
        try:
            numero_ingresado = int(numero_ingresado)
            break
        except ValueError:
            print("Oops, eso no era un numero")
            
    comprobar = es_par(numero_ingresado)
    
    if comprobar == True:
        print(f"[{numero_ingresado}] Es par.")
    else:
        print(f"[{numero_ingresado}] No es par.")

prueba()