from abc import ABC, abstractmethod


class Pessoa(ABC):

    @abstractmethod
    def __init__(self, cpf, nome, data_nascimento, fone, endereco):
        self.__cpf = cpf
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__fone = fone
        self.__endereco = endereco

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf1):
        self.__cpf = cpf1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nomee):
        self.__nome = nomee

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, dat_nascimento):
        self.__data_nascimento = dat_nascimento

    @property
    def fone(self):
        return self.__fone

    @fone.setter
    def fone(self, tel):
        self.__fone = tel

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, enderc):
        self.__endereco = enderc
