# INÍCIO
print("\nSTUDYFY")
print("Onde todo o estudante tem espaço para aprender!")
input("\nPressione ENTER para continuar...")  

# LISTA PARA GUARDAR TAREFAS
tarefas = []

# FUNÇÕES DE CONTA
def fazer_login():
    print("\n--- LOGIN ---")
    input("Nome de Usuário: ")
    input("Senha: ")
    print("Entrando...")
    input("\nPressione ENTER para continuar...")  

def criar_conta():
    print("\n--- CRIAR CONTA ---")
    input("Nome Completo: ")
    input("E-mail Institucional: ")
    input("CPF: ")
    input("Nome de Usuário: ")
    input("Criar Senha: ")
    print("Conta criada com sucesso!")
    input("\nPressione ENTER para continuar...") 

# Verificar se usuário tem conta
resposta = input("\nVocê já possui conta? S/N: ").upper()

if resposta == "S":
    fazer_login()
else:
    criar_conta()

# MENU
while True:
    print("\n--- MENU ---")
    print("1. Cadastrar tarefa")
    print("2. Listar tarefas")
    print("3. Ver tarefas urgentes")
    print("4. Marcar tarefa como concluída")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    # SAIR
    if opcao == "5":
        print("Saindo...")
        break

    # CADASTRAR TAREFA
    elif opcao == "1":
        print("\n--- CADASTRAR TAREFA ---")
        nome = input("Nome da tarefa: ")
        urgente = input("É urgente? (s/n): ").lower()

        tarefa = {
            "nome": nome,
            "urgente": urgente == "s",
            "concluida": False
        }

        tarefas.append(tarefa)
        print("Tarefa cadastrada com sucesso!")
        input("\nPressione ENTER para continuar...")  

    # LISTAR TODAS
    elif opcao == "2":
        print("\n--- LISTAR TAREFAS ---")
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            for i, tarefa in enumerate(tarefas, 1):
                status = "✓" if tarefa["concluida"] else " "
                urgente_texto = "[URGENTE]" if tarefa["urgente"] else ""
                print(f"{i}. [{status}] {tarefa['nome']} {urgente_texto}")
        input("\nPressione ENTER para continuar...")  

    # VER URGENTES
    elif opcao == "3":
        print("\n--- Tarefas urgentes ---")
        urgentes = [t for t in tarefas if t["urgente"] and not t["concluida"]]
        if len(urgentes) == 0:
            print("Nenhuma tarefa urgente pendente")
        else:
            for i, tarefa in enumerate(urgentes, 1):
                print(f"{i}. {tarefa['nome']}")
        input("\nPressione ENTER para continuar...")  

    # MARCAR COMO CONCLUÍDA
    elif opcao == "4":
        print("\n--- Marcar tarefa como concluída ---")
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            pendentes = [t for t in tarefas if not t["concluida"]]
            
            if len(pendentes) == 0:
                print("Todas as tarefas já estão concluídas!")
            else:
                for i, tarefa in enumerate(pendentes, 1):
                    print(f"{i}. {tarefa['nome']}")
                
                try:
                    escolha = int(input("\nQual tarefa concluir? (número): "))
                    if 1 <= escolha <= len(pendentes):
                        pendentes[escolha-1]["concluida"] = True
                        print("Tarefa marcada como concluída!")
                    else:
                        print("Número inválido, tente novamente!")
                except ValueError:
                    print("Digite um número válido, tente novamente!")
        input("\nPressione ENTER para continuar...") 

    # OPÇÃO INVÁLIDA
    else:
        print("Opção inválida, tente novamente!")
        input("\nPressione ENTER para continuar...")