distancia = float(input("Digite a distância da viagem em km (apenas números): "))
if distancia<=200:
    a = (distancia*0.50)
    print("O valor da viagem será: {} reais".format(a))
else:
    b = (distancia*0.45)
    print("O valor da viagem será: {} reais".format(b))
