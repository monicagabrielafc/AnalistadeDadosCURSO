# FASE 1 : IMPLEMENTAÇÃO BÁSICA

Mês = 0
Faturamento = 0 
Meses =  []
Faturamentos =  []


while True:
   Mês = input("Digite o nome mês: ")
   Meses.append(Mês)
   Faturamento = int(input("Digite o valor do faturamento: "))
   Faturamentos.append(Faturamento)
   if len (Meses) >= 3:
        break

print (Meses)
print (Faturamentos)

for i in range (len(Meses)):

    if Faturamentos[i] > 5000 and Faturamentos[i] < 200000:
        print (f"{Meses[i]} -{ Faturamentos [i]} - Dentro da margem")
    else:
        print (f"{Meses[i]} - {Faturamentos [i]} - Fora da margem")

Valor_total = 0
Maior = 0
for faturamento in Faturamentos:
    Valor_total += faturamento

    media = sum(Faturamentos) / len (Faturamentos)
print(f"Média do faturamento: {media}")

print (F"O TOTAL DO FATURAMENTO É {Valor_total}!!!")
print(F"MAIOR VALOR É {Maior}")