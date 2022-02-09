################
# Tomás Gadea - @B4zy
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def detectar_parentesis(cadena):
    lista = []
    signo = { '{' : '}' , '[' : ']' , '(' : ')' , '¿' : '?' , '¡' : '!' }
    if len(cadena) % 2 != 0:
        return False
    else:
        for llave in cadena:
            if llave in signo:
                lista.append(llave)
            elif len(lista) == 0 or not (llave == signo[lista.pop()]):
                return False
    cantidad_elementos = len(lista)
    if cantidad_elementos != 0:
        return False
    else:
        return True
        
def prueba():
    cadena = input("Ingrese un texto: ")
    mostrar = detectar_parentesis(cadena)
    if mostrar == True:
        print(f"[{mostrar}] Es correcta")
    else:
        print(f"[{mostrar}] Es incorrecta")
        
if __name__ == "__main__":
    prueba()