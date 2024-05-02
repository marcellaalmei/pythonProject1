n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite outro número: "))
#Verificando quem é maior
if n1 > (n2 and n3):
    print("O maior número é: {}".format(n1))
if n2 > (n1 and n3):
    print("O maior número é: {}".format(n2))
if n3 > (n1 and n2):
    print("O maior número é: {}".format(n3))
#Verificando quem é menor
if n1 < (n3 and n2):
    print("O menor número é: {}".format(n1))
if n2 < (n3 and n1):
    print("O menor número é: {}".format(n2))
if n3 < (n1 and n2):
    print("O menor número é: {}".format(n3))
#Outra forma de fazer é definindo que a é maior e ir testando com if


