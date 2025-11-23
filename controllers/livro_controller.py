# controllers/livro_controller.py
from models.livro_model import LivroModel
from models.autor_model import AutorModel

class LivroController:
    def __init__(self):
        self.model = LivroModel()
        self.autor_model = AutorModel()

    def cadastrar_livro(self, view):
        titulo = view.input_text("Título do livro: ")
        ano = view.input_int("Ano de publicação: ")
        autores = self.autor_model.listar_autores()
        if not autores:
            view.mostrar_mensagem("Nenhum autor cadastrado. Cadastre um autor antes de criar um livro.")
            return
        view.mostrar_lista_autores(autores)
        autor_id = view.input_int("ID do autor (escolha da lista acima): ")
        # verifica existência
        existe = False
        for a in autores:
            if a[0] == autor_id:
                existe = True
                break
        if not existe:
            view.mostrar_mensagem("Autor inválido.")
            return
        try:
            self.model.inserir_livro(titulo, ano, autor_id)
            view.mostrar_mensagem("Livro cadastrado com sucesso.")
        except Exception as e:
            view.mostrar_mensagem(f"Erro ao cadastrar livro: {e}")

    def listar_livros(self, view):
        livros = self.model.listar_livros()
        view.mostrar_lista_livros(livros)

    def atualizar_livro(self, view):
        id_livro = view.input_int("ID do livro a atualizar: ")
        if id_livro is None:
            return

        l = self.model.obter_por_id(id_livro)
        if not l:
            view.mostrar_mensagem("Livro não encontrado.")
            return

        titulo_atual = l[1]
        ano_atual = l[2]
        autor_atual = l[3]

        view.mostrar_mensagem(f"Atual -> Título: {titulo_atual}, Ano: {ano_atual}, Autor ID: {autor_atual}")

        titulo = view.input_text("Novo título (vazio para manter): ")
        ano = view.input_int("Novo ano (vazio para manter): ", allow_empty=True)

        autores = self.autor_model.listar_autores()
        view.mostrar_lista_autores(autores)

        autor_id = view.input_int("Novo ID de autor (vazio para manter): ", allow_empty=True)

        if titulo == "":
            titulo = titulo_atual
        if ano is None:
            ano = ano_atual
        if autor_id is None:
            autor_id = autor_atual
        else:
            existe = any(a[0] == autor_id for a in autores)
            if not existe:
                view.mostrar_mensagem("Autor inválido.")
                return

        self.model.atualizar_livro(id_livro, titulo, ano, autor_id)
        view.mostrar_mensagem("Livro atualizado com sucesso.")

    def excluir_livro(self, view):
        id_livro = view.input_int("ID do livro a excluir: ")
        if id_livro is None:
            return
        livros = self.model.listar_livros()
        encontrado = None
        for l in livros:
            if l[0] == id_livro:
                encontrado = l
                break
        if not encontrado:
            view.mostrar_mensagem("Livro não encontrado.")
            return
        confirmar = view.input_text(f"Confirma exclusão do livro '{encontrado[1]}'? (s/N): ")
        if confirmar.lower() != 's':
            view.mostrar_mensagem("Operação cancelada.")
            return
        try:
            self.model.excluir_livro(id_livro)
            view.mostrar_mensagem("Livro excluído com sucesso.")
        except Exception as e:
            view.mostrar_mensagem(f"Erro ao excluir livro: {e}")
