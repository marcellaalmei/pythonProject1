salary = float(input("Digite o seu salário: "))
if salary > 1250:
    a = (10/100)*salary
    print("O seu aumento será de R$ {}".format(a))
else:
    b = (15/100)*salary
    print("O seu aumento será de R$ {}".format(b))