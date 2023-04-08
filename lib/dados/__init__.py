from time import sleep


def titulo(msg):
    print('*' * 60)
    print(msg.center(60))
    print('*' * 60)


def linha():
    print('*' * 60)


def menu(lista):    
    titulo('MENU')
    for pos, valor in enumerate (lista):
        print(f'\033[34m{pos + 1:>4}\033[m -- \033[35m{valor:<30}\033[m')
    linha()
    while True:
        try:
            opc = int(input('Opção: '))
            if opc < 1 or opc > len(lista):
                print('\033[31mSelecione uma opção válida!')
                continue
        except(ValueError, TypeError, KeyboardInterrupt):
            print('\033[31mSelecione uma opção válida!')
        else:
            sleep(1)
            return opc


def leiaCpf(lista):
    while True:
        try:
            valores = []
            cpf = input('CPF: ')
            if cpf.isnumeric() == False or len(cpf) != 11:
                print('\033[31mCPF Inválido. Digite novamente.\033[m')
                continue
        except (ValueError, TypeError):
            print('\033[31mCPF Inválido. Digite novamente.\033[m')
            continue
        except (KeyboardInterrupt):
            break
        for valor in cpf:
            valores.append(valor)
        valores.insert(3, '.')
        valores.insert(7, '.')
        valores.insert(11, '-')
        cpf = ''.join(valores)
        if cpf in lista:
            print('\033[31mCPF existente.\033[m')
            continue
        lista.append(cpf)
        sleep(1)
        break
