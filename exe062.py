n = 0
cont = 0
soma = 0
while n != 999:
    n = int(input('Digite um numero [999 para parar]: '))
    if n != 999:
        soma += n
        cont += 1
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')
