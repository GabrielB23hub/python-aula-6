#1 mostrar lista
#2 cadastrar item na lista
#3 excluir item da lista
#4 modificar
#5 saída

lista = ["pão","leite","ovos","café","arroz"]

def mostrar():
    print(lista)
    
def cadastrar():
     lista.append((input("O que deseja adicionar? ")))
     print("Item adicionado com sucesso")  

def excluir():
    lista.remove(input("O que deseja remover da lista? "))
    print("Item removido com sucesso!!") 

def modificar():
    item = input("Qual item deseja alterar? ")
    item2 = lista.index(item)
    lista[item2] = input("O que deseja adicionar no lugar do outro item? ")
    print("Item alterado!")
     
while True:
    print ("1 - Mostrar lista")
    print ("2 - Cadastrar item na lista")
    print ("3 - Excluir item da lista")
    print ("4 - Modificar")
    print ("5 - Saída")

    opcao = input ("Escolha uma opção: ")
    
    if opcao == "1":
            mostrar()
    elif opcao == "2":
        cadastrar()
    elif opcao == "3":
        excluir()
    elif opcao == "4":
        modificar()
    elif opcao == "5":
        print ("Saindo do sistema...")
        break
    else:
            print("Opção inválida. Tente novamente.")