from sys import exit

id_clientes = [1, 2]
clientes = [
    ["Bruno Rodrigues"],
    ["Emiliano Rigoni"],
]

id_produtos = [1, 2, 3]
produtos = [
    ["SSD 240 GB", "Kingston", 250.00],
    ["Mouse Gamer", "Razer", 300.00],
    ["Notebook Vostro", "Dell", 7500.00]
]

id_vendas = []
vendas = []

idx = 0
line = []


class Colors:
    green = "\033[0;32m"
    red = "\033[0;31m"
    red_bold = "\033[1;31m"
    white = "\033[0;97m"
    white_bold = "\033[1;97m"
    yellow = "\033[0;33m"
    close = "\033[m"


class Cliente:
    id_cliente = None
    nome_cliente = None

    def new_cliente(cliente):
        line = []
        print()
        cliente.id_cliente = len(clientes)+1
        print("ID Cliente: {}".format(cliente.id_cliente))
        cliente.nome_cliente = str(input("Insira o nome do cliente: "))
        print()

        id_clientes.append(cliente.id_cliente)
        line.append(cliente.nome_cliente)
        clientes.append(line)

        print("{}Cliente cadastrado com sucesso ✓{}".format(
            Colors.green, Colors.close))
        print()

    def search_cliente(cliente):
        global idx
        pesq = int(input("Informe o ID do cliente a ser consultado: "))

        if pesq in id_clientes:
            idx = id_clientes.index(pesq)
            print()
            print("Tabela de Clientes - Resultados da Pesquisa")
            print(" {:<5} {:<15}".format('ID', 'Nome Cliente'))
            print(" {:<5} {:<15}".format(id_clientes[idx], clientes[idx][0]))
            print()
        else:
            print()
            print("{}Nenhum Cliente com o ID {} foi encontrado X{}".format(
                Colors.red, pesq, Colors.close))
            print()

    def display_cliente(cliente):
        print()
        print("Tabela de Clientes")
        print(" {:<5} {:<15}".format('ID', 'Nome Cliente'))
        for x in range(0, len(clientes)):
            print(" {:<5} {:<15}".format(id_clientes[x], clientes[x][0]))
        print()


class Produto:
    id_prod = None
    descr_prod = None
    fabricante_prod = None
    valor_unit_prod = None

    def new_produto(produto):
        line = []
        print()
        produto.id_prod = len(produtos)+1
        print("ID Produto: {}".format(produto.id_prod))
        produto.descr_prod = str(
            input("Informe uma descrição para este produto: "))
        produto.fabricante_prod = str(input("Informe a fabricante: "))
        produto.valor_unit_prod = float(input("Informe o valor unitário: "))
        print()

        id_produtos.append(produto.id_prod)
        line.append(produto.descr_prod)
        line.append(produto.fabricante_prod)
        line.append(produto.valor_unit_prod)
        produtos.append(line)

        print("{}Produto cadastrado com sucesso ✓{}".format(
            Colors.green, Colors.close))
        print()

    def search_produto(produto):
        global idx
        pesq = int(input("Informe o ID do produto a ser consultado: "))

        if pesq in id_produtos:
            idx = id_produtos.index(pesq)
            print()
            print("Tabela de Produtos - Resultados da Pesquisa")
            print(" {:<5} {:<15} {:<15} {:<15}".format(
                'ID', 'Descrição', 'Fabricante', 'Valor Unitário'))
            print(" {:<5} {:<15} {:<15} {:<15}".format(
                id_produtos[idx], produtos[idx][0], produtos[idx][1], produtos[idx][2]))
            print()
        else:
            print()
            print("{}Nenhum Produto com o ID {} foi encontrado X{}".format(
                Colors.red, pesq, Colors.close))
            print()

    def display_produto(produto):
        print()
        print("Tabela de Produtos")
        print(" {:<5} {:<15} {:<15} {:<15}".format(
            'ID', 'Descrição', 'Fabricante', 'Valor Unitário'))
        for x in range(0, len(produtos)):
            print(" {:<5} {:<15} {:<15} {:<15}".format(
                id_produtos[x], produtos[x][0], produtos[x][1], produtos[x][2]))
        print()


