lista = ["Pão", "Banana", "Maçã", "Limão", "Queijo", "Presunto", "Refrigerante"]

def mostrar():
    for x in lista:
        print(f"{x}")

def cadastrar():
    item = input("Digite o item que deseja adicionar na lista: ")
    lista.append(item)

def remover():
    item = input("Digite qual item da lista deseja remover: ")
    lista.remove(item)
    
def modificar():
    posicao_item = lista.index(input("Qual item deseja substituir? "))
    lista[posicao_item] = input("Qual item deseja adicionar no lugar? ")

while True:
    print ("LISTA DE COMPRAS")
    print ("1 - Mostrar lista")
    print ("2 - Cadastrar item na lista")
    print ("3 - Excluir item da lista")
    print ("4 - Modificar item da lista")
    print ("0 - Sair")
    
    opcao = input("Escolha sua opção: ")
    
    if opcao == "1":
        mostrar()
    elif opcao == "2":
        cadastrar()
    elif opcao == "3":
        remover()
    elif opcao == "4":
        modificar()
    elif opcao == "0":
        print ("Saindo do sistema...")
        break
    else:
        print ("Opção inválida. Tente novamente.")