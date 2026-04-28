peso = float(input("ingrese su peso en kg "))
altura = int(input("ingrese su altura en cm "))
altura = altura / 100
imc = peso / (altura * altura)
print ("su indice de masa corporal es: ",imc)
