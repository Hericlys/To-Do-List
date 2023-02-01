from os import system
from time import sleep
from getpass import getpass

tasks = []


def add_task(task):
    tasks.append(task)
    print(f"A tarefa '{task}' foi adcionada à lista.")


def edit_task(index, task):
    tasks[index] = task
    print(f"A tarefa na posição {index} doi editada para '{task}'.")


def delete_task(index):
    task = tasks.pop(index)
    print("A tarefa '{task}' foi excluída da lista.")


def view_tasks(confirmation=True):
    print("Lista de Tarefas: ")
    for i, task in enumerate(tasks):
        print(f"{i}: {task}")
    if confirmation:
        getpass('Precione enter para sair')



def check_int(msg):
    # verifica o o valor fornecido é um numero inteiro.
    while True:
        try:
            r = int(input(msg))
        except ValueError:
            print("O valor fornecido nao é um numero inteiro, tente novamente.")
            continue
        break
    return r


def main():
    while True:
        sleep(2)
        system("cls")
        print("""
        ==============================================
        1. Adicionar Tarefa
        2. Editar Tarefa
        3. Excluir Tarefa
        4. Ver Tarefas
        0. Sair
        ==============================================
        """)

        msg = "Selecione uma opção: "
        option = check_int(msg)
        if option == 0:
            break
        elif option == 1:
            task = input("Digite a nova tarefa: ")
            add_task(task)
        elif option == 2:
            view_tasks()
            index = int(input("Selecione a tarefa a ser editada: "))
            task = input("Digite a nova descrição: ")
            edit_task(index, task)
        elif option == 3:
            view_tasks(False)
            index = int(input("Selecione a tarefa a ser excluída: "))
            delete_task(index)
        elif option == 4:
            view_tasks()
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
