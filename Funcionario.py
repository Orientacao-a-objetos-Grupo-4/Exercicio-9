from Pessoa import Pessoa
from datetime import date

class Funcionario(Pessoa):
    def __init__(self):
        super().__init__()
        self.__endereco = None
        self.__telefone = None
        self.__email = None
        self.__cargo = None
        self.__ocorrencias = []
        self.__dependentes = []

    def getEndereco(self):
        return self.__endereco

    def setEndereco(self, endereco):
        self.__endereco = endereco

    def getTelefone(self):
        return self.__telefone

    def setTelefone(self, telefone):
        self.__telefone = telefone

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    def getCargo(self):
        return self.__cargo

    def setCargo(self, cargo):
        self.__cargo = cargo

    def getOcorrencias(self):
        return self.__ocorrencias

    def setOcorrencias(self, ocorrencias):
        self.__ocorrencias = ocorrencias

    def addOcorrencia(self, ocorrencia):
        self.__ocorrencias.append(ocorrencia)

    def removeOcorrencia(self, ocorrencia):
        self.__ocorrencias.remove(ocorrencia)

    def getDependentes(self):
        return self.__dependentes

    def addDependente(self, dependente):
        self.__dependentes.append(dependente)

    def removeDependente(self, dependente):
        self.__dependentes.remove(dependente)

    def setDependentes(self, dependentes):
        self.__dependentes = dependentes

    def salarioLiquido(self, ano, mes):
        bruto = self.__cargo.getSalario_bruto()
        salario_final = 0
        for ocorrencia in self.__ocorrencias:
            if ocorrencia.getDataOcorrencia().year == ano and ocorrencia.getDataOcorrencia().month == mes:
                acrescimos = ocorrencia.getValorAcrescimo()
                descontos = ocorrencia.getValorDesconto()
                salario_final = bruto + acrescimos - descontos
        acrescimo_dependente = 0
        for dependente in self.__dependentes:
            idade = date.today().year - dependente.getDataNascimento().year
            if idade < 18:
                acrescimo_dependente += 100
        salario_final = salario_final + acrescimo_dependente
        return salario_final

    def listarDependentes(self):
        print("-= Dependentes =-")
        for dep in self.__dependentes:
            if date(day=dep.getDataNascimento().day , month=dep.getDataNascimento().month , year=date.today().year) < date.today():
                proximo_aniversario = date(day=dep.getDataNascimento().day , month=dep.getDataNascimento().month , year=date.today().year + 1)
            else:
                proximo_aniversario = date(day=dep.getDataNascimento().day, month=dep.getDataNascimento().month, year=date.today().year)
            dia_semana = ('Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sabado',
                          'Domingo')
            quantidade_dias = (proximo_aniversario - date.today()).days
            print(f"{dep.getNome()} ({dep.getParentesco()}) - Data Nascimento: {dep.getDataNascimento().strftime('%d/%m/%Y')}\n"
                  f"Idade: {date.today().year - dep.getDataNascimento().year}\n"
                  f"Próximo Aniversário: {proximo_aniversario.strftime('%d/%m/%Y')}\n"
                  f"Quantos dias faltam: {quantidade_dias}\n"
                  f"Dia da Semana: {dia_semana[proximo_aniversario.weekday()]}\n")
            print("-"*30)

