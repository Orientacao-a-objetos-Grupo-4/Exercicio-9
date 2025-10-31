class Ocorrencia:
    def __init__(self, id, data_ocorrencia, valor_acrescimo, valor_desconto, descricao_ocorrencia, funcionario):
        self.__id = id
        self.__data_ocorrencia = data_ocorrencia
        self.__valor_acrescimo = valor_acrescimo
        self.__valor_desconto = valor_desconto
        self.__descricao_ocorrencia = descricao_ocorrencia
        self.__funcionario = funcionario

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getDataOcorrencia(self):
        return self.__data_ocorrencia

    def setDataOcorrencia(self, data_ocorrencia):
        self.__data_ocorrencia = data_ocorrencia

    def getValorAcrescimo(self):
        return self.__valor_acrescimo

    def setValorAcrescimo(self, valor_acrescimo):
        self.__valor_acrescimo = valor_acrescimo

    def getValorDesconto(self):
        return self.__valor_desconto

    def setValorDesconto(self, valor_desconto):
        self.__valor_desconto = valor_desconto

    def getDescricaoOcorrencia(self):
        return self.__descricao_ocorrencia

    def setDescricaoOcorrencia(self, descricao_ocorrencia):
        self.__descricao_ocorrencia = descricao_ocorrencia

    def getFuncionario(self):
        return self.__funcionario

    def setFuncionario(self, funcionario):
        self.__funcionario = funcionario

