'''
Copie o array apresentado embaixo no seu editor de código, e imprima no terminal: a quantidade de elementos que ele possui, o dado salvo no índice 2, o dado salvo no índice 9, e dado salvo no índice 14.

lista_musicos = [ 'Djavan', 'Roberto Carlos', 'Elis Regina', 'Tom Jobim', 'Milton Nascimento', 'Chico Buarque', 'Nara Leão', 'Pitty', 'Simonal', 'Moacir Santos', 'Caetano Veloso', 'Elza Soares', 'Paulinho da Viola', 'Yamandú Costa', 'Gal Costa'] 
'''

lista_musicos = [ 'Djavan', 'Roberto Carlos', 'Elis Regina', 'Tom Jobim', 'Milton Nascimento', 'Chico Buarque', 'Nara Leão', 'Pitty', 'Simonal', 'Moacir Santos', 'Caetano Veloso', 'Elza Soares', 'Paulinho da Viola', 'Yamandú Costa', 'Gal Costa'] 

quantidadeElementos = len(lista_musicos)

print(f'Quantidade de elementos: {quantidadeElementos}')

for indice, elemento in enumerate(lista_musicos):
    if indice == 2:
        print(f'Indice {indice}: {elemento}')
    if indice == 9:
        print(f'Indice {indice}: {elemento}')
    if indice == 14:
        print(f'Indice {indice}: {elemento}')