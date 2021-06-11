################
# Tomás Gadea - @B4zy
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def factorion():
    from soporte import factorial
    numero = 0
    factorion = 0
    fact = factorial(9, True)
    lista_factorion = []
    lista_factorial = []
    while factorion < 1499999:
        numero += 1
        lista_numero = list(str(numero))
        for c in range(len(lista_numero)):
            lista_numero[c] = int(lista_numero[c])    
        lista_factorial = lista_numero
        for c in range(len(lista_factorial)):
            if lista_numero[c] == 0 or lista_numero[c] == 1:
                lista_factorial[c] = fact[0]
            elif lista_numero[c] == 2:
                lista_factorial[c] = fact[2]
            elif lista_numero[c] == 3:
                lista_factorial[c] = fact[3]
            elif lista_numero[c] == 4:
                lista_factorial[c] = fact[4]
            elif lista_numero[c] == 5:
                lista_factorial[c] = fact[5]
            elif lista_numero[c] == 6:
                lista_factorial[c] = fact[6]
            elif lista_numero[c] == 7:
                lista_factorial[c] = fact[7]
            elif lista_numero[c] == 8:
                lista_factorial[c] = fact[8]
            else:
                lista_factorial[c] = fact[9]          
            if sum(lista_factorial) ==  numero:
                factorion = sum(lista_factorial)
                lista_factorion.append(factorion)
                print(lista_factorion)
                
def prueba():
    while True:
        mostrar = input("Escriba 'mostrar' para ver la lista: ")
        mostrar = mostrar.lower()
        if mostrar == "mostrar":
            valor = True
            break
        else:
            print("La clave es 'mostrar'.")       
    factorion()

            
if __name__ == "__main__":
    prueba()