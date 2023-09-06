%Bisabuelos_nivel1
padrede('Jose','Luis').
madrede('Maria','Luis').
padrede('Jose','Karla').
madrede('Maria','Karla').





hijode(A,B):- padrede(B,A).
hermanode(A,B):- padrede(C,A), padrede(C,B), A\==B.
tiode(A,B):- hermanode(A,C), padrede(C,B).
abuelode(A,B):- padrede(A,C), padrede(C,B).
bisabuelode(A,B):- padrede(A,C), padrede(C,D), padrede(D,B).
casadocon(A,B):- padrede(A,C), padrede(B,C).
esfeliz(A):- casadocon(A,_).
