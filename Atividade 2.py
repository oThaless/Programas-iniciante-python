import os

def limpar_tela():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def exibir_menu ():
    print ("================================") 
    print ("SISTEMA DE USUARIOS")
    print ("================================")
    print ("1 - Cadastrar Usuario")  
    print ("2 – Listar Usuarios")
    print ("9 - Sair")
    print ("================================")

def cadastrar_usuario ():
    nome = input("Qual o nome do usuario? ")
    arquivo = open("nome.txt", "a")
    arquivo.write(nome + "\n")
    arquivo.close()
    resposta = input("Deseja cadastrar outro usuario? (S/N) ").upper()
    if resposta == "S":
        cadastrar_usuario()
    if resposta == "N":
        print("Cadastro finalizado")
    elif resposta != "S" and resposta != "N":
        print("Opção invalida. Tente novamente")
        cadastrar_usuario()

def listar_usuarios():
    arquivo = open("nome.txt", "r")
    conteudo = arquivo.read()
    arquivo.close()
    if not conteudo:
        print("Não há nenhum usuario cadastrado")
    else: 
        print("Lista de usuarios cadastrada")
        print(conteudo)

def main():
    usuarios = []

    while True:
        limpar_tela()
        exibir_menu()

        opcao = input("Escolha uma opção: ")
        limpar_tela()

        if opcao == "1":
            cadastrar_usuario()
            input("Pressione Enter para voltar ao menu...")

        elif opcao == "2":
            listar_usuarios()
            input("Pressione Enter para voltar ao menu...")

        elif opcao == "9":
            print("Encerrando programa.")
            break
        else:
            print("Opção invalida. Tente novamente")
            input("Pressione Enter para voltar ao menu...")

main()