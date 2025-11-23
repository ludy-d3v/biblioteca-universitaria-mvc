# models/livro_model.py
import psycopg2

class LivroModel:
    def __init__(self):
        try:
            self.conexao = psycopg2.connect(
                host="localhost",
                database="biblioteca_db",
                user="postgres",
                password="minhasenha123"
            )
        except Exception as e:
            print("\nErro ao conectar ao banco:", e)

    def listar_livros(self):
        try:
            cursor = self.conexao.cursor()
            cursor.execute(
                """
                SELECT l.id, l.titulo, l.ano_publicacao, a.nome AS nome_autor
                FROM livro l
                JOIN autor a ON l.autor_id = a.id
                ORDER BY l.id;
                """
            )
            livros = cursor.fetchall()
            cursor.close()
            return livros
        except Exception as e:
            print("\nErro ao listar livros:", e)
            return []

    def inserir_livro(self, titulo, ano, autor_id):
        try:
            cursor = self.conexao.cursor()
            cursor.execute(
                "INSERT INTO livro (titulo, ano_publicacao, autor_id) VALUES (%s, %s, %s);",
                (titulo, ano, autor_id)
            )
            self.conexao.commit()
            cursor.close()
        except Exception as e:
            print("Erro ao inserir livro:", e)
            self.conexao.rollback()

    def atualizar_livro(self, id_livro, titulo, ano, autor_id):
        try:
            cursor = self.conexao.cursor()
            cursor.execute(
                "UPDATE livro SET titulo=%s, ano_publicacao=%s, autor_id=%s WHERE id=%s;",
                (titulo, ano, autor_id, id_livro)
            )
            self.conexao.commit()
            cursor.close()
        except Exception as e:
            print("\nErro ao atualizar livro:", e)
            self.conexao.rollback()

    def excluir_livro(self, id_livro):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("DELETE FROM livro WHERE id = %s;", (id_livro,))
            self.conexao.commit()
            cursor.close()
        except Exception as e:
            print("\nErro ao excluir livro:", e)
            self.conexao.rollback()

    def contar_livros_por_autor(self, autor_id):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("SELECT COUNT(*) FROM livro WHERE autor_id = %s;", (autor_id,))
            qtd = cursor.fetchone()[0]
            cursor.close()
            return qtd
        except Exception as e:
            print("\nErro ao contar livros do autor:", e)
            return 0
        
    def obter_por_id(self, id_livro):
        try:
            cursor = self.conexao.cursor()
            cursor.execute(
                "SELECT id, titulo, ano_publicacao, autor_id FROM livro WHERE id = %s;",
                (id_livro,)
            )
            livro = cursor.fetchone()
            cursor.close()
            return livro
        except Exception as e:
            print("Erro ao obter livro:", e)
            return None