num = int(input("Digite um número para calcular o fatorial: "))
resultado = 1
contador = 1

while contador <= num:
    resultado = resultado * contador
    contador = contador + 1

print(f'O fatorial de {num} é {resultado}.')
