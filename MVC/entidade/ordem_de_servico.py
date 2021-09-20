
class OrdemDeServico:

    def __init__(self, id_ordem, diagnostico: str, cpf_cliente):
        self.__id_ordem = id_ordem
        self.__diagnostico = diagnostico
        self.__cpf_cliente = cpf_cliente

    @property
    def cpf_cliente(self):
        return self.__cpf_cliente

    @property
    def get_id(self):
        return self.__id_ordem

    @property
    def get_diagnostico(self):
        return self.__diagnostico
