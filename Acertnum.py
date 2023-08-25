import random

numero_aleatorio = random.randint(1, 200)
tentativas = 0

while True:
    chute = int(input("Chute um número entre 1 e 200: "))
    tentativas += 1
    if chute == numero_aleatorio:
        print("Parabéns! Você acertou o número!")
        print("tentativas: ", tentativas)
    elif chute < numero_aleatorio:
        print("Chute um número maior")
    else:
        print("Chute um número menor")
