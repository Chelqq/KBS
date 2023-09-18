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
:- discontiguous Ceo_de/2.
Ceo_de('Elon musk','Tim cook').


%Director_gral
:- discontiguous Director_de/2.
Director_de('Tim cook','Barak obama').
Director_de('Tim cook','Joe bezos').
Director_de('Tim cook','Donald trump').
Director_de('Tim cook','Joe biden').
Director_de('Tim cook','Kamala harris').

%Gerente
:- discontiguous Gerente_de/2.
Gerente_de('Jared Kushner','Mark zuckerberg').
Gerente_de('Barak obama','Mark zuckerberg').
Gerente_de('Kamala harris','Mark zuckerberg').
Gerente_de('Mark zuckerberg','Jared Kushner').
Gerente_de('Joe biden','Jared Kushner').
Gerente_de('Joe bezos','Jared Kushner').

%Super
:- discontiguous Supervisor_de/2.
Supervisor_de('Mark zuckerberg','Steve wozniak').
Supervisor_de('Mark zuckerberg','Arvind krisman').
Supervisor_de('Kamala harris','Arvind krisman').
Supervisor_de('Jared Kushner','Steve wozniak').
Supervisor_de('Jared Kushner','Arvind krisman').
Supervisor_de('Kamala harris','Steve wozniak').

%Reglas_de_inferencia
Ceo_de(X, Y) :- Director_de(X, Z), Gerente_de(Z, Y).
Director_de(X, Y) :- Gerente_de(X, Z), Supervisor_de(Z, Y).
Ceo(X, Y) :- Ceo_de(X, Y).

