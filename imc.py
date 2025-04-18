## Cálculo do IMC com classificação da OMS

# Entrada de dados
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# Cálculo do IMC
imc = peso / (altura ** 2)
print(f"\nSeu IMC é: {imc:.2f}\n")

# Classificação segundo a OMS
if imc < 18.5:
    print("Classificação: Baixo peso")
    print("Recomendação: Procure um médico para uma avaliação criteriosa. Pode haver risco devido a poucas reservas nutricionais.")
elif 18.5 <= imc < 25:
    print("Classificação: Peso adequado")
    print("Recomendação: Tudo indica que está bem. Mas avalie também a composição corporal e circunferência abdominal.")
elif 25 <= imc < 30:
    print("Classificação: Sobrepeso")
    print("Recomendação: Risco aumentado para doenças como diabetes e hipertensão. Consulte um médico e revise seus hábitos.")
elif 30 <= imc < 35:
    print("Classificação: Obesidade Grau I")
    print("Recomendação: Busque orientação médica e nutricional, mesmo com exames normais.")
elif 35 <= imc < 40:
    print("Classificação: Obesidade Grau II")
    print("Recomendação: Quadro mais avançado. É importante procurar auxílio médico e nutricional.")
else:
    print("Classificação: Obesidade Grau III (mórbida)")
    print("Recomendação: Alto risco de comorbidades. Procure ajuda médica com urgência.")

print("\n--- Fim da análise ---")

