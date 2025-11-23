# main.py
from controllers.autor_controller import AutorController
from controllers.livro_controller import LivroController
import view.view as view

def main():
    autor_ctrl = AutorController()
    livro_ctrl = LivroController()

    try:
        while True:
            opc = view.menu_principal()
            if opc == '1':
                while True:
                    opc_a = view.menu_autor()
                    if opc_a == '1':
                        autor_ctrl.cadastrar_autor(view); view.pausar()
                    elif opc_a == '2':
                        autor_ctrl.listar_autores(view); view.pausar()
                    elif opc_a == '3':
                        autor_ctrl.atualizar_autor(view); view.pausar()
                    elif opc_a == '4':
                        autor_ctrl.excluir_autor(view); view.pausar()
                    elif opc_a == '5':
                        break
                    else:
                        print("\nOpção inválida.")
            elif opc == '2':
                while True:
                    opc_l = view.menu_livro()
                    if opc_l == '1':
                        livro_ctrl.cadastrar_livro(view); view.pausar()
                    elif opc_l == '2':
                        livro_ctrl.listar_livros(view); view.pausar()
                    elif opc_l == '3':
                        livro_ctrl.atualizar_livro(view); view.pausar()
                    elif opc_l == '4':
                        livro_ctrl.excluir_livro(view); view.pausar()
                    elif opc_l == '5':
                        break
                    else:
                        print("Opção inválida.")
            elif opc == '3':
                print("\nEncerrando...")
                break
            else:
                print("\nOpção inválida.")
    except Exception as e:
        print(f"\nErro inesperado: {e}")

if __name__ == "__main__":
    main()