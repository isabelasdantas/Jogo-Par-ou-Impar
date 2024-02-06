from random import randint
print('***' * 10)
print('VAMOS JOGAR PAR OU ÌMPAR')
print('***' * 10)
vito = 0
while True:
    n = int(input('Digite um valor: '))
    comp = randint(1, 100)
    total = comp + n
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ìmpar: [P/I]? ')).strip().upper()[0]
    print(f'Vocês jogou {n} e o computador {comp}. O total de {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÌMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            vito += 1
        else:
            print('Você perdeu!')
            break
    if tipo == 'I':
        if total % 2 == 0:
            print('Você venceu!!')
            vito += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos Jogar novamente...')
print(f'GAME OVER! Você venceu em {vito} vezes')
