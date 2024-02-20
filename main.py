nome_usuario = input("Digite o seu nome: ")

salario_usuario = float(input("Digite o seu salario: "))

bonus_usuario = float(input("DIgite o seu bonus: "))

valor_do_bonus = 1000 + salario_usuario * bonus_usuario

print(f"O usuario {nome_usuario} possui o bonus de {valor_do_bonus}")
