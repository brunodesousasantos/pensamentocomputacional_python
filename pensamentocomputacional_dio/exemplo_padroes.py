arroz_kg = 6.57
feijao_kg = 8.35
carne_kg = 32.74


# a linha 7 é uma linha de codigo de repetição executada 3 vezes
for i in range(3):
    valor = input()
    valor = float(valor)
    if valor <= 10.00:
        print('Posso comprar')
    else:
        print('Não posso comprar')

# a linha 8 input() é para entrada de dados pelo usuario. Os dados digitados são strings
# a linha 9 float(valor) converte o dado da variavel valor que é string em numero.