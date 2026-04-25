class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.disponivel = True


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                if not livro.disponivel:
                    raise ValueError("Livro já emprestado")
                livro.disponivel = False
                return
        raise ValueError("Livro não encontrado")

    def devolver_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                if livro.disponivel:
                    raise ValueError("Livro já está disponível")
                livro.disponivel = True
                return
        raise ValueError("Livro não encontrado")