nome = str(input("Digite seu nome: "))
if nome == "Marcella":
    print("\033[2;33mQue lindo nome!\033[m")
else:
    print("Seu nome é tão normal\033[4;38m")
print("Bom dia,{}!".format(nome))
