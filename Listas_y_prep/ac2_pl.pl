/*Predicado para calcular el factorial de un número */
factorial(0, 1).
factorial(N, Resultado) :-
    N > 0,
    N1 is N - 1,
    factorial(N1, SubFactorial),
    Resultado is N * SubFactorial.

/*Predicado principal para pedir un número y calcular el factorial */
fact :-
    write('Ingrese un numero no negativo: '),
    read(Numero),
    (   Numero < 0 ->
        write('El factorial no esta definido para numeros negativos.\n');
        factorial(Numero, Factorial),
        write('El factorial de '), write(Numero), write(' es '), write(Factorial), nl
    ).

/*Ejecutar el predicado principal */
%fact.
