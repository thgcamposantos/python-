nome = input('Digite seu nome: ')
if(nome != " "):
    print(f'Seu nome é: {nome}')
    print('Seu nome tem ' , len(nome) , ' letras')
    print(f'Seu nome invertido é: {nome[::-1]}')
else:
    print('Desculpe')