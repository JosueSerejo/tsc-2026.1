sexo(denise,feminino).
sexo(fabricia,feminino).
sexo(gabriela,feminino).
sexo(mariano,masculino).
sexo(chico,masculino).

pais(mariano,jonas,lurdes).
pais(denise,jonas,lurdes).
pais(fabricia,aroldo,amanda).
pais(gabriela,jonas,lurdes).
pais(chico,aroldo,amanda).

nao_sabe(mariano).
nao_sabe(denise).

irmaos(X,Y) :- 
    pais(X,Pai,Mae),
    pais(Y,Pai,Mae),
    X \= Y.

nao_sabe_parentesco(X,Y) :-
    irmaos(X,Y),
    nao_sabe(X),
    nao_sabe(Y).