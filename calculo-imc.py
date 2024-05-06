
#Realiza o calculo do IMC
def calcula_imc(peso, altura):

    return peso / (altura**2)


#Classifica qual tipo de IMC é o seu
def tipo_imc(imc):

    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"
    
# Solicitação de entrada do usuário
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

# Calcula o IMC
imc = calcula_imc(peso, altura)

# Classifica o IMC
categoria = tipo_imc(imc)

# Exibe o resultado
print("Seu IMC é:", imc)
print("Você está na categoria:", categoria)
