################
# Tomás Gadea - @B4zy
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def tribonacci(numero):
    primer_termino = 1
    segundo_termino = 1
    tercer_termino = 1
    cuarto_termino = 0
    i = 3
    while i < numero:
        cuarto_termino = primer_termino + segundo_termino + tercer_termino
        primer_termino = segundo_termino
        segundo_termino = tercer_termino
        tercer_termino = cuarto_termino
        i = i + 1
    return tercer_termino

def prueba():
    while True:
        numero_ingresado = input("Ingrese un numero: ")
        try:
            numero_ingresado = int(numero_ingresado)
            break
        except ValueError:
            print("Oops, eso no era un numero")
    
    mostrar = tribonacci(numero_ingresado)
    print(f"El término [{numero_ingresado}] en la sucesion de tribonacci es [{mostrar}]")
    
prueba()