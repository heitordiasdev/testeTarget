#questão 3

# letra a

# a sequência se dá entre númeras impares.

number = 1
numberlist = []
for x in range(5):
    numberlist.append(number)
    number +=2

print(f'Letra a: {numberlist}')

#letra b

# a sequência se dá onde o próximo número é o dobro do anterior.

number = 2
numberlist = []
for x in range(7):
    numberlist.append(number)
    number *=2

print(f'Letra b: {numberlist}')

#letra c

# O intervalo entre esses números é sempre números impares, sendo assim o intervalo do primeiro entre o segundo é 1
# entre o segundo e o terceiro é 3, e assim sempre somando o intervalo mais 2.

number = 0
cont = 1
numberlist = []
for x in range(8):
    numberlist.append(number)
    number +=cont
    cont += 2

print(f'Letra c: {numberlist}')

#letra d

# o intervalo começa em 12 e esse intervalo vai aumentando sucessivamente somando a 8.
# ex: intervalo = 12,20,28,36.

number = 4
cont = 12
numberlist = []
for x in range(5):
    numberlist.append(number)
    number +=cont
    cont += 8

print(f'Letra d: {numberlist}')

# letra e

# a soma dos dois anteriores é o próximo número
number1= 1
number2= 0
numberlist= []
for x in range(7):
    numberlist.append(number1)
    number1 +=number2
    number2= number1 - number2

print(f'Letra e: {numberlist}')

# letra f

# Se trata de uma lista de números com a letra "d", sendo assim, não pode ser implementado em lógica.
# ficando assim:

numberlist= [2,10, 12, 16, 17, 18, 19]
numberlist.append(200) #duzentos
print(f'Letra f: {numberlist}')
