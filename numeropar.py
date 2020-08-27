def numpar():
    numpar = int(input("digitar el numero a calcular"))
    if numpar % 2 == 0:
        print(f"El número {numpar} es un numero par")

    else:
        print(f"El número {numpar} es un numero impar")

def main():
    numpar()

if __name__ == "__main__":
    main()