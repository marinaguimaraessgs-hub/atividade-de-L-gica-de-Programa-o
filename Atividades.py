# 1. Verificador de Par ou Ímpar

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")


# 2. Classificador de Idade

idade = int(input("\nDigite a idade: "))

if idade >= 0 and idade <= 12:
    print("Criança")
else:
    if idade >= 13 and idade <= 17:
        print("Adolescente")
    else:
        if idade >= 18 and idade <= 64:
            print("Adulto")
        else:
            if idade >= 65:
                print("Idoso")
            else:
                print("Idade inválida.")


# 3. Mini Calculadora

numero1 = float(input("\nDigite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = int(input("Escolha uma operação: "))

if operacao == 1:
    resultado = numero1 + numero2
    print("Resultado:", resultado)
else:
    if operacao == 2:
        resultado = numero1 - numero2
        print("Resultado:", resultado)
    else:
        if operacao == 3:
            resultado = numero1 * numero2
            print("Resultado:", resultado)
        else:
            if operacao == 4:
                resultado = numero1 / numero2
                print("Resultado:", resultado)
            else:
                print("Operação inválida.")


# 4. Classificador de Triângulos

a = float(input("\nDigite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))

if a + b > c and a + c > b and b + c > a:

    if a == b and b == c:
        print("Triângulo Equilátero")
    else:
        if a == b or a == c or b == c:
            print("Triângulo Isósceles")
        else:
            print("Triângulo Escaleno")

else:
    print("Os lados não formam um triângulo válido.")


# 5. Equação do Segundo Grau

a = float(input("\nDigite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b**2 - 4*a*c

print("Delta =", delta)

if delta > 0:
    print("A equação possui duas raízes reais distintas.")
else:
    if delta == 0:
        print("A equação possui uma raiz real.")
    else:
        print("A equação não possui raízes reais.")


# 6. Estado Físico da Água

temperatura = float(input("\nDigite a temperatura da água: "))

if temperatura <= 0:
    print("Sólido")
else:
    if temperatura < 100:
        print("Líquido")
    else:
        print("Gasoso")


# 7. Comissão do Corretor

nome = input("\nDigite o nome do corretor: ")
venda = float(input("Digite o valor da venda: "))

if venda <= 500000:
    comissao = venda * 0.06
else:
    if venda <= 700000:
        comissao = venda * 0.085
    else:
        if venda <= 1000000:
            comissao = venda * 0.10
        else:
            comissao = venda * 0.12

print("\n--- RELATÓRIO DO CORRETOR ---")
print("Nome:", nome)
print("Valor da venda: R$", venda)
print("Comissão: R$", comissao)


# 8. Valor da Hospedagem

nome = input("\nDigite o nome do hóspede: ")
dias = int(input("Digite quantos dias ficou hospedado: "))

if dias > 7:
    taxa = 6.50
else:
    if dias == 7:
        taxa = 12.00
    else:
        taxa = 16.50

total = (290 + taxa) * dias

print("\n--- CONTA DO HÓSPEDE ---")
print("Nome:", nome)
print("Total da conta: R$", total)
