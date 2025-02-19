#1

def comparar_par_impar(num1, num2):
    if num1 % 2 == 0:
        resultado1 = "par"
    else:
        resultado1 = "ímpar"
    
    if num2 % 2 == 0:
        resultado2 = "par"
    else:
        resultado2 = "ímpar"
    
    print(f"O primeiro número é {resultado1} e o segundo número é {resultado2}.")

comparar_par_impar(4, 7)

#2

def multiplicar_tres_numeros(num1, num2, num3):
    resultado = num1 * num2 * num3
    return resultado

print(multiplicar_tres_numeros(2, 3, 4))

#3

def elevar_numero(base, expoente):
    resultado = base ** expoente
    return resultado

print(elevar_numero(2, 3))

#4

def mensagem_personalizada(idade):
    if idade == 18:
        print("Parabéns, você acabou de completar 18 anos!")
    else:
        print("Idade não é 18.")

mensagem_personalizada(18)

#5

def calcular_idade(ano_nascimento, ano_atual):
    idade = ano_atual - ano_nascimento
    return idade

print(calcular_idade(2005, 2025))

#6

def brasil_ganhou_copa_1999():
    copa_1999 = "Brasil não ganhou a Copa de 1999."
    return copa_1999

print(brasil_ganhou_copa_1999())

#7
def menu_restaurante():
    print("Bem-vindo ao nosso restaurante!")
    print("Escolha uma opção de prato:")
    print("1. Salada")
    print("2. Macarronada")
    print("3. Sanduíche")
    print("4. Sorvete")

    opcao = int(input("Digite o número da sua escolha: "))

    if opcao == 1:
        print("Você escolheu Salada!")
    elif opcao == 2:
        print("Você escolheu Macarronada!")
    elif opcao == 3:
        print("Você escolheu Sanduíche!")
    elif opcao == 4:
        print("Você escolheu Sorvete!")
    else:
        print("Opção inválida! Por favor, escolha um número de 1 a 4.")

menu_restaurante()


