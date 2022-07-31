#questão 2

number1= 1
number2= 0
askNumber = int(input('Digite qual número vc quer saber se existe: '))

if askNumber == 0:
    print("Seu número percente a sequência de Fibonacci!")

elif askNumber == 1:
    print("Seu número percente a sequência de Fibonacci!")

for x in range(0, askNumber-1):
    number1 +=number2
    number2= number1 - number2

    if askNumber == number1:
        print("Seu número percente a sequência de Fibonacci!")
        break

if askNumber != number1 and askNumber != 0:
    print("Seu número NÃO percente a sequência de Fibonacci!")
