

def comparar(lista_uno, lista_dos):
    primera_lista = sorted(lista_uno)
    segunda_lista = sorted(lista_dos)
    return primera_lista == segunda_lista



def prueba():
    ingreso = 0
    primer_lista = []
    segunda_lista = []
    while True:
        print("Escriba 'stop' para escribir otra lista")
        if ingreso == "stop":
            break
        else:
            ingreso = input("Ingrese un caracter para la lista: ")
            primer_lista.append(ingreso)
    ingreso = 0        
    while True:
        print("Escriba 'stop' para terminar con las listas")
        if ingreso == "stop":
            break
        else:
            ingreso = input("Ingrese un caracter para la lista: ")
            segunda_lista.append(ingreso)
    
    mostrar = comparar(primer_lista, segunda_lista)
    print(f"La comparacion de {primer_lista} y {segunda_lista} es: {mostrar}")
    
    
    
if __name__ == "__main__":
    prueba()