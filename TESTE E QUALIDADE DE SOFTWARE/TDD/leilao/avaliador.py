class Avaliador:
	
    def __init__(self):
        self.maior_lance = -10 ** 101    # Um número muito pequeno
        self.menor_lance = 10 ** 101     # Um número muito grande
        self.tres_maiores = []
    		
    def avaliar(self, leilao):
        for lance in leilao.lances:
            if lance.valor > self.maior_lance:
                self.maior_lance = lance.valor
            if lance.valor < self.menor_lance:
                self.menor_lance = lance.valor
    
    def avaliar_tres_maiores(self, leilao):
        self.tres_maiores = sorted(leilao.lances, key=lambda lanc: lanc.valor, reverse=True)[:3]
		
    def get_maior_lance(self):
        return self.maior_lance

    def get_menor_lance(self):
        return self.menor_lance

    def get_tres_maiores(self):
        return self.tres_maiores
	