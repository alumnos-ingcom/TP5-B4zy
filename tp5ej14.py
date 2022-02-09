################
# Tomás Gadea - @B4zy
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def es_capicua(numero):
    capicua = list(str(numero))
    for i in range(len(capicua)):
        capicua[i] = int(capicua[i])
    print(capicua)
    capicua_reverse = list(reversed(capicua))
    return capicua == capicua_reverse

def prueba():
    from soporte import ingreso_entero
    mensaje_ingreso = "Ingresa un numero: "
    mensaje_error = "Oops, eso no era un numero"
    numero = ingreso_entero(mensaje_ingreso, mensaje_error)
    mostrar = es_capicua(numero)
    
    if mostrar == True:
        print(f"[{mostrar}] Es capicua")
    else:
        print(f"[{mostrar}] No es capicua")
        
prueba()