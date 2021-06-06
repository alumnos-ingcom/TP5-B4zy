################
# Tomás Gadea - @B4zy
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def es_capicua(numero):
    capicua = list(str(numero))
    capicua_reverse = list(reversed(capicua))
    return capicua == capicua_reverse

def prueba():
    while True:
        numero = input("Ingresa un numero: ")
        try:
            numero = int(numero)
            break
        except ValueError:
            print("Oops, eso no era un numero")
            
    mostrar = es_capicua(numero)
    
    if mostrar == True:
        print(f"[{mostrar}] Es capicua")
    else:
        print(f"[{mostrar}] No es capicua")
        
prueba()