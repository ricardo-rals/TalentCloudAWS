'''
    Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
    A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

    Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.
'''

repetir = True
anoAtual = 2022

while repetir == True :
    try:
        nomeCompleto = str(input("Informe o nome completo: "))
        anoNascimento = int(input("Informe o ano de nascimento: "))

        if anoNascimento >= 1922 and anoNascimento <= 2021 and anoNascimento != None:
            idade = anoAtual - anoNascimento
            print(f"\nNome completo: {nomeCompleto}")
            print(f"Idade: {idade}")
            repetir = False
        else:
            print("O ano precisa ser entre 1922 e 2021")
       
       
        
    except ValueError as err :
        print("")
        print(f'\nErro detectado: {err}')
        print("Por favor informe o ano correto")
        print("")

