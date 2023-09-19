import pytholog as pl

new_kb = pl.KnowledgeBase("TESLA")
new_kb([#CEO
    "ceo_de(Elon musk,Tim cook)",
    #Director general
    "director_de(Tim cook,Barak obama)",
    "director_de(Tim cook,Joe bezos)",
    "director_de(Tim cook,Donald trump)",
    "director_de(Tim cook,Joe biden)",
    "director_de(Tim cook,Kamala harris)",
    #Gerente
    "gerente_de(Jared Kushner,Mark zuckerberg)",
    "gerente_de(Barak obama,Mark zuckerberg)",
    "gerente_de(Kamala harris,Mark zuckerberg)",
    "gerente_de(Mark zuckerberg,Jared Kushner)",
    "gerente_de(Joe biden,Jared Kushner)",
    "gerente_de(Joe bezos,Jared Kushner)",
    #Supervisor
    "supervisor_de(Mark zuckerberg,Steve wozniak)",
    "supervisor_de(Mark zuckerberg,Arvind krisman)",
    "supervisor_de(Kamala harris,Arvind krisman)",
    "supervisor_de(Jared Kushner,Steve wozniak)",
    "supervisor_de(Jared Kushner,Arvind krisman)",
    "supervisor_de(Kamala harris,Steve wozniak)"])

