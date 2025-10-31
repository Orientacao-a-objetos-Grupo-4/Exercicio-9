from Pessoa import Pessoa

class Dependente(Pessoa):
    def __init__(self, parentesco, nascimento):
        super().__init__()
        self.__parentesco = parentesco
        self.__dataNascimento = nascimento
        