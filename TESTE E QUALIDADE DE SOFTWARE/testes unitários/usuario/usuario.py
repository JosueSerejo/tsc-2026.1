class Usuario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def eh_maior_de_idade(self):
        return self.idade >= 18
    

    def atualizar_idade(self, nova_idade):
        if nova_idade < 0:
            raise ValueError("Idade inválida")

        if nova_idade != self.idade + 1:
            raise ValueError("Só pode aumentar a idade em 1")

        self.idade = nova_idade