n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n = n1+n2/2
print("A sua média foi {}".format(n))
if n>=6.0:
    print("Você está aprovado")
else:
    print("Você não alcançou a média esperada")

