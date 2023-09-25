cons(a,[b,c]).
/* cons(a,[b,c]).
    cons(x,[b,c]).
    cons(b,[b,c]).
    cons(c,[b,c]).
    cons(a,[b,c]).         */
    
pertenece(a,[a,b,c]).
pertenece(b,[a,b,c]).
pertenece(c,[a,b,c]).

/*  pertenece(a,[a,b,c]).
    pertenece(b,[a,b,c]).
    pertenece(c,[a,b,c]).
    pertenece(x,[a,b,c]).
    */

conc([a,b],[c,d,e]).
/*  conc(L,L2)
    */