'''
	Desenvolva um código que utilize as seguintes características de um veículo:
	- Quantidade de rodas;
	- Peso bruto em quilogramas;
	- Quantidade de pessoas no veículo.

	Com essas informações, o programa mostrará qual é a melhor categoria de habilitação para o veículo informado a partir das condições:
	A: Veículos com duas ou três rodas;
	B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
	C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
	D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas; E: Veículos com quatro rodas ou mais e com mais de 6000 kg.
'''

quantidadeRodas = int(input("Informe a quantidade de rodas do vículo: "))
quantidadeDePessoas = int(input("Informe capacidade maxima de pessoas: "))
pesoEmQuilos = float(input("Informe o peso do vículo: "))


if (quantidadeRodas == 2 or quantidadeRodas == 3):
  print("\nCategoria A")
elif (quantidadeRodas == 4 and quantidadeDePessoas <= 8 and pesoEmQuilos <= 3500):
  print("\nCategoria B")
elif (quantidadeRodas == 4 and (pesoEmQuilos >= 3500 or pesoEmQuilos <= 6000)):
  print("\nCategoria C")
elif (quantidadeRodas >= 4 and quantidadeDePessoas > 8):
  print("\nCategoria D")
elif (quantidadeRodas >= 4 and pesoEmQuilos > 6000):
  print("\nCategoria E")
else:
	print("\nInformações incorretas")