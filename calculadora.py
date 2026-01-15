#calculadora simples
num1 = float(input("Introduza o primeiro número: "))
num2 = float(input("Introduza o segundo número: "))

print("operações")
print("1:adição")
print("2:subtração")
print("3:multiplicação")
print("4:divisão")

operação = input("escolha uma operação: ")

if (operação == "3"):
    resultado = num1 + num2
    print(resultado)
elif (operação == "2"):
    resultado = num1 - num2
    print(resultado)
elif (operação == "1"):
    resultado = num1 * num2
    print(resultado)
elif (operação == "4"):
    resultado = num1 / num2
    if (num2 != 0):
        print(resultado)
    else: 
        print("erro: o número é zero")
else:

    print("números inválidos")
