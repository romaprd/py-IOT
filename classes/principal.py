
from Funcionario import Funcionarios

# variavel especial ==> obejto

f1 = Funcionarios("roma", "engenherio de software", 10000)
f1.apresentar()
# print(p1.__nome)
# print(p1.__idade)
# print(p1.__cidade)
# novo_nome = input("digite um novo nome: ")
# print(p1.get_nome())
# p1.set_nome(novo_nome)
# print(p1.get_nome())

# p1.set_idade(18)

# # print(p1.get_idade())
# print(p1.nome)
# p1.nome = novo_nome
# print(p1.nome)
# p1.idade = 18
# print(p1.idade)
f1.cargo = "genio"
f1.aplicar_aumento(10)
f1.apresentar()
