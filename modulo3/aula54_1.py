numero_usuario = input('Digite um número inteiro: ')
try:
    numero_inteiro = int(numero_usuario)
    if numero_inteiro % 2 == 0:
        print('Número inteiro par , digitou o número' , numero_inteiro)
    else:
        print('Número inteiro impar , digitou o numero ' , numero_inteiro)
except:
    print('A informação digitada não se adequa aos requisitos pedido')

