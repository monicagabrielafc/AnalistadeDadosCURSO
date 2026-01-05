# Solicitar 12 temperaturas de acordo com cada mês
# Ordenar temperaturas da maior para menor


temperatura = 0
temperaturas = []
Mês = 0
Meses = []
Nome = 0

Nome = input ("Para iniciarmos, por favor, digite seu nome: ")
while True:
   Mês = input(f"Certo {Nome}! Agora digite o nome mês: ")      
   temperatura = input(f"Digite a temperatura do mês de {Mês}. Caso não seja esse mês, digite CORRIGIR: ")
   if temperatura == "CORRIGIR":
       continue
   Meses.append(Mês)
   temperaturas.append(int(temperatura))
   if len (Meses) >= 2:
        break

maior = max(temperaturas)
menor = min(temperaturas)  
media = sum(temperaturas)/(len(temperaturas))
mesmaior = Meses[temperaturas.index(maior)]
mesmenor = Meses[temperaturas.index(menor)]

print (f"{Nome}, de acordo com os dados que você forneceu, temos as seguintes conclusões: ")
print(f"A maior temperatura foi {maior}°C no mês de {mesmaior}")
print(f"A menor temperatura foi {menor}°C no mês de {mesmenor}")
print (f"A média das temperaturas foi: {media}")

print ("Lista das Temperaturas:")
contador = 0
for t in sorted(temperaturas, reverse=True): #ler o original e nos dar uma lista ordenada do maior para maior, mas para analisar dados usa os dados otiginais.

    print(f"{contador+1}. {t:.1f}°C ")
    contador += 1