import random

def bem_Vindo(nome):
    print('--' * 20)
    print(f'     Bem vindo {nome}      ')
    print('--' * 20)


def escolhaTema():
    while True:
        print('Escolha o tema para jogar: [1] - Fruta / [2] - Animal / [3] - Cor')
        escolha = int(input())

        if escolha == 1 or escolha == 2 or escolha == 3:
            break
        else:
            print('Escolha um tema valido')

    return escolha

def forca(tema):
    if tema == 1:
        palavra = random.choice(['Banana', 'Manga', 'Uva', 'Laranja', 'Limao']).upper()
        print(palavra)
        tema = "FRUTA"
    elif tema == 2:
        palavra = random.choice(['Cachorro', 'gato', 'Cavalo', 'Abelha', 'Gaviao']).upper()
        tema = "ANIMAL"
    elif tema == 3:
        palavra = random.choice(['Amarelo', 'Roxo', 'Vermelho', 'Laranja', 'Cinza']).upper()
        tema = "COR"


    escondida = '_' * len(palavra)
    letra_adi = []

    max_chutes = 6

    while True:
        
        print(escondida)


        chute = input('Digite a letra do seu chute: ').upper()

        if chute in letra_adi:
            print('Ja digitou essa letra')
            continue

        letra_adi.append(chute)

        if chute in palavra:
            lista = []
            for i in range(len(palavra)):
                if chute == palavra[i]:
                    lista.append(chute)
                else:
                    lista.append(escondida[i])
            
            escondida = "".join(lista)

        else:
            max_chutes -= 1

            print(f'Letra não está na palavra, restam {max_chutes} tentativas')

        if escondida == palavra:
            print('Voce ganhou')
            break
        elif max_chutes == 0:
            print(f'Voce perdeu a palavra era {palavra}')
            break