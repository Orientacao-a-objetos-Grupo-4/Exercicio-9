from Pessoa import Pessoa

class Dependente(Pessoa):
    def __init__(self, parentesco, nascimento):
        super().__init__()
        self.__parentesco = parentesco
        self.__dataNascimento = nascimento

    def getParentesco(self):
        return self.__parentesco

    def setParentesco(self, parentesco):
        self.__parentesco = parentesco

    def getDataNascimento(self):
        return self.__dataNascimento

    def setDataNascimento(self, dataNascimento):
        self.__dataNascimento = dataNascimento
        