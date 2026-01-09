
import json

#Carregar dados de um JSON

with open("baseBiblioteca.json","r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

lista_emprestimos = dados["emprestimos"]
print (lista_emprestimos)