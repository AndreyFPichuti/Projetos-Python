from random import randint
import time

escolha = 'S'


while escolha.upper() == 'S':
    tempo_inicial = time.perf_counter()
    print('Bem-vindo ao Jogo da Advinhação!')
    print('Estou pensando em um número entre 1 e 100.')
    print('Você terá algumas chances baseadas na dificuldade que escolher.\n\n')

    print('Por favor, selecione a dificuldade!')
    print('1. Fácil (10 chances)')
    print('2. Médio (5 chances)')
    print('3. Difícil (3 chances)')

    numero = randint(1, 100)
    i = 0
    opcao = int(input('Digite sua escolha: '))

    if opcao == 1:
        chances = 10
    if opcao == 2:
        chances = 5
    if opcao == 3:
        chances = 3

    print('Ótimo! Você escolheu o nível fácil!')
    print('Vamos começar o jogo!')

    while chances > 0:
        chances -= 1
        i += 1
        tentativa = int(input('Digite sua tentativa: '))

        if tentativa < numero:
            print(f'Errado! O número é maior que {tentativa}')

        elif tentativa > numero: 
            print(f'Errado! O número é menor que {tentativa}')

        else:    
            print(f'Parabéns! Você acertou o número em {i} tentativas!')
            tempo_final = time.perf_counter()
            tempo_jogo = tempo_final - tempo_inicial
            print(f'Você demorou {tempo_jogo:.2f} segundos para advinhar o número!')
            break

    escolha = input('Você quer continuar? (S / N) ')
    if escolha.upper() == 'N':
        break


            