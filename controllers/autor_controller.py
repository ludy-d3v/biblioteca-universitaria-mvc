# controllers/autor_controller.py
from models.autor_model import AutorModel
from models.livro_model import LivroModel

class AutorController:
    def __init__(self):
        self.model = AutorModel()
        self.livro_model = LivroModel()

    def cadastrar_autor(self, view):
        nome = view.input_text("\nNome do autor: ")
        nacionalidade = view.input_text("Nacionalidade: ")
        if not nome:
            view.mostrar_mensagem("Nome não pode ficar vazio.")
            return
        try:
            self.model.inserir_autor(nome, nacionalidade)
            view.mostrar_mensagem("Autor cadastrado com sucesso.")
        except Exception as e:
            view.mostrar_mensagem(f"\nErro ao cadastrar autor: {e}")

    def listar_autores(self, view):
        autores = self.model.listar_autores()
        view.mostrar_lista_autores(autores)

    def atualizar_autor(self, view):
        id_autor = view.input_int("\nID do autor a atualizar: ")
        if id_autor is None:
            return
        autor = self.model.listar_autores()
        # verifica existência mais direto:
        encontrado = None
        for a in autor:
            if a[0] == id_autor:
                encontrado = a
                break
        if not encontrado:
            view.mostrar_mensagem("\nAutor não encontrado.")
            return
        view.mostrar_mensagem(f"Atual -> Nome: {encontrado[1]}, Nacionalidade: {encontrado[2]}")
        nome = view.input_text("Novo nome (vazio para manter): ")
        nacionalidade = view.input_text("Nova nacionalidade (vazio para manter): ")
        if nome == "": nome = encontrado[1]
        if nacionalidade == "": nacionalidade = encontrado[2]
        try:
            self.model.atualizar_autor(id_autor, nome, nacionalidade)
            view.mostrar_mensagem("\nAutor atualizado com sucesso.")
        except Exception as e:
            view.mostrar_mensagem(f"\nErro ao atualizar autor: {e}")

    def excluir_autor(self, view):
        id_autor = view.input_int("\nID do autor a excluir: ")
        if id_autor is None:
            return

        # busca autor (model.listar_autores retorna lista de tuplas)
        autores = self.model.listar_autores()
        autor = None
        for a in autores:
            if a[0] == id_autor:
                autor = a
                break

        if not autor:
            view.mostrar_mensagem("Autor não encontrado.")
            return

        # contar livros via livro_model
        qtd_livros = self.livro_model.contar_livros_por_autor(id_autor)

        confirmar = view.input_text(
            f"\nAutor: {autor[1]} (Nacionalidade: {autor[2]}). "
            f"\nEste autor possui {qtd_livros} livro(s). \n"
            "Confirma exclusão (os livros também serão removidos)? (s/N): "
        )

        if confirmar.lower() != 's':
            view.mostrar_mensagem("Operação cancelada.")
            return

        try:
            self.model.excluir_autor(id_autor)  # isso chama delete no banco cascade fará o resto
            view.mostrar_mensagem("Autor excluído com sucesso.")
        except Exception as e:
            view.mostrar_mensagem(f"\nErro ao excluir autor: {e}")
            self.model.conexao.rollback()
