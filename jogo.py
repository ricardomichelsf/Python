import random


class Jogo():
    def __init__(self):
        self.restart()

    def restart(self):
        self.alvo = random.randint(0,100)
        self.maior = 100
        self.menor = 0
        self.chutes = [] #AAA

    def chutar(self, chute):
        assert(type(chute) == int)
        #TODO: salvar o chute na lista de chutes
        self.chutes.append(chute) 
        #----------
        # lista 
        # definida no restart (linha AAA)
        #TODO atualizar o intervalo. Eu comecei no intervalo de 0 a 100
        #     se eu chutei 75, e meu chute foi alto,
        #     agora estou entre 0 e 74
        #10.11.12.13,14,15,16,17,18
        #               15     
        #10.11.12.13,14
           
        if chute > self.alvo:
            self.maior = chute-1
        if chute < self.alvo:
            self.menor = chute+1

        if chute == self.alvo:
            self.menor = chute
            self.maior = chute

        #     isso se reflete nas variaveis self.menor = 0 (nao mudou)
        #     e self.maior = 74 (acabei de atualizar)
        #     Note: isso significa que o usuário deve chutar 
        #     o próximo número entre 0 e 74
    
    def resumo(self):
        if self.chutes == []:
            return f"Estamos entre {self.maior} e {self.menor}. Chute um número!"
        
        ultimo_chute = self.chutes[-1]
        if ultimo_chute == self.alvo:
            return "Você fez um chute correto! Você acertou! Parabéns!"

        resumo = ""

        if ultimo_chute < self.alvo:
            resumo += "Seu ultimo chute foi baixo!"
        if ultimo_chute > self.alvo:
            resumo += "Seu ultimo chute foi alto!"
        resumo += f"estamos entre {self.menor} e {self.maior}"
        
        return resumo

