# pessoa_lista = ["João", 23, 1.7] #não serve para agrupar informações distitintas
# pessoa_dicionario = {"nome": "João",
#                      "idade": 23,
#                      "altura": 1.7
#                      }


# #CRUD
# #LER
# print(pessoa_dicionario["nome"])
# print(pessoa_dicionario.get("telefone", "Informação não encontrada"))

# #CRIAR
# pessoa_dicionario["telefone"] = "85986243256"

# #MODIFICAÇÃO
# pessoa_dicionario ["nome"] = "Tarik"

# #REMOVER

# pessoa_dicionario.pop("idade")


#crie um dicionario que representa o produto de um supermercado. Deve conter: nome, preço e estoque.

# Protudo_um= {
#     "produto": "Queijo",
#     "Marca": "Regina",
#     "Preço": 25.50,
#     "Estoque": 125
#     }

# print(Protudo_um)

# ## 2. Crie um dicionário que organiza os contatos telefônicos de alguém. Como chave você deverá utilizar o nome da pessoa e como valor, o telefone da pessoa. 
# # Crie 5 contatos e exiba somente o telefone de um contato chamado "Mario".
# contatos = {
#     "Mario": "99999-1211",
#     "Lucas": "97888-2222",
#     "Marlia": "97557-3333",
#     "Bruna": "96666-4444",
#     "João": "95555-5555"
# }
# print(contatos["Mario"])

#interagindo com aluno

cadastro = 0
listaalunos= []
while True:
    Aluno = input ("Digite seu nome: ")
    CPF = input ("Digite seu CPF - exemplo:05068030317 ")
    Idade= input ("Digite seu idade: ")
    Altura = input ("Digite seu altura: ")
    Genero = input ("Digite seu gênero: ")
   
    CadatroAlunos = {
                "Aluno": Aluno,
                "CPF": CPF,
                "Altura": Altura,
                "Genero": Genero 
        }
   
    listaalunos.append(CadatroAlunos)

    cadastro = input ("Deseja cadastrar um novo aluno?")
    if cadastro == "SIM":
        continue
    else:
        break


print(listaalunos)





