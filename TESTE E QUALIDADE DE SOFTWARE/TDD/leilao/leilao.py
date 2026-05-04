class Leilao:

    def __init__(self, produto):
        self.produto = produto
        self.lances = []
    
    def propor(self, lance):
        if self.lances is None or not self.lances[-1].get_usuario() == lance.get_usuario().get_nome():
            self.lances.append(lance)
    
    def get_produto(self):
        return self.produto
    
    def get_lances(self):
        return self.lances

