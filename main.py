produtos = []

def cadastrar_produto():
    print("\n--- CADASTRAR PRODUTO ---")
    nome = input("Nome da roupa: ")
    codigo = input("Código do produto: ")
    categoria = input("Categoria: ")
    preco = float(input("Preço: R$ "))
    quantidade = int(input("Quantidade em estoque: "))

    produto = {
        "nome": nome,
        "codigo": codigo,
        "categoria": categoria,
        "preco": preco,
        "quantidade": quantidade
    }

    produtos.append(produto)
    print("Produto cadastrado com sucesso!")


def listar_produtos():
    print("\n--- LISTA DE PRODUTOS ---")

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
    else:
        for produto in produtos:
            print("-------------------------")
            print("Nome:", produto["nome"])
            print("Código:", produto["codigo"])
            print("Categoria:", produto["categoria"])
            print(f"Preço: R$ {produto['preco']:.2f}")
            print("Estoque:", produto["quantidade"])


def pesquisar_produto():
    print("\n--- PESQUISAR PRODUTO ---")
    pesquisa = input("Digite o nome ou código: ").lower()
    encontrado = False

    for produto in produtos:
        if (pesquisa in produto["nome"].lower()
                or pesquisa == produto["codigo"].lower()):
            print("Produto:", produto["nome"])
            print("Código:", produto["codigo"])
            print(f"Preço: R$ {produto['preco']:.2f}")
            print("Estoque:", produto["quantidade"])
            encontrado = True

    if not encontrado:
        print("Produto não encontrado.")


def registrar_venda():
    print("\n--- REGISTRAR VENDA ---")
    codigo = input("Código do produto: ")

    for produto in produtos:
        if produto["codigo"].lower() == codigo.lower():
            quantidade = int(input("Quantidade vendida: "))

            if quantidade <= 0:
                print("Quantidade inválida.")
            elif quantidade <= produto["quantidade"]:
                produto["quantidade"] -= quantidade
                total = quantidade * produto["preco"]

                print(f"Venda realizada! Total: R$ {total:.2f}")
                print("Estoque atualizado.")
            else:
                print("Estoque insuficiente.")
            return

    print("Produto não encontrado.")


def menu():
    while True:
        print("\n===== LOJA DE ROUPAS =====")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Pesquisar produto")
        print("4 - Registrar venda")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            pesquisar_produto()
        elif opcao == "4":
            registrar_venda()
        elif opcao == "5":
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()