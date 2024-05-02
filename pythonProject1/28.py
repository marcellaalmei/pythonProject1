import random
nreal = int(input("Digite um número inteiro de 1 a 5 e veja se você pensa como seu computador: "))
n = [1, 2, 3, 4, 5]
sorteio = random.choice(n)
if nreal == sorteio:
    print("UAL, vocês estão conectados, seu computador também pensou {}".format(sorteio))
else:
    print("Você errou, seu computador estava pensando no número {}".format(sorteio))
