
# class Pessoa: 
#     # construtor
#     def __init__(self, nome, idade, cidade):
#       self.__nome = nome
#       self.__idade = idade
#       self.__cidade = cidade

      #getter

    # def set_nome(self, novo_nome):
    #     self.__nome = novo_nome

    # def get_nome(self):
    #      return self.__nome
      
    # def set_idade(self, valor):
    #      self.__idade += valor

    # def get_idade(self):
    #     return self.__idade
      
    # @property
    # def nome(self, novo_nome):
    #    self.__nome = novo_nome

    # @nome.setter
    # def nome(self, novo_nome):
    #    self.__nome = novo_nome

    # @property
    # def idade(self):
    #    return self.__idade
    
    # @idade.setter
    # def idade(self, valor):
    #    self.__idade += valor

    # def apresentar(self):
    #    print(f"o meu nome eh: {self.__nome}, moro em: {self.__cidade}, e tenho {self.__idade} anos de idade!")
class Funcionarios:

    #construtor
    def __init__(self, nome, cargo, salario):
        self.__nome = nome
        self.__cargo = cargo
        self.__salario = salario

    def apresentar(self):
        print(f"funcionario: {self.__nome}")
        print(f"cargo: {self.__cargo}")
        print(f"salario: {self.__salario: .2f}")

    def aplicar_aumento(self, valor):
        self.__salario *= (1 + valor/100)

    @property
    def cargo(self):
        return self.__cargo
    
    @cargo.setter
    def cargo(self, novo_cargo):
        self.__cargo = novo_cargo
