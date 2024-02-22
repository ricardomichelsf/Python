def notas(*args, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param args: Uma ou mais notas dos alunos (aceita varias).
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    nota = {}
    nota['total'] = len(args)
    nota['maior'] = max(args)
    nota['menor'] = min(args)
    nota['media'] = sum(args) / nota['total']
    if sit:
        if nota['media'] < 5:
            nota['situação'] = 'RUIM'
        elif nota['media'] < 7:
            nota['situação'] = 'RAZOÁVEL'
        else:
            nota['situação'] = 'BOA'

    return nota


print('--'*25)
resp = notas(3.5, 10, 6.5, sit=True)
print(resp)
print()

help(notas)