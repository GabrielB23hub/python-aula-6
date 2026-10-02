clientes = [
    {"nome":"Pedro","cel":"192356", "empresa":"Monster"},
    {"nome":"Mateus","cel":"938388", "empresa":"redbull"},
    {"nome":"Gabriel","cel":"556656", "empresa":"fiat"},
    {"nome":"beti","cel":"293856", "empresa":"Monster"}
]

def lista():
    empresa_digitada = input ("Digite o nome da empresa: " )
    for cliente in clientes:
        if cliente ["empresa"] == empresa_digitada:
            print( cliente)

#Cadastrar cliente
def cadastrar():
    print ("---> Cadastrando um novo CLIENTE<---")
    nome = input ("Digite o nome do Cliente: ")
    celular = input ("Digite o número de celular do Cliente: ")
    empresa = input ("Digite a empresa do Cliente: ")


    novo_cliente = {
        "nome": nome,
        "cel": celular,
        "empresa": empresa
    }   
    clientes.append(novo_cliente)
    print (clientes)

# remover um cliente
def remover():
    print("---> Removendo um Cliente pelo Nome")
    nome_cliente = input ("Digite o nome do Cliente para remover: ")
    for cliente in clientes:
         if cliente["nome"] == nome_cliente:
             clientes.remove (cliente)
             break

print (clientes)
while True:
    print ("1 - Procurar na lista")
    print ("2 - Cadastrar")
    print ("3 - remover")

    opcao = input ("O que deseja fazer? ")

    if opcao == "1":
            lista()
    elif opcao == "2":
         cadastrar()
    elif opcao == "3":
         remover()
    elif opcao == "0":
         print("Saindo do Sistema...")
         break
    else:
            print("Opção inválida. Tente novamente")