
import mysql.connector

class Pizza:
    def __init__(self):
        self.__conexao = mysql.connector.connect(
            host = 'localhost',
            user = 'dasilva',
            password = '1234',
            database = 'pizzaria'
        )
        self.__cursor = self.__conexao.cursor()
        self.criar_tabela()

    def criar_tabela(self):
      query = (''' 
               create table if not exists pizzas(id int auto_increment primary key, nome varchar(255) not null, tamanho varchar(255) not null default 'grande', preco decimal(10,2))''')
      
      
      self.__cursor.execute(query)
      self.__conexao.commit()
      
    def adicionar_pizza(self, nome, tamanho, preco):
        self.__cursor.execute('insert into pizzas(nome, tamanho, preco) values(%s, %s, %s)', (nome, tamanho,  preco))
        self.__conexao.commit()
        print("pizza adiconada com sucesso!")
        
    def listar_pizzas(self):
        self.__cursor.execute("select * from pizzas")
        pizza = self.__cursor.fetchall()
        
        if not pizza:
            print("pizzas nao cadastradas")