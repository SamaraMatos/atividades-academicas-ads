import matplotlib.pyplot as plt
from collections import Counter

class Livro:
    def __init__(self, titulo, autor, ano_publicacao, genero):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.genero = genero

livros = []

def cadastrar_livro():
    while True:
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        ano_publicacao = input("Digite o ano de publicação: ")
        genero = input("Digite o gênero do livro: ")
        livro = Livro(titulo, autor, ano_publicacao, genero)
        livros.append(livro)
        print(f"Livro '{titulo}' cadastrado com sucesso!")
        continua = input("Deseja adicionar mais livro? (s/n)")
        if continua.lower() != "s":
            break

def listar_livros():
    if not livros:
        print("Nenhum livro cadastrado ainda.")
    else:
        print("\nLista de livros cadastrados:")
        for i, livro in enumerate(livros, start=1):
            print(f"{i}. {livro.titulo}, {livro.autor}, {livro.ano_publicacao}, {livro.genero}")

def buscar_livro(titulo):
    for livro in livros:
        if livro.titulo.lower() == titulo.lower():
            return livro
    return None

print("Bem-Vindo á Biblioteca Páginas Ocultas")
while True:
    print("\n1. Cadastrar livro")
    print("2. Listar livros")
    print("3. Buscar livro por título")
    print("4. Gerar gráfico de livros por gênero")
    print("5. Sair")
    opcao = input("Escolha uma opção:")

    if opcao == "1":
        cadastrar_livro()

    elif opcao == "2":
        listar_livros()

    elif opcao == "3":
        titulo_busca = input("Digite o título do livro que deseja buscar: ")
        livro_encontrado = buscar_livro(titulo_busca)
        if livro_encontrado:
            print(f"Livro encontrado: {livro_encontrado.titulo} - {livro_encontrado.autor} ({livro_encontrado.ano_publicacao})")
        else:
            print("Livro não encontrado.")

    elif opcao == "4":
        generos = [livro.genero for livro in livros]
        contagem_generos = Counter(generos)
        generos_unicos = list(contagem_generos.keys())
        contagem = list(contagem_generos.values())

        plt.bar(generos_unicos, contagem, color='pink')

        plt.xlabel("Gênero")
        plt.ylabel("Quantidade")
        plt.title("Quantidade de Livros por gênero")
        plt.show()

    elif opcao == "5":
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")