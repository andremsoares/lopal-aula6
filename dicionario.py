aluno = {"nome": "Ana", "nota": 8, "cel": "11971759956"}



clientes = [
    {"nome": "Ana", "cel": "11971759956", "empresa":"FIAT"},
    {"nome": "Pedro", "cel": "1199666767", "empresa": "INTEL"},
    {"nome": "Ramon", "cel": "11967676767", "empresa":"SEBRAE"},
    {"nome": "Chico", "cel": "11989765234", "empresa": "INTEL"}
]

# Pesquisa cliente para a empresa

decisao = input("Qual empresa você deseja filtrar os usuários? ")

for cliente in clientes:
    if decisao == cliente["empresa"]:
        print(cliente["nome"])
        
# Cadastrar um novo cliente

print("---> Cadastrando um novo CLIENTE <---")
nome = input("Digite o nome do cliente: ")
celular = input("Digite o celular do cliente: ")
empresa = input("Digite o nome da empresa: ")

novo_cliente = {
    "nome": nome,
    "cel": celular,
    "empresa": empresa
}

clientes.append(novo_cliente)

print (clientes)

# Remover um cliente

print("---> Removendo um cliente pelo nome <---")
print(clientes)
nome_cliente = input("Digite o nome do cliente: ")

for cliente in clientes:
    if cliente["nome"] == nome_cliente:
        clientes.remove(cliente)
        break
    
print(clientes)