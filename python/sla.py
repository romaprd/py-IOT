import os
ingredientes = []

def titulo():
    print("""
████████╗░█████╗░██████╗░████████╗░█████╗░  ██████╗░███████╗  ███╗░░░███╗███████╗██╗░░░░░███████╗
╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗  ██╔══██╗██╔════╝  ████╗░████║██╔════╝██║░░░░░██╔════╝
░░░██║░░░██║░░██║██████╔╝░░░██║░░░███████║  ██║░░██║█████╗░░  ██╔████╔██║█████╗░░██║░░░░░█████╗░░
░░░██║░░░██║░░██║██╔══██╗░░░██║░░░██╔══██║  ██║░░██║██╔══╝░░  ██║╚██╔╝██║██╔══╝░░██║░░░░░██╔══╝░░
░░░██║░░░╚█████╔╝██║░░██║░░░██║░░░██║░░██║  ██████╔╝███████╗  ██║░╚═╝░██║███████╗███████╗███████╗
░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝  ╚═════╝░╚══════╝  ╚═╝░░░░░╚═╝╚══════╝╚══════╝╚══════╝""")
    

        
def adicionar_ingredientes():
    os.system("cls")
    while True:
        ingrediente = input("informe o nome dos ingredientes: ")
        ingredientes.append(ingrediente)
        print("ingredinte salvo com sucesso!!\n")
        op = input("gostaria de adicionar novos ingredientes (s/n): ")
        if op == "n" or op == "N":
            principal()
        elif op == "s" or op == "S":
            adicionar_ingredientes()
                 
def remover_ingredientes():
    os.system("cls")
    while True:
        exibir_ingredientes()
        resposta = int(input("informe o index do ingrediente que voce deseja remover: "))
        if resposta <= 0 or resposta>len(ingredientes):
            print("o index informado nao existe!!")
        else:
            ingredientes.pop(resposta -1)
            print("ingrediente removido com sucesso!!")
            
            op = input("gostaria de remover mais ingredientes (s/n): ")
            if op.lower() == "n":
                break
            
def exibir_ingredientes():
    os.system("cls")
    print("\n")
    print("os ingredientes sao: \n")
    for i, ingrediente in enumerate(ingredientes):
        print(i + 1, ". ", ingrediente)
        print("\n")
    exibir_menu()

     
def exibir_menu():
    print("\n")
    print("1. adicionar ingredietes\n2. exibir ingredientes\n3. remover ingredientes\n4. voltar ao menu inicial\n5. sair\n")
    
    op = int(input("escolha uma opcao de um a cinco: "))
    match op:
        case 1:
            adicionar_ingredientes()
        case 2:
            exibir_ingredientes()
        case 3:
            remover_ingredientes()
        case 4:
            principal()
        case 5:
            print("sando...")
            exit()
        case _:
            pass
            
def principal():
    os.system("cls")
    titulo()
    exibir_menu()
    
if __name__ == "__main__":
        principal()