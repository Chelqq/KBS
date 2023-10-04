/*Definición de la regla para calcular la potencia
    pow(X,N, Res).  
    pow(X,5, Res).
    pow(6,N, R).
    */
/* Caso base: Cualquier número elevado a la potencia 0 es 1. */
pow(_, 0, 1).

/* Caso recursivo: Elevar X a la potencia N */
pow(X, N, Res) :-
    N > 0,                  
    N1 is N - 1,            
    pow(X, N1, Temp),       
    Res is X * Temp.  

/* Aseguramos que N sea un número positivo */
/* Reducimos N en 1 en cada llamada recursiva */
/* Llamada recursiva */
/* Calculamos el Resultado */


