nome_usuario = input('Digite seu primeiro nome: ')
tamanho_nome = int(len(nome_usuario))
print(tamanho_nome)
if tamanho_nome <= 4:
    print('Nome curto')
elif tamanho_nome > 4 and tamanho_nome <=6:
    print('Nome normal')
else:
    print('Nome grande')