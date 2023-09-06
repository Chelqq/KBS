% Definición de un árbol binario
arbol_binario(vacio).
arbol_binario(nodo(Izquierda, _, Derecha)) :-
    arbol_binario(Izquierda),
    arbol_binario(Derecha).

% Regla para calcular la altura de un árbol binario
altura_arbol(vacio, 0).
altura_arbol(nodo(Izquierda, _, Derecha), Altura) :-
    altura_arbol(Izquierda, AlturaIzq),
    altura_arbol(Derecha, AlturaDer),
    Altura is max(AlturaIzq, AlturaDer) + 1.