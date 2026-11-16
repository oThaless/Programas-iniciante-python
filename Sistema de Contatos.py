import os

def limpar_tela():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def exibir_menu ():
    print ("================================") 
    print ("SISTEMA DE CONTATOS")
    print ("================================")
    print ("1 - Cadastrar Contato")  
    print ("2 – Listar Contatos")
    print ("9 - Sair")
    print ("================================")

def cadastrar_contato ():
    nome = input("Qual seu nome? ")
    numero = input("Qual seu numero? ")
    contatos = open("contatos.txt", "a")
    contatos.write(nome + " - " + numero + "\n")
    contatos.close()
    resposta = input("Deseja cadastrar outro contato? (S/N) ").upper()
    if resposta == "S":
        cadastrar_contato()
    if resposta == "N":
        print("Cadastro finalizado")
    elif resposta != "S" and resposta != "N":
        print("Opção invalida. Tente novamente")
        cadastrar_contato()

def listar_contatos():
    arquivo = open("contatos.txt", "r")
    conteudo = arquivo.read()
    arquivo.close()
    if not conteudo:
        print("Não há nenhum contato cadastrado")
    else: 
        print("Lista de contatos cadastrados")
        print(conteudo)

def main():
    contatos = []

    while True:
        limpar_tela()
        exibir_menu()

        opcao = input("Escolha uma opção: ")
        limpar_tela()

        if opcao == "1":
            cadastrar_contato()
            input("Pressione Enter para voltar ao menu...")

        elif opcao == "2":
            listar_contatos()
            input("Pressione Enter para voltar ao menu...")

        elif opcao == "9":
            print("Encerrando programa.")
            break
        else:
            print("Opção invalida. Tente novamente")
            input("Pressione Enter para voltar ao menu...")

main()
