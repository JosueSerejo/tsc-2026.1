sexo(ana,feminino).
sexo(maria,feminino).
sexo(claudia,feminino).
sexo(pedro,masculino).
sexo(lucas,masculino).

pais(pedro,jonas,lurdes).
pais(ana,jonas,lurdes).
pais(maria,fabricio,amanda).
pais(claudia,jonas,lurdes).
pais(lucas,fabricio, amanda).

irma(X,Y) :- 
    sexo(X,feminino),
    pais(X,Pai,Mae),
    pais(Y,Pai,Mae),
    X \= Y.