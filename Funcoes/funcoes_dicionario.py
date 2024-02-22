def inicio():
    while True:
        opcao = input("""O que deseja realizar?
        <I> - Para Inserir um usuário 
        <P> - Para Pesquisar um usuário
        <E> - Para Excluir um usuário
        <L> - Para Listar um usuário: 
        <S> - Sair do Programa: """).upper()
        if opcao in 'IPELS':
            return opcao
        print('DIgite um valor válido!!')
        

def inserir(dicionario):
    chave = input('Digite o login: ').upper()
    dicionario[chave] = [input('Digite o nome: ').upper(),
        input("Digite a última data de acesso: "),
        input("Qual a última estação acessada: ").upper()]
    

def pesquisar(dicionario, chave):
    try:
        lista = dicionario.get(chave)
        print(f'Nome............:  {lista[0]}')
        print(f'Data de acesso..:  {lista[1]}')
        print(f'Estação acessada:  {lista[2]}')
    except KeyError:
        print('\nUsuário não encontrado!\n')


def listar(dicionario):
    for key, valor  in dicionario.items():
        print('Objeto.......')
        print(f'Login: {key}: ')
        print(f'Dados: {valor}')


def excluir(dicionario,chave):
    confirmacao = str(input(f'Deseja realmente excluir {chave}? ')).upper()
    if confirmacao == 'SIM':
        del dicionario[chave]
    else:
        print('Exclusão cancelada!')


