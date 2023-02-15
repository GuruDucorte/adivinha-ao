import random

print ("********************************")
print ("Bem vindo ao jodo de adivinhção!")
print ("********************************")

numero_secreto = random.randrange(1,1000)
total_de_tentativas = 0
pontos = 1000
pontos_perdidos = 0
rodada = 0

print("Qual nivel de dificudade?")
print("(1) Fácil (2) Médio (3) Difícil")
nivel = int(input("Defina o nivel:"))

if(nivel == 1):
    total_de_tentativas = 30
    pontos_perdidos = 25
elif(nivel == 2):
    total_de_tentativas = 20
    pontos_perdidos = 50 
else:
    total_de_tentativas = 10
    pontos_perdidos = 100

    for rodada in range(total_de_tentativas):
        print("\nTentativa ", rodada, "de ", total_de_tentativas)

        chute = int(input("Digite um numero entre 1 e 1000: "))
        print("\nVocê digitou ", chute)

        if(chute < 1 or chute > 1000):
            print("Você deve digitar um numero entre 1 e 1000!")
            continue

        acertou = bool (chute == numero_secreto)
        maior = bool(chute > numero_secreto)
        menor = bool(chute< numero_secreto)

        if(acertou ==  True):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            pontos = pontos - pontos_perdidos

            if(maior):
                print("Você errou ! o seu chute foi o maior do que o numero secreto.")
                print("Maximo{}".format(chute))
                
            elif(menor):
                print("Você errou ! o seu chute foi menor do que o numero secreto.")
                print("Minimo {}".format(chute))

                rodada = rodada + 1

    if(rodada == total_de_tentativas):
        print("O numero secreto era: {}".format(numero_secreto))
print("fim do jogo")
input()
        