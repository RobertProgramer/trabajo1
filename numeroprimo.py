num=int(input("Digite un numero para calcular:  "))

if num > 1: 

    cont = 0 
   
    for i in range(2,num):

        resto = num % i

        # print(f"{num} % {i} = {resto}")

        if resto == 0:
           cont += 1

    if  cont == 0:
   
         print(f"el {num} es un numero primo")
  
    else: 
         print(f"El {num} no es un numero primo")


else: 
     print(f"El {num} no es un numero primo")
