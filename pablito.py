resposta = input('Pablo, qual é a música?')
print(resposta)

idade = input('Pablo, qual a sua idade?')

idade = idade.strip()
if idade.isnumeric():
    ano_que_vem = idade + 1
	print('minha idade ano que vem é', ano_que_vem)
	
else:
    print('Errou feio, errou rude.')
