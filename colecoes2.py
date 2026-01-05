# nomes = ["Mônica, Lucas, Mari, Bruna"]
# nomes.append() #add nomes ao final
# nomes.insert() #add nomes onde você preferir
# nomes[3] = "Mônica" #subsituir
# nomes.remove()
# nomes.pop()


qtd_idade = 0
idades = []

for i in range(3):
    idade = int(input("Digite sua idade: "))
    qtd_idade += 1
    idades.append(idade)

print(f"Idades coletadas: {idades}")

soma =0

for idade in idades:
    soma += idade
    idade+=1

media = sum(idades) / len (idades)
menor_idade = min(idades)
maior_idade = max(idades)
 

print(f"Média das idades: {media}")
print(f"Menor idade: {menor_idade}")
print(f"Maior idade: {maior_idade}")
