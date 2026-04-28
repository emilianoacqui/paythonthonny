n= int(input("ingrese un numero "))
d = 0
for i in range (1, n):
    if (n % i == 0):
        d = d+i
if (d == n):
    print ("tu numero es perfecto ")
else:
    print ("tu numero no es perfecto ")