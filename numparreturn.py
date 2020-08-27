def funcion_numpar(numero):
    res = numero % 2 
    if res == 0:
        return True
    
    else:
        return False

def main ():
    numero = int(input("digitar el numero a calcular"))
    result = funcion_numpar(numero)
    if result == True:
       print (f"El número {numero} es un numero par")

    else:
       print(f"El número {numero} es un numero impar")

if __name__ == "__main__":
    main()