class Venda:
    idx = 0
    id_venda = None
    id_prod = None
    id_cliente = None
    nome_cliente = None
    descr_prod = None
    fabricante_prod = None
    valor_unit_prod = None
    qtde_prod = None
    valor_final = None

    def new_venda(venda):
        global idx
        line = []
        print()
        venda.id_venda = len(vendas)+1
        print("ID Venda: {}".format(venda.id_venda))

        def searchC():
            venda.id_cliente = int(input("Informe o ID do cliente: "))
            if venda.id_cliente in id_clientes:
                idx = id_clientes.index(venda.id_cliente)
                venda.nome_cliente = clientes[idx][0]
            else:
                print("Cliente não encontrado.")
                searchC()
        searchC()

        def searchP():
            venda.id_prod = int(input("Informe o ID do produto: "))
            if venda.id_prod in id_produtos:
                idx = id_produtos.index(venda.id_prod)
                venda.descr_prod = produtos[idx][0]
            else:
                print("Cliente não encontrado.")
                searchP()
        searchP()

        if venda.fabricante_prod in produtos:
            idx = produtos.index(venda.fabricante_prod)
        venda.fabricante_prod = produtos[idx][1]

        venda.qtde_prod = int(input("Informe a quantidade: "))

        if venda.valor_unit_prod in produtos:
            idx = produtos.index(venda.valor_unit_prod)
        venda.valor_unit_prod = produtos[idx][2]
        total = float(venda.qtde_prod * venda.valor_unit_prod)
        venda.valor_final = total
        print()

        id_vendas.append(venda.id_venda)
        line.append(venda.id_cliente)
        line.append(venda.nome_cliente)
        line.append(venda.id_prod)
        line.append(venda.descr_prod)
        line.append(venda.fabricante_prod)
        line.append(venda.qtde_prod)
        line.append(venda.valor_unit_prod)
        line.append(venda.valor_final)
        vendas.append(line)

        print("{}Venda cadastrada com sucesso ✓{}".format(
            Colors.green, Colors.close))
        print()

    def search_venda(venda):
        global idx
        pesq = int(input("Informe o ID da venda a ser consultada: "))

        if pesq in id_vendas:
            idx = id_vendas.index(pesq)
            print()
            print("Tabela de Vendas -  Resultados da Pesquisa")
            print(" {:<10} {:<15} {:<20} {:<10} {:<20} {:<20} {:<10} {:<15} {:<15}".format(
                'ID Venda', 'ID Cliente', 'Nome Cliente', 'ID Prod', 'Descrição', 'Fabricante', 'Qtde', 'Valor Unitário', 'Valor Final'))
            print(" {:<10} {:<15} {:<20} {:<10} {:<20} {:<20} {:<10} {:<15} {:<15}".format(
                id_vendas[idx], vendas[idx][0], vendas[idx][1], vendas[idx][2], vendas[idx][3], vendas[idx][4], vendas[idx][5], vendas[idx][6], vendas[idx][7]))
            print()
        else:
            print()
            print("{}Nenhuma Venda com o ID {} foi encontrado X{}".format(
                Colors.red, pesq, Colors.close))
            print()

    def display_venda(venda):
        print()
        print("Tabela de Vendas")
        print(" {:<10} {:<15} {:<20} {:<10} {:<20} {:<20} {:<10} {:<15} {:<15}".format(
            'ID Venda', 'ID Cliente', 'Nome Cliente', 'ID Prod', 'Descrição', 'Fabricante', 'Qtde', 'Valor Unitário', 'Valor Final'))
        for x in range(0, len(vendas)):
            print(" {:<10} {:<15} {:<20} {:<10} {:<20} {:<20} {:<10} {:<15} {:<15}".format(
                id_vendas[x], vendas[x][0], vendas[x][1], vendas[x][2], vendas[x][3], vendas[x][4], vendas[x][5], vendas[x][6], vendas[x][7]))
        print()


