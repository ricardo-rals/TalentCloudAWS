def dividirDoisNumeros() :
    divisao = False

    while divisao == False :
        try:
            numerador = int(input("Digite o numerador: "))
            denominador = int(input("Digite o denominador: "))
            
            if denominador == 0:
                raise ZeroDivisionError("Divisão por zero não é permitida.")
            
            resultado = numerador / denominador
            divisao = True
            print(f"Resultado da divisão: {round(resultado, 5)}")
        except ValueError:
            print("Insira apenas números inteiros.")

        except ZeroDivisionError as e:
            print(e)


for i in range(2,10):
    print(i)