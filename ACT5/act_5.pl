%Hombres
%Ceo_tesla
hombre('Elon musk').
%Director_general
hombre('Tim cook').
%Gerente_de_produccion
hombre('Barak obama').
%Gerente_de_Ventas
hombre('Joe bezos').
%Gerente_de_RH
hombre('Donald trump').
%Gerente_de_Logistica
hombre('Joe biden').
%Supervisor
hombre('Mark zuckerberg').
%Supervisor
hombre('Jared kushner').
%Ingenieros
hombre('Steve wozniak').
hombre('Arvind krisman').
%jefe_de_area
hombre('Hunter biden').

%Mujeres
%jefe_de_area
mujer('Ivanka trump').
%Gerente_de_Mantenimiento
mujer('Kamala harris').

%CEO
:- discontiguous ceo_de/2.
ceo_de('Elon musk','Tim cook').

%Director general
:- discontiguous director_de/2.
director_de('Tim cook','Barak obama').
director_de('Tim cook','Joe bezos').
director_de('Tim cook','Donald trump').
director_de('Tim cook','Joe biden').
director_de('Tim cook','Kamala harris').

%Gerente
:- discontiguous gerente_de/2.
gerente_de('Jared Kushner','Mark zuckerberg').
gerente_de('Barak obama','Mark zuckerberg').
gerente_de('Kamala harris','Mark zuckerberg').
gerente_de('Mark zuckerberg','Jared Kushner').
gerente_de('Joe biden','Jared Kushner').
gerente_de('Joe bezos','Jared Kushner').

%Supervisor
:- discontiguous supervisor_de/2.
supervisor_de('Mark zuckerberg','Steve wozniak').
supervisor_de('Mark zuckerberg','Arvind krisman').
supervisor_de('Kamala harris','Arvind krisman').
supervisor_de('Jared Kushner','Steve wozniak').
supervisor_de('Jared Kushner','Arvind krisman').
supervisor_de('Kamala harris','Steve wozniak').

%Reglas_de_inferencia

es_director(X) :- director_de(X, _), !.
es_gerente(X) :- gerente_de(X, _), !.
es_supervisor(X) :- supervisor_de(X, _), !.
es_ingeniero(X) :- hombre(X), (supervisor_de(_, X) ; gerente_de(_, X)), !.

ceo(X) :- ceo_de(X, _), !.

