from random import randint, choices  
from time import sleep
h = "s"
cofre = 50
while (h == "s"):
    if(cofre > 0):

        print("APOSTE E PERCA TUDO")
        
        population = [0,1,2,3,4,5,6,7,8,9,10]
        weights = [40,10,10,5,5,3,3,2,2,2,0.5]
        n = choices(population, weights, k=100)

        #n  = (0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,2,2,2,2,3,3,3,4,4,5,5,6,6,6,7,8,8,9,9,9,9,10,10,10,10,10)
        computador = n[randint(0,len(n)-1)]
        print(computador)
        print("===================COMECE SUA APOSTA=====================")
        resp = input("Deseja checar seu cofre?\ns para sim. \nn para não.\nResposta: ")
        if(resp == "s"):
            print(cofre)
        else:
            print("ok.")
        jogador = int(input("Aposte um número de 0 à 10: "))

        aposta = int(input("Digite o valor da aposta: "))

        sleep(3)

        

        if (jogador <= computador):
            sleep(3)
            for c in range(computador + 1):
                print (c)

            aposta = aposta * jogador
            print("Você recebeu a quantia de {}".format(aposta))
            cofre = cofre + aposta
            h = input("Deseja jogar novamente?\ns para sim. \nn para não.\nResposta: ")
            
        elif (jogador > 10 ):
            print("valor de aposta incorreto")
            h = "n"
        else:
            
            sleep(3)
            for c in range(len(computador)):
                print (c)
            print("{}".format(computador))
            print("perdeu tudo")
            cofre = cofre - aposta
            h = input("Deseja jogar novamente?\ns para sim. \nn para não.\nResposta: ")
    else:
        h = "n"
        print("Seu dinheiro todo acabou, além de burro agora é pobre!")