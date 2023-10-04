'''
    Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.

    Escreva um código que imprima todos os números exceto o número 13.
    Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de laços de repetição aprendidos.

    Como desafio, imprima eles em ordem decrescente (20, 19, 18...)
'''


andares = 20

for i in range(1, andares+1):
  if i == 13:
    continue
  else:
    print(f"Andar: {i}")
    
print("\n==================================================\n")

for i in range(andares, 0, -1):
  if i == 13:
    continue
  else:
    print(f"Andar: {i}")


# andares = 20

# while andares >= 1:
#     if andares != 13:
#          print(f"Andar: {andares}")
#     andares -= 1



# '''
# FEITO EM C, NÃO VAI EXECUTAR AQUI
# '''

# #include <stdio.h>

# int main() {
#     int andares = 20;
#     do {
#         if (andares != 13) {
#             printf("%d\n", andares);
#         }
#         andares--;
#     } while (andares >= 1);
#     return 0;
# }