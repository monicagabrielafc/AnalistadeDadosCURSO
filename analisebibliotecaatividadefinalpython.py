
import json

#Carregar dados de um JSON

with open("baseBiblioteca.json","r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

lista_emprestimos = dados["emprestimos"]
print (lista_emprestimos)


#Exibir o nome do usuário
lista_usuario = []
for dados in lista_emprestimos:
    if dados["usuario"] not in lista_usuario:
        lista_usuario.append(dados["usuario"])

print("- Segue lista de usuários em 2024 -")
lista_usuario.sort()
for usuario in lista_usuario:
 print(usuario)
print()
#Exibir o nome dos livros
lista_livros = []
for dados in lista_emprestimos:
    if dados["livro"] not in lista_livros:
        lista_livros.append(dados["livro"])

print(" - Segue lista de Livros emprestados em 2024 - ")
print()
lista_livros.sort()
for livro in lista_livros:
 print(livro)
print (f"Quantidade de livros: {len(lista_livros)}")
print()
print ("O LIVRO MAIS EMPRESTADO FOI")
livro_mais_emprestado = []
quantidade_max = 0

livro_mais_emprestado = ""
quantidade_max = 0
emprestimo_por_livro = {

}
for livro in lista_livros:

    # if livro not in emprestimo_por_livro:
    #      emprestimo_por_livro [livro] = 0

    qtd = 0
    for emprestimo in lista_emprestimos:
        if emprestimo["livro"] == livro:
            qtd += 1
    
    emprestimo_por_livro[livro] = qtd

    
    if qtd > quantidade_max:
        quantidade_max = qtd
        livro_mais_emprestado = livro

print(f"Livro mais emprestado: {livro_mais_emprestado} ({quantidade_max} vezes)")
for livro in emprestimo_por_livro:

    print(f"{livro} - {emprestimo_por_livro[livro]})")



#Livros mais emprestados e Autores mais emprestados


#Contagem por livro

#Gêneros mais populares

#Contagem por genero

#Livros que mais atrasam

#Média de dias_atraso por livro

#Livros com maior valor de multa acumulada

#Soma de multa por livro