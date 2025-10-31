class Pessoa:
    def __init__(self):
        self.__id = None
        self.__nome = None
        self.__nascimento = None
        self.__cpf = None

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getNascimento(self):
        return self.__nascimento

    def setNascimento(self, nascimento):
        self.__nascimento = nascimento

    def getCpf(self):
        return self.__cpf

    def setCpf(self, cpf):
        self.__cpf = cpf