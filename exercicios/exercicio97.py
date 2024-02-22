def escreva(texto):
    taman = len(texto) + 8
    tex = texto.center(taman)
    print('~'*taman)
    print(tex)
    print('~'*taman)


text = 'Gustavo Guanabara'
escreva(text)
curso = 'Curso de Python no Youtube'
escreva(curso)
ce = 'CeV'
escreva(ce)
nome = str(input('Digite alguma coisa: '))
escreva(nome)