class ContaBancaria:
   def __init__(self, nome):
      self.__nome = nome
      self.__saldo = 0

   def ver_saldo(self):
      print(f"{self.__nome}, seu saldo eh de: R$ {self.__saldo: .2f}")

   def depositar(self, valor):
      if valor <= 0:
         self.__saldo += valor
         if valor >= 0:
            self.__saldo -= valor
            print("saque efetuado com sucesso!!")
         else:
            print("o valor nao pode ser negativo!!")
      else:
         print("o valor nao pode ser negativo ou igual a zero!")

      self.__saldo += valor

   def sacar(self, valor):
      self.__saldo -= valor
    