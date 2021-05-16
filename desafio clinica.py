class Pessoa:
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone


class Medico(Pessoa):
    def __init__(self, nome, cpf, telefone, crm):
        super().__init__(nome, cpf, telefone)
        self.crm = crm
        self.__salario = 0
        self.especialidade = []

    def get_salario(self):
        return self.__salario

    def set_salario(self, valor):
        self.__salario = valor
        
    def especialistas(self, especialista):
        self.especialidade = especialista


class Paciente(Pessoa):
    def __init__(self, nome, cpf, telefone, rg, endereco, dataDeNascoimeto):
        super().__init__(nome, cpf, telefone)
        self.rg = rg
        self.endereco = endereco
        self.dataDeNascimento = dataDeNascoimeto


class Clinica:
    def __init__(self, quarto, andar):
        self.quarto = quarto
        self.andar = andar


class Internacao(Clinica, Medico, Paciente):
    def __init__(self, quarto, andar, observacao, nome, especialidade):
        super().__init__(quarto, andar)
        self.observacao = observacao

    def nome_Paciente(self, Paciente):
        self.nome = Paciente.nome

    def nome_Medico(self, Medico):
        self.nome = Medico.nome
        self.especialidade = Medico.especialidade


class Relatorio(Internacao):
    def __init__(self, quarto, andar, observacao, data, horario, nome, especialidade):
        super().__init__(quarto, andar, observacao, nome, especialidade)
        self.data = data
        self.horario = horario
    def exibir_dados(self, nome_Paciente, nome_Medico):
        print(f'O paciente {nome_Paciente()} está internado no quarto {self.quarto}, no {self.andar} andar')
        print(f'O médico responsavél {nome_Medico()}')
        print(f'Foi visitado no dia {self.data} as {self.horario} horas')

        



