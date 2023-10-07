'''
    Declare dois arrays, cada um com um mínimo de cinco elementos, e imprima eles no terminal usando o comando print(). O primeiro array deve conter os produtos de uma loja da sua escolha (loja de comida, materiais de construção, música, etc). O segundo array deve conter os anos de nascimento de familiares e amigos seus. Lembre-se de usar nomes descritivos para nomear cada variável, e de usar o tipo de dado apropriado para cada lista (strings, booleanos, números inteiros, floats).
'''
def registrarProdutos():
    produtos = []
    while True:
        try:
          if len(produtos) < 5:
              produto = input("Informe um produto da loja: ")

          else:
              produto = input("Informe um produto da loja (ou digite '0' para parar): ")

          if produto == '0':
              if len(produtos) < 5:
                  raise Exception("É necessário registrar pelo menos 5 produtos.")
              
              else:
                  break
              
          produtos.append(produto)

        except Exception as e:
            print(f"Ocorreu um erro ao registrar o produto: {e}")
    
    return produtos

def registrarAnoNascimento():
    anos = []
    while True:
        try:
            if len(anos) < 5:
                ano = input("Informe um ano de nascimento: ")

            else:
                ano = input("Informe um ano de nascimento (ou digite '0' para parar): ")

            if ano == '0':
                if len(anos) < 5:
                    raise Exception("É necessário registrar pelo menos 5 anos.")
                
                else:
                    break
                
            anos.append(ano)

        except Exception as e:
            print(f"Ocorreu um erro ao registrar o ano de nascimento: {e}")
  
    return anos


def imprimirLista(lista):
    for indice, elemento in enumerate(lista):
        print(f"Índice {indice + 1}: {elemento}")

listaProdutos = []
listaAnosNascimento = []

while True:
    try:
        print("Registrando produtos: (INSIRA PELO MENOS 5 PRODUTOS)")
        listaProdutos += registrarProdutos()
        
        print("Registrando anos de nascimento: (INSIRA PELO MENOS 5 ANOS)")
        listaAnosNascimento += registrarAnoNascimento()

        continuar = input("Deseja continuar? (Digite '0' para parar): ")
        if continuar == '0':
            break

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

print("Lista de produtos registrados:")
imprimirLista(listaProdutos)

print("Lista de anos de nascimento registrados:")
imprimirLista(listaAnosNascimento)

