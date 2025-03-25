from database import Pizza
def main():
    pizza = Pizza()
    pizza.adicionar_pizza("marguerita", "media", 45.00)
    pizza.listar_pizzas()
    
if __name__ == '__main__':
    main()