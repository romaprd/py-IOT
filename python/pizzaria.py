
pizzas = []
pedidos = []

def titulo():
    print("""
██████╗░██╗███████╗███████╗░█████╗░██████╗░██╗░█████╗░  ██╗░░██╗░█████╗░████████╗
██╔══██╗██║╚════██║╚════██║██╔══██╗██╔══██╗██║██╔══██╗  ██║░░██║██╔══██╗╚══██╔══╝
██████╔╝██║░░███╔═╝░░███╔═╝███████║██████╔╝██║███████║  ███████║██║░░██║░░░██║░░░
██╔═══╝░██║██╔══╝░░██╔══╝░░██╔══██║██╔══██╗██║██╔══██║  ██╔══██║██║░░██║░░░██║░░░
██║░░░░░██║███████╗███████╗██║░░██║██║░░██║██║██║░░██║  ██║░░██║╚█████╔╝░░░██║░░░
╚═╝░░░░░╚═╝╚══════╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚═╝  ╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░

░░░░░░░░░███╗░░░█████╗░
░░██╗░░░████║░░██╔══██╗
██████╗██╔██║░░╚█████╔╝
╚═██╔═╝╚═╝██║░░██╔══██╗
░░╚═╝░░███████╗╚█████╔╝
░░░░░░░╚══════╝░╚════╝░""")
    
def cadastrar_pizza():
   
    nome = input("Digite o nome da pizza: ")
    sabor = input("Digite o sabor da pizza: ")
    preco = float(input("Digite o preço da pizza: "))
    pizza = {'nome': nome, 'sabor': sabor, 'preco': preco}
    pizzas.append(pizza)
    print(f"Pizza {nome} cadastrada com sucesso!\n")

def adicionar_pizza():
   
    if pizzas:
        print("\nPizzas cadastradas:")
        for i, pizza in enumerate(pizzas, 1):
            print(f"{i}. {pizza['nome']} - {pizza['sabor']} - R${pizza['preco']:.2f}")
        opcao = int(input("\nEscolha a pizza pelo número para adicionar ao pedido: "))
        if 1 <= opcao <= len(pizzas):
            pizza = pizzas[opcao - 1]
            pedidos.append(pizza)
            print(f"\nPizza {pizza['nome']} adicionada ao pedido!\n")
        else:
            print("\nOpção inválida!")
    else:
        print("\nNenhuma pizza cadastrada ainda.\n")

def listar_pizzas():
    
    if pizzas:
        print("\nPizzas cadastradas:")
        for pizza in pizzas:
            print(f"Nome: {pizza['nome']}, Sabor: {pizza['sabor']}, Preço: R${pizza['preco']:.2f}")
    else:
        print("\nNenhuma pizza cadastrada.\n")

def listar_pedidos():
   
    if pedidos:
        print("\nPizzas no pedido:")
        for pizza in pedidos:
            print(f"Nome: {pizza['nome']}, Sabor: {pizza['sabor']}, Preço: R${pizza['preco']:.2f}")
    else:
        print("\nNenhuma pizza foi adicionada ao pedido ainda.\n")

def remover_pizza():
  
    if pizzas:
        print("\nPizzas cadastradas:")
        for i, pizza in enumerate(pizzas, 1):
            print(f"{i}. {pizza['nome']} - {pizza['sabor']} - R${pizza['preco']:.2f}")
        opcao = int(input("\nEscolha a pizza pelo número para remover: "))
        if 1 <= opcao <= len(pizzas):
            pizza = pizzas.pop(opcao - 1)
            print(f"\nPizza {pizza['nome']} removida com sucesso!\n")
        else:
            print("\nOpção inválida!")
    else:
        print("\nNenhuma pizza cadastrada para remover.\n")

def remover_pizza_do_pedido():
    
    if pedidos:
        print("\nPizzas no pedido:")
        for i, pizza in enumerate(pedidos, 1):
            print(f"{i}. {pizza['nome']} - {pizza['sabor']} - R${pizza['preco']:.2f}")
        opcao = int(input("\nEscolha a pizza pelo número para remover do pedido: "))
        if 1 <= opcao <= len(pedidos):
            pizza = pedidos.pop(opcao - 1)
            print(f"\nPizza {pizza['nome']} removida do pedido com sucesso!\n")
        else:
            print("\nOpção inválida!")
    else:
        print("\nNenhuma pizza foi adicionada ao pedido.\n")

def menu():
    titulo()
    
    while True:
        print("\n--- MENU DA PIZZARIA ---")
        print("1. Cadastrar Pizza")
        print("2. Adicionar Pizza ao Pedido")
        print("3. Listar Pizzas")
        print("4. Listar Pizzas no Pedido")
        print("5. Remover Pizza do Menu")
        print("6. Remover Pizza do Pedido")
        print("7. Sair")
        
        opcao = input("Escolha uma opção (1-7): ")
        
        if opcao == '1':
            cadastrar_pizza()
        elif opcao == '2':
            adicionar_pizza()
        elif opcao == '3':
            listar_pizzas()
        elif opcao == '4':
            listar_pedidos()
        elif opcao == '5':
            remover_pizza()
        elif opcao == '6':
            remover_pizza_do_pedido()
        elif opcao == '7':
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")


menu()
