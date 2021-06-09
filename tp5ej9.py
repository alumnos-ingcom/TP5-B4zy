################
# Tomás Gadea - @B4zy
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def factorion():
    from soporte import factorial
    numero = 0
    factorion = 0
    factorial = factorial(9, True)
    lista_factorion = []
    lista_factorial = []
    while factorion < 1499999:
        numero += 1
        lista_numero = list(str(numero))
        for c in range(len(lista_numero)):
            lista_numero[c] = int(lista_numero[c])
            indice_factorial = factorial[lista_numero[c]]
            
        if len(lista_factorial) < len(lista_numero):
            print("Entró")
            lista_factorial.append(indice_factorial)
        print(lista_numero, lista_factorial)
         
        
            
            
        
        
        
    
    
        
        
        
        
    
        
            


def prueba():
    while True:
        mostrar = input("Escriba 'mostrar' para ver la lista: ")
        mostrar = mostrar.lower()
        if mostrar == "mostrar":
            break
        else:
            print("La clave es 'mostrar'.")
            
    lista = factorion()

            
if __name__ == "__main__":
    prueba()