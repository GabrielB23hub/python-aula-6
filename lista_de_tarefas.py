# lista de tarefas #
#1 - Mostrar todas tarefas
#2 - Mostrar tarefas concluídas
#3 - Mostrar tarefas pendentes
#4 - Mostrar tarefas por prioridade
#5 - Cadastrar tarefa nova
#6 - Finalizar tarefa
#7 - remover tarefa
#0 - Sair

lista = [
    {"titulo":"estudar", "concluída":"Sim","Prioridade":"Alta"},
    {"titulo":"comer", "concluída":"Sim","Prioridade":"Baixa"},
    {"titulo":"caminhar", "concluída":"Não","Prioridade":"Alta"},
    {"titulo":"louça", "concluída":"Não","Prioridade":"Baixa"}
    ]
    


def tudo():
        for x in lista:
         print(x)

def concluidas():
        feito = "Sim"
        for x in lista:
          if (x["concluída"]) == feito:
           print(x["titulo"])
def pendentes():
        feito = "Não"
        for x in lista:
          if (x["concluída"]) == feito:
           print(x["titulo"])
def prioridade():
        requisito = input("Qual é a prioridade da tarefa? ")
        for x in lista:
          if (x["Prioridade"]) == requisito:
              print(x["titulo"])
def cadastrar():
        nome =  input("Qual o nome/título da tarefa? ")
        concluida = "Não"
        prioridade = input("Qual a prioridade da tarefa? ")
        nova_tarefa = {
            "titulo": nome,
            "concluída": concluida,
            "Prioridade": prioridade
        }
        lista.append(nova_tarefa)
        print (lista)
def finalizar():
        tarefa = input("Qual tarefa deseja deixar como concluída? ")
        for x in lista:
            if x["titulo"] == tarefa:
                x["concluída"] = "Sim"
                break
        else:
            print("Tarefa não encontrada.")
def remover():
        remover = (input("Qual tarefa remover? "))
        for x in lista:
          if x["titulo"] == remover:
               lista.remove (x)
               print("Tarefa removida da lista com sucesso")
               break
while True:
    print ("1 - Mostrar toda as tarefas")
    print ("2 - Mostrar tarefas concluídas")
    print ("3 - Mostrar tarefas pendentes")
    print ("4 - Mostrar tarefas por prioridade")
    print ("5 - Cadastrar tarefa nova")
    print ("6 - Finalizar tarefa")
    print ("7 - Remover tarefa")
    print ("0 Sair")

    opcao = input ("Escolha uma opção: ")
    
    if opcao == "1":
        tudo()
    elif opcao == "2":
        concluidas()
    elif opcao == "3":
        pendentes()
    elif opcao == "4":
        prioridade()
    elif opcao == "5":
        cadastrar()
    elif opcao == "6":
        finalizar()
    elif opcao == "7":
         remover()
    elif opcao == "0":
        print("Saindo...")
        break
    else:
            print("Opção inválida. Tente novamente.")