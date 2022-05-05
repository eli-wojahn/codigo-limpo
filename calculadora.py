
# inserir string para escolher operação
calcula = input("Digite a operação desejada (soma, sub, mult, div): ")

# variáveis com entrada de números
numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")

if calcula == "soma":
	resultado = int(numero1) + int(numero2)
if calcula == "sub":
	resultado = int(numero1) - int(numero2)
if calcula == "mult":
	resultado = int(numero1) * int(numero2)
if calcula == "div":
	resultado = int(numero1) / int(numero2)
else:
	resultado = "Operação não suportada"
    
print("O resultado da operação é: ", resultado)
