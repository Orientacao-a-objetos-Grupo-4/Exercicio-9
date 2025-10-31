from Pessoa import Pessoa

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

    def getDependentes(self):
        return self.__dependentes

    def setDependentes(self, dependentes):
        self.__dependentes = dependentes