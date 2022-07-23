from itertools import filterfalse
import pandas as pd


class Entrevistador():

    def __init__(self, nome, idade, sexo, resposta1, resposta2, resposta3, resposta4, resposta5, data_hora_cadastro):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.resposta1 = resposta1
        self.resposta2 = resposta2
        self.resposta3 = resposta3
        self.resposta4 = resposta4
        self.resposta5 = resposta5
        self.data_hora_cadastro = data_hora_cadastro

    def dadosBasicos(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        # return self.dadosBasicos

    def pergunta1(self, resposta1):
        if resposta1 == 1:
            self.resposta1 = "Sim"
            return self.resposta1
        elif resposta1 == 2:
            self.resposta1 = "Não"
            return self.resposta1
        elif resposta1 == 3:
            self.resposta1 = "Não sei responder"
            return self.resposta1

    def pergunta2(self):
        return  # resposta 2: Sim, Não, Não Sei

    def pergunta3(self, resposta3):
        if resposta3 == 1:
            self.resposta3 = "Sim"
            return self.resposta3
        elif resposta3 == 2:
            self.resposta3 = "Não"
            return self.resposta3
        elif resposta3 == 3:
            self.resposta3 = "Não sei responder"
            return self.resposta3

    def pergunta4(self):
        return  # resposta 4: Sim, Não, Não Sei

    # recebe um valor entre 1 e 3 e devolve "Sim", "Não" ou "Não Sei".
    def pergunta5(self, resposta5):
        if resposta5 == 1:
            self.resposta5 = "Sim"
            return self.resposta5
        elif resposta5 == 2:
            self.resposta5 = "Não Sei"
            return self.resposta5
        elif resposta5 == 3:
            self.resposta5 = "Não"
            return self.resposta5

    def reunirRespostas(self, nome, idade, sexo, resposta1, resposta2, resposta3, resposta4, resposta5):
        resposta = {nome: [idade, sexo, resposta1,
                           resposta2, resposta3, resposta4, resposta5]}
        return resposta

    def get_nome(self):
        return self.nome

    # Data e hora:
    def horaeData(self, data_hora_cadastro):
        self.data_hora_cadastro = data_hora_cadastro
        return data_hora_cadastro


    def reunirRespostas(self, nome, idade, sexo, resposta1, resposta2, resposta3, resposta4, resposta5, data_hora_cadastro):
        resposta = {'Nome': nome,
                    'Idade': idade,
                    'Gênero': sexo,
                    'Resposta 1': resposta1,
                    'Resposta 2': resposta2,
                    'Resposta 3': resposta3,
                    'Resposta 4': resposta4,
                    'Resposta 5': resposta5,
                    'Data e hora': data_hora_cadastro}
        return resposta


    def verificarCsv(self):
        try:
            arquivo = pd.read_csv('resultados.csv', sep=';')
            return arquivo

        except:
            columas = ['Nome', 'Idade', 'Gênero', 'Resposta 1', 'Resposta 2', 'Resposta 3', 'Resposta 4', 'Resposta 5', 'Data a hora']
            arquivo = pd.DataFrame(columns= columas, inplece= True)
            arquivo.to_csv('resultados.csv', sep=';', index=False)
            return self.verificarCsv()


    def pyToCsv(self, respostas):
        dados = self.verificarCsv()
        dados = pd.concat([dados, pd.DataFrame.from_records(respostas)])
        dados = dados.append(respostas, ignore_index=True)
        dados.to_csv('resultados.csv', sep=';', index=filterfalse)
