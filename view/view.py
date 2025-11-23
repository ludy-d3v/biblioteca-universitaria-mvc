# view/view.py
def input_text(prompt: str):
    return input(prompt).strip()

def input_int(prompt: str, allow_empty=False):
    while True:
        s = input(prompt).strip()
        if allow_empty and s == "":
            return None
        try:
            return int(s)
        except ValueError:
            print("\nEntrada inválida. Digite um número inteiro.")

def mostrar_mensagem(texto: str):
    print("\n" + texto)

def mostrar_lista_autores(autores):
    print("\n=== Lista de Autores ===")
    if not autores:
        print("\nNenhum autor cadastrado.")
        return
    # autores como tuplas id, nome, nacionalidade
    for a in autores:
        print(f"ID: {a[0]} | Nome: {a[1]} | Nacionalidade: {a[2]}")

def mostrar_lista_livros(livros):
    print("\n=== Lista de Livros ===\n")
    if not livros:
        print("\nNenhum livro cadastrado.")
        return
    # livros retornados pelo modelo select l.id, l.titulo, l.ano_publicacao, a.nome AS nome_autor
    for l in livros:
        # l[0]=id, l[1]=titulo, l[2]=ano_publicacao, l[3]=nome_autor
        autor = l[3] if l[3] else "— Autor não encontrado —"
        print(f"ID: {l[0]} | Título: {l[1]} | Ano: {l[2]} | Autor: {autor}")

def menu_principal():
    print("\n===== Menu Principal =====\n")
    print("1 - Gerenciar autor")
    print("2 - Gerenciar livro")
    print("3 - Sair")
    return input("\nEscolha uma opção: ").strip()

def menu_autor():
    print("\n--- Gerenciar Autor ---\n")
    print("1 - Cadastrar autor")
    print("2 - Listar autores")
    print("3 - Atualizar autor")
    print("4 - Excluir autor")
    print("5 - Voltar ao menu principal")
    return input("\nEscolha uma opção: ").strip()

def menu_livro():
    print("\n--- Gerenciar Livro ---\n")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Atualizar livro")
    print("4 - Excluir livro")
    print("5 - Voltar ao menu principal")
    return input("\nEscolha uma opção: ").strip()

def pausar():
    input("\nPressione Enter para continuar...")
