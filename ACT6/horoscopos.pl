horoscopo(aries, 21, 3, 21, 4).
horoscopo(tauro, 21, 4, 21, 5).
horoscopo(geminis, 21, 5, 21, 6).
horoscopo(cancer, 21, 6, 21, 7).
horoscopo(leo, 21, 7, 21, 8).
horoscopo(virgo, 21, 8, 21, 9).
signo(Dia, Mes, Signo) :- 
    horoscopo(Signo, DiaInicio, MesInicio, DiaFin, MesFin),
    (Mes = MesInicio, Dia >= DiaInicio; Mes > MesInicio),
    (Mes = MesFin, Dia =< DiaFin; Mes < MesFin).