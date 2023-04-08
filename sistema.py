from lib.dados import *

opcoes = ['Novo Cadastro', 'Consultar Cadastrados', 'Sair']
dados = []
while True:
    opcao = menu(opcoes)
    if opcao == 1:
        # validando cpf
        leiaCpf(dados)
    elif opcao == 2:
        for pos, valor in enumerate(dados):
            print(f'\033[32m{pos + 1:>3} -- {valor:<15}\033[m')
    else:
        titulo('\033[31mAté logo!\033[m')
        break
