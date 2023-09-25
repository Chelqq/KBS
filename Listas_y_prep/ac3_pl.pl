/*Predicado para calcular el n-ésimo número de Fibonacci*/
fibonacci(0, 0).
fibonacci(1, 1).
fibonacci(N, Resultado) :-
    N > 1,
    N1 is N - 1,
    N2 is N - 2,
    fibonacci(N1, F1),
    fibonacci(N2, F2),
    Resultado is F1 + F2.

/*Predicado para generar la serie de Fibonacci hasta un límite -----> fibo(X).*/

fibo(Limite) :-
    between(0, Limite, N),
    fibonacci(N, Resultado),
    write(Resultado), write(' '),
    fail.