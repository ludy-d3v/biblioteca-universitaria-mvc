# models/autor_model.py
import psycopg2

class AutorModel:
    def __init__(self):
        try:
            self.conexao = psycopg2.connect(
                host="localhost",
                database="biblioteca_db",
                user="postgres",
                password="s3nh4"
            )
        except Exception as e:
            print("\nErro ao conectar ao banco:", e)

    def listar_autores(self):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("SELECT id, nome, nacionalidade FROM autor ORDER BY id;")
            autores = cursor.fetchall()
            cursor.close()
            return autores
        except Exception as e:
            print("\nErro ao listar autores:", e)
            return []

    def inserir_autor(self, nome, nacionalidade):
        try:
            cursor = self.conexao.cursor()
            cursor.execute(
                "INSERT INTO autor (nome, nacionalidade) VALUES (%s, %s);",
                (nome, nacionalidade)
            )
            self.conexao.commit()
            cursor.close()
        except Exception as e:
            print("\nErro ao inserir autor:", e)
            self.conexao.rollback()

    def atualizar_autor(self, id_autor, nome, nacionalidade):
        try:
            cursor = self.conexao.cursor()
            cursor.execute(
                "UPDATE autor SET nome = %s, nacionalidade = %s WHERE id = %s;",
                (nome, nacionalidade, id_autor)
            )
            self.conexao.commit()
            cursor.close()
        except Exception as e:
            print("\nErro ao atualizar autor:", e)
            self.conexao.rollback()

    def excluir_autor(self, id_autor):
        try:
            # com on delete cascade no banco, basta deletar o autor
            cursor = self.conexao.cursor()
            cursor.execute("DELETE FROM autor WHERE id = %s;", (id_autor,))
            self.conexao.commit()
            cursor.close()
        except Exception as e:
            print("\nErro ao excluir autor:", e)
            self.conexao.rollback()