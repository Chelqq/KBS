%Hombres
hombre('Jose').
hombre('Luis').
hombre('Luisito').
hombre('Luis angel').
hombre('Carlos').

%Nujeres
mujer('Maria').
mujer('Karla').
mujer('Luisita').
mujer('Elvira').

%Bisabuelos_nivel1
:- discontiguous padrede/2, madrede/2.
padrede('Jose','Luis').
madrede('Maria','Luis').
padrede('Jose','Karla').
madrede('Maria','Karla').

%Abuelos_nivel2
:- discontiguous padrede/2, madrede/2.
padrede('Luis','Luisito').
padrede('Luis','Luisita').
padrede('Luis','Luis angel').
madrede('Karla','Carlos').
madrede('Karla','Juan').

%Padres_nivel3_y_4
:- discontiguous padrede/2, madrede/2.
padrede('Luisito','Andres').
padrede('Luisito','Tomas').
madrede('Luisita', 'Elvira').
padrede('Luis angel','Angel').
padrede('Luis angel','Angelito').
padrede('Carlos','Carlitos').

%Conexiones
bisabuelo(X, Y) :- padrede(X, Z), padrede(Z, Y).
bisabuela(X, Y) :- madrede(X, Z), padrede(Z, Y).
abuelo(X, Y) :- padrede(X, Z), padrede(Z, Y).
abuela(X, Y) :- madrede(X, Z), padrede(Z, Y).
padre(X, Y) :- padrede(X, Y).
madre(X, Y) :- madrede(X, Y).

padre_nivel3_4(X, Y) :- padrede(X, Z), padrede(Z, W), padrede(W, Y).
madre_nivel3_4(X, Y) :- madrede(X, Z), padrede(Z, W), padrede(W, Y).

%Hijo_de
hijo_de(X, Y) :- padrede(Y, X).
hijo_de(X, Y) :- madrede(Y, X).

%Hija_de
hija_de(X, Y) :- padrede(Y, X).
hija_de(X, Y) :- madrede(Y, X).

%Hermano_de
hermano_de(X, Y) :- 
    hombre(X),              % X es un hombre
    padrede(Z, X),          % Z es el padre de X
    padrede(Z, Y),          % Z es también el padre de Y
    X \= Y.                 % X no es igual a Y (para evitar a sí mismo)

%Hermana_de
hermana_de(X, Y) :- 
    mujer(X),               % X es una mujer
    padrede(Z, X),          % Z es el padre de X
    padrede(Z, Y),          % Z es también el padre de Y
    X \= Y.                 % X no es igual a Y

%Tio_de
tio_de(X, Y) :- 
    hombre(X),              % X es un hombre
    hermano_de(X, Z),       % X es hermano de Z
    padrede(Z, Y).          % Z es el padre de Y

%Tia_de
tia_de(X, Y) :- 
    mujer(X),               % X es una mujer
    hermana_de(X, Z),       % X es hermana de Z
    padrede(Z, Y).          % Z es el padre de Y

%Primo_de
primo_de(X, Y) :- 
    hombre(X),              % X es un hombre
    padrede(Z, X),          % Z es el padre de X
    tio_de(Z, Y).           % Z es tío de Y

%Prima_de
prima_de(X, Y) :- 
    mujer(X),               % X es una mujer
    padrede(Z, X),          % Z es el padre de X
    tia_de(Z, Y).           % Z es tía de Y

%Sobrino_de
sobrino_de(X, Y) :- 
    hombre(X),              % X es un hombre
    tio_de(Y, X).           % Y es tío de X

%Sobrina_de
sobrina_de(X, Y) :- 
    mujer(X),               % X es una mujer
    tia_de(Y, X).           % Y es tía de X

%Nieta_de
nieta_de(X, Y) :- 
    mujer(X),               % X es una mujer
    abuela(Y, X).           % Y es abuela de X

%Nieto_de
nieto_de(X, Y) :- 
    hombre(X),              % X es un hombre
    abuelo(Y, X).           % Y es abuelo de X