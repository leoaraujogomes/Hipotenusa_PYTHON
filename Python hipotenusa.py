import math

y = float(input("Insira a altura do prédio: "))
x = float(input("Insira a distância referente ao prédio: "))
h = math.sqrt(math.pow(x,2) + math.pow(y,2))
a = math.atan(y/x)

print ("O tamanho da corda é: ", h)
print ("O ângulo equivale a: ", math.degrees(a))
