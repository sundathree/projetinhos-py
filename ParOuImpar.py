from random import randint
from time import sleep
import os

def limpar():
    sleep(2)
    os.system('cls')
vitorias = 0
jogando = True

while jogando:
    try:
        num = int(input('Digite um valor: '))

        while (escolha := input('Par ou ímpar? [P/I] ').strip().upper()) not in ('P', 'I'):
            print(f'\033[1;31mEscolha inválida.\033[m')

        cpu = randint(1, 20)
        total = num + cpu
        par = total % 2 == 0

        resultado = (
            f'Você jogou {num} e o computador jogou {cpu}... O total de {total} é PAR...'
            if par else
            f'Você jogou {num} e o computador jogou {cpu}... O total de {total} é ÍMPAR...'
        )

        print(resultado)
        sleep(1)

        if (escolha == 'P' and par) or (escolha == 'I' and not par):
            vitorias += 1
            print('\033[1;32mVocê venceu!\033[m')
            print('Vamos jogar novamente...')
            limpar()
        else:
            print('\033[1;31mVocê perdeu...\033[m')
            sleep(2)
            break

    except ValueError:
        print('\033[1;31mEntrada inválida.\033[m')
print(f'\033[1;31mFIM DE JOGO! \033[mVocê venceu {vitorias} vezes.')
while (escolha := input('Quer jogar novamente? [S/N] ').strip().upper()) not in ('S', 'N'):
    print(f'\033[1;31mEscolha inválida.\033[m')
if escolha == 'S':
    rodando = True
else:
    input('Pressione ENTER para sair.')
