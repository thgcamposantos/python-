numero1 = input('Digite um número: ')
numero2 = input('Digite um número: ')

int_numero1 = int(numero1)
int_numero2 = int(numero2)

if int_numero1 == int_numero2:
    print('Numeros iguais')
elif int_numero1 > int_numero2:
    print(f'Numero 1 maior que numero 2, {numero1} > {numero2}')
else:
    print(f'Numero 2 maior que numero 1, {numero2} > {numero1}')
