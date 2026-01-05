
# Crie um programa que apresente um menu contendo 3 charadas e uma opção para sair.
acerto1 = False
acerto2 = False
acerto3 = False
while True:

    print("CHARADAS")
    print("Escolha uma opção abaixo:")
    print("Charada 1")
    print("Charada 2")
    print("Charada 3")
    print("Sair    0")

# o usuário deve escolher uma das opções de charadas
    opcao = input("escolha uma das opções de charada:")
    if opcao == "0":
        print ("estamos saindo do jogo") 
        break
# Exibir o texto da charada escolhida.
    elif opcao == "1":
        print ("é surdo e mudo  e conta tudo:")
        print (input(" qual sua resposta?"))
        palpite = ""
        if palpite == "Livro":
            print ("Você acertou!")
            acerto1 = True
        else: 
            print ("você errou!")
    elif opcao == "2":
        print ("cai em pé e corre deitado")
        print (input(" qual sua resposta?"))
        palpite = ""
        if palpite == "Chuva":
            print ("Você acertou!")
            acerto2 = True
        else: 
            print ("você errou!")
    elif opcao == "3":
        print ("o que é um ponto preto no açucar")
        print (input(" qual sua resposta?"))
        palpite = ""
        if palpite == "Formiga":
            print ("Você acertou!")
            acerto3 = True
        else: 
            print ("você errou!")
    else:
        print("digite uma opção válida")

if acerto1 == True and acerto2 == True and acerto3 == True:
    print ("VOCÊ É FUEDAAAAAAAAA")