def menu_options():
    print()
    print("-"*15, "MENU", "-"*15)
    print("▼ Clientes")
    print(" 1 - Cadastrar Cliente")
    print(" 2 - Listar Clientes")
    print(" 3 - Consultar Clientes")
    print()
    print("▼ Produtos")
    print(" 4 - Cadastrar Produtos")
    print(" 5 - Listar Produtos")
    print(" 6 - Consultar Produtos")
    print()
    print("▼ Vendas")
    print(" 7 - Cadastrar Venda")
    print(" 8 - Listar Vendas")
    print(" 9 - Consultar Vendas")
    print()
    print("▼ Outras Opções")
    print(" 10 - SAIR")
    print()
    # print("➦")
    register_menu()


def register_menu():
    option = int(input("Informe o que deseja fazer: "))

    # Cadastrar Clientes
    if (option == 1):
        cliente = Cliente()
        cliente.new_cliente()

        running = True
        while running:
            resp = str(input("Deseja cadastrar outro Cliente?: "))
            resp = resp.upper()

            if (resp == "N") or (resp == "NAO") or (resp == "NÃO"):
                running = False
                menu_options()

            elif (resp == "S") or (resp == "SIM"):
                cliente.new_cliente()
            else:
                print("Informe uma opção válida.")
                menu_options()

    # Listar Clientes
    elif (option == 2):
        cliente = Cliente()
        cliente.display_cliente()
        menu_options()

    # Consultar Clientes
    elif (option == 3):
        cliente = Cliente()
        cliente.search_cliente()

        running = True
        while running:
            resp = str(input("Deseja consultar outro Cliente?: "))
            resp = resp.upper()

            if (resp == "N") or (resp == "NAO") or (resp == "NÃO"):
                running = False
                menu_options()

            elif (resp == "S") or (resp == "SIM"):
                cliente.search_cliente()
            else:
                print("Informe uma opção válida.")
                menu_options()

    # Cadastrar Produtos
    elif (option == 4):
        produto = Produto()
        produto.new_produto()

        running = True
        while running:
            resp = str(input("Deseja cadastrar outro Produto?: "))
            resp = resp.upper()

            if (resp == "N") or (resp == "NAO") or (resp == "NÃO"):
                running = False
                menu_options()
            elif (resp == "S") or (resp == "SIM"):
                produto.new_produto()
            else:
                print("Informe uma opção válida.")
                menu_options()

    # Listar Produtos
    elif (option == 5):
        produto = Produto()
        produto.display_produto()
        menu_options()

    # Consultar Produtos
    elif (option == 6):
        produto = Produto()
        produto.search_produto()

        running = True
        while running:
            resp = str(input("Deseja consultar outro Produto?: "))
            resp = resp.upper()

            if (resp == "N") or (resp == "NAO") or (resp == "NÃO"):
                running = False
                menu_options()
            elif (resp == "S") or (resp == "SIM"):
                produto.search_produto()
            else:
                print("Informe uma opção válida.")
                menu_options()

    # Cadastrar Vendas
    elif (option == 7):
        venda = Venda()
        venda.new_venda()

        running = True
        while running:
            resp = str(input("Deseja cadastrar outra Venda?: "))
            resp = resp.upper()

            if (resp == "N") or (resp == "NAO") or (resp == "NÃO"):
                running = False
                menu_options()
            elif (resp == "S") or (resp == "SIM"):
                venda.new_venda()
            else:
                print("Informe uma opção válida.")
                menu_options()

    # Listar Vendas
    elif (option == 8):
        venda = Venda()
        venda.display_venda()
        menu_options()

    # Consultar Vendas
    elif (option == 9):
        venda = Venda()
        venda.search_venda()

        running = True
        while running:
            resp = str(input("Deseja consultar outra Venda?: "))
            resp = resp.upper()

            if (resp == "N") or (resp == "NAO") or (resp == "NÃO"):
                running = False
                menu_options()
            elif (resp == "S") or (resp == "SIM"):
                venda.search_venda()
            else:
                print("Informe uma opção válida.")
                menu_options()

   # Sair
    elif (option == 10):
        exit()

    # opção inválida
    else:
        print("Informe uma opção válida.")
        menu_options()


# inicio
menu_options()
