class Leilao:

    def __init__(self, produto):
        self.produto = produto
        self.lances = []
    
    def propor(self, lance):
        if not self.lances or self.lances[-1].get_usuario() != lance.get_usuario():
            self.lances.append(lance)
    
    def get_produto(self):
        return self.produto
    
    def get_lances(self):
        return self.lances

