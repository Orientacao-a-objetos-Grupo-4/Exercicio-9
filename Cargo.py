class Cargo:
    def __init__(self, id, funcao, salario_bruto):
        self.__id = id
        self.__funcao = funcao
        self.__salario_bruto = salario_bruto

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getFuncao(self):
        return self.__funcao

    def setFuncao(self, funcao):
        self.__funcao = funcao

    def getSalario_bruto(self):
        return self.__salario_bruto

    def setSalario_bruto(self, salario_bruto):
        self.__salario_bruto = salario_bruto