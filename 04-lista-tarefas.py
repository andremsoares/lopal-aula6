# LISTA DE TAREFAS

# 1 - Mostrar todas tarefas
# 2 - Mostrar tarefas concluídas
# 3 - Mostrar tarefas pendentes
# 4 - Mostrar tarefas por prioridade
# 5 - Cadastrar tarefa nova
# 6 - Finalizar tarefa
# 7 - Remover tarefa
# 0 - Sair do sistema

tarefas = [
    {"titulo": "Estudar", "concluida": "Sim", "prioridade": "Alta"},
    {"titulo": "Ler", "concluida": "Não", "prioridade": "Baixa"},
    {"titulo": "Jogar videogame", "concluida": "Não", "prioridade": "Baixa"},
    {"titulo": "Ir à academia", "concluida": "Não", "prioridade": "Alta"},
    {"titulo": "Lavar louça", "concluida": "Sim", "prioridade": "Baixa"}
]

def mostrar():
    for tarefa in tarefas:
        if tarefa["concluida"] == "Sim":
            condicao = "X"
        else:
            tarefa["concluida"] == "Não"
            condicao = " "
        print(f"{tarefa["titulo"]} [{condicao}] {tarefa["prioridade"]}")

def mostrar_concluidas():
    for tarefa in tarefas:
        if tarefa["concluida"] == "Sim":
            condicao = "X"
            print(f"{tarefa["titulo"]} [{condicao}] {tarefa["prioridade"]}")
            
def mostrar_pendentes():
    for tarefa in tarefas:
        if tarefa["concluida"] == "Não":
            condicao = " "
            print(f"{tarefa["titulo"]} [{condicao}] {tarefa["prioridade"]}")
            
def mostrar_prioridades():
    opcao = input("Você deseja ver as tarefas de prioridade alta ou baixa? ").capitalize()
    for tarefa in tarefas:
        if opcao == tarefa["prioridade"]:
            if tarefa["concluida"] == "Sim":
                condicao = "X"
            else:
                tarefa["concluida"] == "Não"
                condicao = " "
            if tarefa["concluida"]:
                print(f"{tarefa["titulo"]} [{condicao}] {tarefa["prioridade"]}")
                
    
def cadastrar():
    titulo = input("Digite o nome da nova tarefa: ").capitalize()
    prioridade = input("A prioridade da tarefa é alta ou baixa? ").capitalize()
    nova_tarefa = {
        "titulo": titulo,
        "concluida": "Não",
        "prioridade": prioridade
    }
    tarefas.append(nova_tarefa)
    print("A tarefa foi adicionada!")
    
def finalizar():
    finalizar = input("Qual tarefa você deseja finalizar? ")
    for tarefa in tarefas:
        if tarefa ["titulo"] == finalizar:
            tarefa ["concluida"] = "Sim"
    print("Sua tarefa foi finalizada!")
    
def remover():
    remover = input("Qual tarefa você deseja remover? ")
    for tarefa in tarefas:
        if tarefa["titulo"] == remover:
            tarefas.remove(tarefa)
    print("Sua tarefa foi removida.")
    
while True:
    print("LISTA DE TAREFAS")
    print("1 - Mostrar todas tarefas")
    print("2 - Mostrar tarefas concluídas")
    print("3 - Mostrar tarefas pendentes")
    print("4 - Mostrar tarefas por prioridade")
    print("5 - Cadastrar tarefa nova")
    print("6 - Finalizar tarefa")
    print("7 - Remover tarefa")
    print("0 - Sair")
    
    opcao = input("Escolha sua opção: ")
    
    if opcao == "1":
        mostrar()
    elif opcao == "2":
        mostrar_concluidas()
    elif opcao == "3":
        mostrar_pendentes()
    elif opcao == "4":
        mostrar_prioridades()
    elif opcao == "5":
        cadastrar()
    elif opcao == "6":
        finalizar()
    elif opcao == "7":
        remover()
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opcão inválida. Tente novamente.")