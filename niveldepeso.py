peso = float(input("ingrese su peso en kg "))
altura = int(input("ingrese su altura en cm "))
altura = altura / 100
imc = peso / (altura * altura)
if (imc >18.6 and imc <25):
    print("usted tiene sobrepeso")
elif (imc <= 18.4):
    print("usted tiene bajo peso")
elif (imc >= 25 and imc <30):
    print("usted tiene sobrepeso")
else:
    print("usted esta en peligro")