import random

ganhou = ('Você ganhou')
perdeu = ('Perdeu')
continua = ('Continua')

def dado():
    print('***'*30)
    dado1 = random.randrange(1, 7)
    dado2 = random.randrange(1, 7)
    print('Primeiro dado: ', dado1)
    print('Segundo dado: ', dado2)
    ponto = dado2 + dado1
    print('Sua pontuação: ', ponto)
    print('***'*30)
    return ponto

while True:
    jogar = input('Deseja jogar ? (s ou n)')
    if jogar == 'n' or jogar == 'N':
        break
    else:
        print('***'*30)
        resultado = dado()
        print('***'*30)

        if resultado == 7 or resultado == 11:
            print (ganhou)
            break
            
        elif resultado == 2 or resultado == 3 or resultado ==12:
            print(perdeu)
            break
        
        else:
            print(continua)
            resultado2 = ''
            while resultado2 != resultado:
                resultado2 = dado()
                if resultado == resultado2:
                    print(ganhou)
                    print('***'*30)
                    break
                    
                elif resultado2 == 7:
                    print(perdeu)
                    print('***'*30)
                    break
                # else:
                #     print(continua)

        
        
        
# Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.