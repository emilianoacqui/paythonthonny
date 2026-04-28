n = int(input("ingrese un numero "))
sumatoria = 1
suma = 0
for i in range (1,n):
    suma = suma + sumatoria
    sumatoria = sumatoria +1
    print (sumatoria)
print ("resultado final:" ,sumatoria)
print ("suma final:" ,suma)