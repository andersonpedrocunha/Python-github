resposta = input('Pablo, qual é a música?')
print(resposta)

idade = input('Pablo, qual a sua idade?')

idade = idade.strip()
if not idade.isnumeric():
	print('errou feio, errou rude')
	
else:
	ano_que_vem = int(idade) + 1
  
	print('minha idade ano que vem é', ano_que_vem)
