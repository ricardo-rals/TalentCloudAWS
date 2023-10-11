
lista_produtos = [] 
lista_atualizados = {}
produtos_removidos = []

def adicionar_produto():
    produto = input("Digite o produto do produto: ")
    lista_produtos.append(produto)
    print(f"{produto} foi adicionado com sucesso!")


def atualizar_produto():
    while True:
        nome = input("Digite o nome do produto que deseja atualizar (ou 0 para voltar ao menu principal): ")
        if nome == "0":
            break
        if nome in lista_produtos:
            novo_nome = input("Digite o novo nome do produto: ")
            lista_atualizados[nome] = novo_nome
            index = lista_produtos.index(nome)
            lista_produtos[index] = novo_nome

            print(f"{nome} foi atualizado com sucesso!")
        else:
            print(f"{nome} não foi encontrado na lista de produtos.")

def remover_produto():
    while True:
        nome = input("Digite o nome do produto que deseja remover (ou 0 para voltar ao menu principal): ")
        if nome == "0":
            break
        if nome in lista_produtos:
            produtos_removidos.append(nome)
            lista_produtos.remove(nome)

            print(f"{nome} foi removido com sucesso!")
        else:
            print(f"{nome} não foi encontrado na lista de produtos.")

def mostrar_produtos():
    print("Lista de produtos:")
    for nome in lista_produtos:
        print(nome)


def mostrar_produtos_atualizados():
    print("Produtos atualizados:")
    for produto_antigo, novo_produto in lista_atualizados.items():
        print(f"Antigo: {produto_antigo}, Novo: {novo_produto}")

def mostrar_produtos_removidos():
    print("Produtos removidos:")
    for nome in produtos_removidos:
        print(nome)

while True:
    print("\nMenu:")
    print("1. Adicionar um novo produto")
    print("2. Atualizar um produto existente")
    print("3. Remover um produto")
    print("4. Mostrar todos os produtos")
    print("5. Mostrar produtos removidos")
    print("6. Mostrar relação de produtos atualizados")
    print("0. Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == "1":
       adicionar_produto()

    elif escolha == "2":
        atualizar_produto()

    elif escolha == "3":
        remover_produto()

    elif escolha == "4":
        mostrar_produtos()
    
    elif escolha == "5":
        mostrar_produtos_removidos()

    elif escolha == "6":
        mostrar_produtos_atualizados()
            
    elif escolha == "0":
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")


