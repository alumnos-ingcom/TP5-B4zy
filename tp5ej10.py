################
# Tomás Gadea - @B4zy
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def conversor_decimal(numero):
    suma = 0
    potencia = 0
    while numero >= 1:
        resto = numero % 10
        numero = numero / 10
        numero = int(numero)
        suma = suma + resto * (2**potencia)
        potencia += 1
    return suma

def conversor_binario(numero):
    lista_binario = []
    while numero >= 1:
        resto = numero % 2
        lista_binario.append(resto)
        numero = numero / 2
        numero = int(numero)
    binario = lista_binario[::-1]
    mostrar = "".join(map(str, binario))
    return mostrar
 
def prueba():
    from soporte import ingreso_entero
    from soporte import recuadro
    seleccion = 0
    while seleccion != 1 and seleccion != 2:
        recuadro("[1] Binario -> Decimal [2] Decimal -> Binario")
        seleccion = ingreso_entero("Ingrese la opcion deseada: ", "Oops, eso no era un numero")
        if seleccion != 1 and seleccion != 2:
            print("Unicos valores admitidos [1] o [2]")
    numero_ingresado = ingreso_entero("Ingrese un numero para convertir: ", "Oops, eso no era un numero")
    if seleccion == 1:
        mostrar = conversor_decimal(numero_ingresado)
    else:
        mostrar = conversor_binario(numero_ingresado)
    print(f"El numero {numero_ingresado} convertido es : {mostrar}")
    
if __name__ == "__main__":
    prueba()