filha(leticia,maria).
filha(maria,josefa).
filha(gabriela,sonia).
filha(sonia,josefa).
filha(juriema,sonia).
filha(eliana,maria).

descendente_direta(X,Y) :-
    filha(X,Y).

descendente_indireta(X,Y) :-
    filha(X,Z),
    (descendente_direta(Z,Y)
    ; descendente_indireta(Z,Y)).