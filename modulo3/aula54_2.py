numero_usuario_int = int(input('Digite a hora: '))
if numero_usuario_int <= 11:
    print('Bom dia')
elif numero_usuario_int > 11 and numero_usuario_int <= 17:
    print('Boa tarde')
else:
    print('Boa noite')
