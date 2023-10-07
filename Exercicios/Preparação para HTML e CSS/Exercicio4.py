'''A loja de cosméticos ficou muito feliz com seu trabalho e chamaram você novamente! Dessa vez, eles precisam que você atualize o array de produtos. Agora, eles estão vendendo rímel ao invés de batons, e cremes hidratantes no lugar de loções. Além disso, ficaram sem delineadores, então precisam que você remova ele da lista de produtos. Imprima a nova lista no terminal para verificar que as alterações foram realizadas corretamente.

lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores'] 

Como desafio, adicione dois novos produtos da sua escolha à lista. '''

lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores'] 

#Criando um diciionário para relacionar os valores que precisam ser alterados
substituicoes = {
    "batons": "rímel",
    "loções": "cremes hidratantes",
}

while True:
    print("\nMenu:")
    print("1. Adicionar um novo item")
    print("2. Atualizar um item existente")
    print("3. Sair")
    
    escolha = input("Escolha uma opção (1/2/3): ")
    
    if escolha == "1":
        item = input("Digite um novo item a ser adicionado: ")
        lista_produtos.append(item)

    elif escolha == "2":
        item = input("Digite um item a ser atualizado: ")
        
        try:
            if item not in lista_produtos:
                raise ValueError(f"{item} não existe na lista de produtos. Por favor, escolha um item válido.")
            
            substituicao = input(f"Digite o novo valor de substituição para {item}: ")
            
            substituicoes[item] = substituicao
            
        except ValueError as e:
            print(e)
    elif escolha == "3":
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

#Um for para varrer a lista de produtos
for i in range(len(lista_produtos)):
    #Adiciono o pruduto que está no indice e depois procuro se ele está no dicionário, caso esteja ele, pego o valor referente a ao produto encontrado e atualizo o array de lista_produtos
    produto = lista_produtos[i]
    if produto in substituicoes:
        lista_produtos[i] = substituicoes[produto]

lista_produtos.remove('delineadores')
print("\nLista de produtos atualizada:")
print(lista_produtos)

print("\nDicionário de substituições atualizado:")
print(substituicoes)