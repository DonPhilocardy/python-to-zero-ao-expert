import sys

Lista = []

MENU = """Escolha uma das 5 opções abaixo:
1: Adicionar um elemento à lista
2: Remover um elemento da lista
3: Mostrar a lista
4: Limpar a lista
5: Sair
👉 Sua escolha: """

MENU_CHOICES = ["1", "2", "3", "4", "5"]

while True:
    user_choice = ""
    while user_choice not in MENU_CHOICES:
        user_choice = input(MENU)
        if user_choice not in MENU_CHOICES:
            print("Por favor, escolha uma opção válida...")


    if user_choice == "1":  # Adicionar um elemento
        item = input("Digite o nome do elemento a ser adicionado à lista de compras: ")
        Lista.append(item)
        print(f"O elemento {item} foi adicionado à lista com sucesso.")
    elif user_choice == "2":  # Remover um elemento
        item = input("Digite o nome do elemento a ser removido da lista de compras: ")
        if item in Lista:
            Lista.remove(item)
            print(f"O elemento {item} foi removido da lista com sucesso.")
        else:
            print(f"O elemento {item} não está na lista.")
    elif user_choice == "3":  # Mostrar a lista
        if Lista:
            print("Aqui está o conteúdo da sua lista:")
            for i, item in enumerate(Lista, 1):
                print(f"{i}. {item}")
        else:
            print("Sua lista não contém nenhum elemento.")
    elif user_choice == "4":  # Limpar a lista
        Lista.clear()
        print("A lista foi esvaziada com sucesso.")
    elif user_choice == "5":  # Sair
        print("Até logo!")
        sys.exit()

    print("-" * 50)