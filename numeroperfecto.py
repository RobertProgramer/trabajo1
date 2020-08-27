ent=int(input("Digite un numero para calcular"))
for i in range(2, ent+1):
    b=0
    for j in range(1, (i//2)+1):
        if((i%j)==0):
            b= b+j;
    if(b==i):
        print("%s el numero es perfecto" %i)
    else:
        print("%s el numero no es perfecto" %i)