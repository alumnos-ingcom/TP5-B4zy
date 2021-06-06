################
# Tomás Gadea - @B4zy
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def distancia(primer_numero, segundo_numero):
    if (primer_numero > 0) and (segundo_numero > 0):
        distancia = primer_numero - segundo_numero
        if distancia < 0:
            distancia = distancia * (-1)
        return distancia
    elif (primer_numero < 0) and (segundo_numero > 0):
        primer_numero = primer_numero * (-1)
        return primer_numero + segundo_numero
    elif (primer_numero > 0) and (segundo_numero < 0):
        segundo_numero = segundo_numero * (-1)
        return segundo_numero + primer_numero
    
def prueba():
    while True:
        primer_numero = input("Ingrese un numero: ")
        try:
            primer_numero = float(primer_numero)
            break
        except ValueError:
            print("Oops, eso no era un numero")
    
    while True:
        segundo_numero = input("Ingrese otro numero: ")
        try:
            segundo_numero = float(segundo_numero)
            break
        except ValueError:
            print("Oops, eso no era un numero")
            
    mostrar = distancia(primer_numero, segundo_numero)
    print(f"La distancia entre {primer_numero} y {segundo_numero} es {mostrar}")
        
if __name__ == "__main__":
    prueba()