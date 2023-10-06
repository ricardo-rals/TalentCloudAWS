'''
    Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:

    1: Soma
    2: Subtração
    3: Multiplicação
    4: Divisão
    0: Sair

    Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

    Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar.

    É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado
'''


def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    return num1 / num2

def recebeNumeros():
    num1 = float(input("Informe o primeiro valor: "))
    num2 = float(input("Informe o segundo valor: "))

    return num1, num2

def calculadora(operador):
    if operador == 1:
        num1, num2 = recebeNumeros()
        resultado = soma(num1, num2)

    elif operador == 2:
        num1, num2 = recebeNumeros()
        resultado = subtracao(num1, num2)

    elif operador == 3:
        num1, num2 = recebeNumeros()
        resultado = multiplicacao(num1, num2)

    elif operador == 4:
        num1, num2 = recebeNumeros()
        resultado = divisao(num1, num2)

    elif operador == 0:
        return "Saindo..."
    
    else:
        return "Essa opção não existe"

    return f"Resultado: {resultado}\n\n"


operador = int(input("ESCOLHA O NUMERO EQUIVALENTE A CADA OPERAÇÃO" +
                      "\n1. Soma" + 
                      "\n2. Subtração" + 
                      "\n3. Multiplicação" + 
                      "\n4. Divisão" + 
                      "\n0. Sair " +
                      "\n\nEscolha: \n"))
print(calculadora(operador))

while operador != 0 :
    operador = int(input("ESCOLHA O NUMERO EQUIVALENTE A CADA OPERAÇÃO" +
                      "\n1. Soma" + 
                      "\n2. Subtração" + 
                      "\n3. Multiplicação" + 
                      "\n4. Divisão" + 
                      "\n0. Sair " +
                      "\n\nEscolha:"))
    print(calculadora(operador))