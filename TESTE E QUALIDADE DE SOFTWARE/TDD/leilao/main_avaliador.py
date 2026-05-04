from avaliador import Avaliador
from usuario import Usuario
from leilao import Leilao
from lance import Lance


joao = Usuario("João")
rita = Usuario("Rita")
jose = Usuario("Jose")
mari = Usuario("Mari")
adam = Usuario("Adam")
vera = Usuario("Vera")
leilao = Leilao("Smart Phone Samsung 32")
leilao.propor(Lance(joao, 300.00))
leilao.propor(Lance(rita, 450.00))
leilao.propor(Lance(jose, 400.00))
leilao.propor(Lance(mari, 150.00))
leilao.propor(Lance(adam, 500.00))
leilao.propor(Lance(vera, 100.00))

leiloeiro = Avaliador()
leiloeiro.avaliar(leilao)
print(f"Maior lance: {leiloeiro.get_maior_lance()}")

leiloeiro.avaliar_tres_maiores(leilao)
for lance in leiloeiro.get_tres_maiores():
    print(f"Lances: {lance.valor}")