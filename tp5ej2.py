################
# Tomás Gadea - @B4zy
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def fibonacci(numero):
    primer_termino = 0
    segundo_termino = 1
    tercer_termino = 0
    i = 1
    while i < numero:
        tercer_termino = primer_termino + segundo_termino
        primer_termino = segundo_termino
        segundo_termino = tercer_termino
        i = i + 1
    return segundo_termino

def prueba():
    
    while True:
        numero_ingresado = input("Ingresa un numero: ")
        try:
            numero_ingresado = int(numero_ingresado)
            break
        except ValueError:
            print("Oops, eso no era un numero")
    
    mostrar = fibonacci(numero_ingresado)
    print(f"El término {numero_ingresado} en la sucesion de fibonacci es el numero {mostrar}")
    
prueba()