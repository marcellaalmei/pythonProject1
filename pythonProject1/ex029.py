velocidade = float(input("Digite a velocidade do carro: "))
multa = 7*(velocidade-80)
if velocidade >= 80:
    print("Você provavelmente receberá uma multa!")
    print("A sua multa irá custar aproximadamente R${}".format(multa))