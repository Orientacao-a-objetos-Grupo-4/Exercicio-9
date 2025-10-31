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