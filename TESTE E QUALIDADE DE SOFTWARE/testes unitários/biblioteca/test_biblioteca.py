import pytest

from biblioteca import Livro, Biblioteca


def test_adicionar_livro():
    biblioteca = Biblioteca()
    livro1 = Livro("HARRY POTTER")

    biblioteca.adicionar_livro(livro1)
    assert len(biblioteca.livros) == 1


def test_adicionar_varios_livro():
    biblioteca = Biblioteca()
    livro1 = Livro("Harry Potter")
    livro2 = Livro("Jogos Vorazes")
    livro3 = Livro("Anne Frank")
    livro4 = Livro("Insurgente")


    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)
    biblioteca.adicionar_livro(livro3)
    biblioteca.adicionar_livro(livro4)

    assert len(biblioteca.livros) == 4



def test_emprestar_livro():
    biblioteca = Biblioteca()
    livro1 = Livro("Harry Potter")

    biblioteca.adicionar_livro(livro1)
    biblioteca.emprestar_livro("Harry Potter")

    assert livro1.disponivel == False


def test_livro_disponivel():
    biblioteca = Biblioteca()
    livro1 = Livro("Harry Potter")
    livro2 = Livro("Jogos Vorazes")

    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)
    biblioteca.emprestar_livro("Harry Potter")

    assert livro2.disponivel == True


def test_devolver_livro():
    biblioteca = Biblioteca()
    livro1 = Livro("Harry Potter")
    livro2 = Livro("Jogos Vorazes")

    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)
    biblioteca.emprestar_livro("Harry Potter")
    biblioteca.emprestar_livro("Jogos Vorazes")
    biblioteca.devolver_livro("Harry Potter")

    assert livro2.disponivel == False


def test_devolver_livro_disponivel():
    biblioteca = Biblioteca()
    livro1 = Livro("Harry Potter")
    livro2 = Livro("Jogos Vorazes")

    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)

    with pytest.raises(ValueError):
        biblioteca.devolver_livro("Harry Potter")

def test_devolver_livro_inexistente():
    biblioteca = Biblioteca()
    livro1 = Livro("Harry Potter")
    livro2 = Livro("Jogos Vorazes")

    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)

    with pytest.raises(ValueError):
        biblioteca.devolver_livro("Divergente")