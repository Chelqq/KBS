%Hombres
hombre('Arthur').
hombre('Bill').
hombre('George').
hombre('Ron').
hombre('Louis').
hombre('Fred').
hombre('Hugo').
hombre('Teddy').
hombre('Percy').
hombre('Harry').
hombre('James').
hombre('Albus').

%Mujeres
mujer('Molly prewett').
mujer('Fleur').
mujer('Angelina').
mujer('Hermione').
mujer('Victoire').
mujer('Dominique').
mujer('Roxanne').
mujer('Rose').
mujer('Audrey').
mujer('Ginny').
mujer('Lucy').
mujer('Molly').
mujer('Lily').


%nivel_1_2
:- discontiguous padrede/2, madrede/2.
padrede('Arthur','Bill').
madrede('Molly prewett','Bill').
padrede('Arthur','Percy').
madrede('Molly prewett','Percy').
padrede('Arthur','George').
madrede('Molly prewett','George').
padrede('Arthur','Ginny').
madrede('Molly prewett','Ginny').
padrede('Arthur','Ron').
madrede('Molly prewett','Ron').

%nivel_2_3
    %Bill
:- discontiguous padrede/2, madrede/2.
padrede('Bill','Victoire').
madrede('Fleur','Victoire').
padrede('Bill','Dominique').
madrede('Fleur','Dominique').
padrede('Bill','Lois').
madrede('Fleur','Loise').
    %Percy
padrede('Percy','Lucy').
madrede('Audrey','Lucy').
padrede('Percy','Molly').
madrede('Audrey','Molly').
    %George
padrede('George','Fred').
madrede('Angelina','Fred').
padrede('George','Roxanne').
madrede('Angelina','Roxanne').
    %Ginny
padrede('Harry','James').
madrede('Ginny','James').
padrede('Harry','Lily').
madrede('Ginny','Lily').
padrede('Harry','Albus').
madrede('Ginny','Albus').
    %Ron
padrede('Ron','Hugo').
madrede('Hermione','Hugo').
padrede('Ron','Rose').
madrede('Hermione','Rose').

%nivel_4
madrede('Victoire','Teddy').


/*Reglas para relaciones de padre y madre*/
padre(Padre, Hijo) :- padrede(Padre, Hijo).
madre(Madre, Hijo) :- madrede(Madre, Hijo).

/*Regla para hermano*/
hermano(Hermano1, Hermano2) :-
    padre(Padre, Hermano1),
    padre(Padre, Hermano2),
    madre(Madre, Hermano1),
    madre(Madre, Hermano2),
    Hermano1 \= Hermano2. /*Evita que alguien sea su propio hermano*/

/*Regla para esposo y esposa*/
esposo(Esposo, Esposa) :- 
    padre(Esposo, Hijo),
    madre(Esposa, Hijo).

esposa(Esposa, Esposo) :- 
    madre(Esposa, Hijo),
    padre(Esposo, Hijo).

/*Regla para suegro y suegra*/
suegro(Suegro, Yerno) :-
    padre(Suegro, Hija),
    esposa(Hija, Yerno).

suegra(Suegra, Yerno) :-
    madre(Suegra, Hija),
    esposa(Hija, Yerno).

/*Regla para yerno y nuera*/
yerno(Yerno, Suegro) :- suegro(Suegro, Yerno).
nuera(Nuera, Suegro) :- suegro(Suegro, Nuera).

/*Regla para cuñado y cuñada*/
cuñado(Cuñado, Persona) :-
    esposo(Cuñado, Hermana),
    hermano(Persona, Hermana).

cuñada(Cuñada, Persona) :-
    esposa(Cuñada, Hermano),
    hermana(Persona, Hermano).

/*Regla para abuelo y abuela*/
abuelo(Abuelo, Nieto) :-
    padre(Padre, Nieto),
    padre(Abuelo, Padre).

abuela(Abuela, Nieto) :-
    madre(Madre, Nieto),
    madre(Abuela, Madre).

/*Regla para nieto y nieta*/
nieto(Nieto, Abuelo) :- abuelo(Abuelo, Nieto).
nieta(Nieta, Abuela) :- abuela(Abuela, Nieta).

/*Regla para tío y tía*/
tio(Tio, Sobrino) :-
    hermano(Tio, Padre),
    padre(Padre, Sobrino).

tia(Tia, Sobrino) :-
    hermana(Tia, Madre),
    madre(Madre, Sobrino).

/*Regla para primo y prima*/
primo(Primo, Persona) :-
    tio(Tio, Persona),
    padre(Tio, Primo).
prima(Prima, Persona) :-
    tia(Tia, Persona),
    madre(Tia, Prima).
