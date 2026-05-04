class Usuario:

    def __init__(self, nome):
        self.nome = nome
    
    def __eq__(self, usuario):
        # Verifica se o 'usuario' é um Usuario
        if not isinstance(usuario, Usuario):
            return NotImplemented
        # Compara o conteúdo
        return self.nome == usuario.nome
    
    def get_nome(self):
        return self.nome 