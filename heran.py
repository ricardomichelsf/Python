class Pessoa:
    def __init__(self, nome, endereco, fone, cpf):
        self.nome = nome
        self.endereco = endereco
        self.fone = fone
        self.cpf = cpf


class Aluno(Pessoa):
    def __init__(self, nome, endereco, fone, cpf):
        super().__init__(nome, endereco, fone, cpf)
        self.disciplina = []

    def incluir_disciplina(self, Disciplina):
        self.disciplina.append(Disciplina)


class Funcionario(Pessoa):
    def __init__(self, nome, endereco, fone, cpf, salario):
        super().__init__(nome, endereco, fone, cpf)
        self.salario = salario


class Disciplina:
    def __init__(self, nome):
        self.nome = nome


class Tecnico(Pessoa, Funcionario):
    def __init__(self, nome, endereco, fone, cpf, salario, cargo):
        Pessoa.__init__(self, nome, endereco, fone, cpf)
        Funcionario.__init__(self, salario)
        self.cargo = cargo


class Professor(Pessoa, Funcionario):
    def __init__(self, salario, nome, endereco, fone, cpf, titulacao):
        Pessoa.__init__(self, nome, endereco, fone, cpf)
        Funcionario.__init__(self, salario)
        self.titulacao = titulacao
        self.disciplina = []

    def incluir_disciplina(self, Disciplina):
        self.displina.append(Disciplina)


disciplina1 = Disciplina("Programação")
disciplina2 = Disciplina("Banco de Dados")
professor1 = Professor("Joao", "Rua Silva, 456", "(11)99999-9555", "9999999",
                       2000, "Mestrado")
aluno1 = Aluno("Maria", "Avenida São Francisco, 239",
               "(11)98888-8435", "555555")
tecnico1 = Tecnico("Pedro", "Rua Rocha, 77",
                   "(11)93333-3333", "8787887", 1500, "Tecnico")

aluno1.incluir_disciplina(disciplina1)
aluno1.incluir_disciplina(disciplina2)
professor1.incluir_disciplina(disciplina1)

print('Disciplinas associadas ao aluno:')
for d in aluno1.disciplina:
    print(d.nome)

print('Disciplinas associadas ao Professor:')
for d in professor1.disciplina:
    print(d.nome)