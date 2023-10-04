'''
    Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
    1. Soma
    2. Subtração
    3. Multiplicação
    4. Divisão

    Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.
'''
def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    return num1 / num2

def calculadora(num1, num2, operador):
    if operador == 1 :
        return soma(num1,num2)
    elif operador == 2 :
        return subtracao(num1, num2)
    elif operador == 3 :
        return multiplicacao(num1, num2)
    elif operador == 4 :
        return divisao(num1, num2)
    else :
        return 0


num1 = float(input("Informe o primeiro valor: "))
num2 = float(input("Informe o segundo valor: "))
operador = int(input("ESCOLHA O NUMERO EQUIVALENTE A CADA OPERAÇÃO" +
                      "\n1. Soma" + 
                      "\n2. Subtração" + 
                      "\n3. Multiplicação" + 
                      "\n4. Divisão" + 
                      "\nOperação: "))

print(calculadora(num1, num2, operador))