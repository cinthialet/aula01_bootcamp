# 1) Solicita ao usuário que digite seu nome
nome_usuario = input("Digite seu nome: ")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
valor_salario = float(input("Valor do seu salário: "))

constante_bonus = 1000

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
valor_bonus = float(input("Valor do bônus recebido: "))

# 4) Calcule o valor do bônus final
valor_bonus_final = constante_bonus + valor_salario * valor_bonus

# 5) Imprima mensagem personalizada incluindo o nome do usuario e valor do bonus final
print(f"O usuario {nome_usuario} possui o bonus de {valor_bonus_final}") #testee


