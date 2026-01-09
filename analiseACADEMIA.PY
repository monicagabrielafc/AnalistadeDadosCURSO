import json

#Carregar dados de um JSON

with open("baseAcademia.json","r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

lista_alunos = dados["alunos"]
print (lista_alunos)
# 1. Exibir a lista de alunos contendo Nome | Mensalidade R$ | Tipo de Plano | Frequência

print("LISTA DE ALUNOS")
print("Nome | Mensalidade R$ | Tipo de Plano | Frequência")

for dados in lista_alunos:
    print(f"{dados['nome']} | {dados['mensalidade']} | {dados['plano']}| {dados['frequencia_mensal']}")

# 2. Exibir total de mensalidade por mês da academia
total_receita = 0
for dados in lista_alunos:
     total_receita += dados["mensalidade"] 
print(f"Receita total mensal: R$ {total_receita:2f}")


# 3. Exibir a média de idade dos alunos da academia

# 4. Frequência total por tipo de plano da academia