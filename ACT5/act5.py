import pytholog as pl

new_kb = pl.KnowledgeBase('TESLA')
new_kb([
    # CEO
    "ceo_de('Elon musk', 'Tim cook')",
    
    # Director general
    "director_de('Tim cook', 'Barak obama')",
    "director_de('Tim cook', 'Joe bezos')",
    "director_de('Tim cook', 'Donald trump')",
    "director_de('Tim cook', 'Joe biden')",
    "director_de('Tim cook', 'Kamala harris')",
    
    # Gerente
    "gerente_de('Jared Kushner', 'Mark zuckerberg')",
    "gerente_de('Barak obama', 'Mark zuckerberg')",
    "gerente_de('Kamala harris', 'Mark zuckerberg')",
    "gerente_de('Mark zuckerberg', 'Jared Kushner')",
    "gerente_de('Joe biden', 'Jared Kushner')",
    "gerente_de('Joe bezos', 'Jared Kushner')",
    
    # Supervisor
    "supervisor_de('Mark zuckerberg', 'Steve wozniak')",
    "supervisor_de('Mark zuckerberg', 'Arvind krisman')",
    "supervisor_de('Kamala harris', 'Arvind krisman')",
    "supervisor_de('Jared Kushner', 'Steve wozniak')",
    "supervisor_de('Jared Kushner', 'Arvind krisman')",
    "supervisor_de('Kamala harris', 'Steve wozniak')"])
    
    # Reglas

    # Define the CEO rule
pl.rule(ceo_de(X, Y), [X == "Elon Musk", Y == "Tim Cook"])

    # Define the Director General rule
pl.rule(director_general(X, Y), [X == "Tim Cook", Y == "Barak Obama"])
pl.rule(director_general(X, Y), [X == "Tim Cook", Y == "Joe Bezos"])
pl.rule(director_general(X, Y), [X == "Tim Cook", Y == "Donald Trump"])
pl.rule(director_general(X, Y), [X == "Tim Cook", Y == "Joe Biden"])
pl.rule(director_general(X, Y), [X == "Tim Cook", Y == "Kamala Harris"])

    # Define the Manager rule
pl.rule(manager(X, Y), [X == "Jared Kushner", Y == "Mark Zuckerberg"])
pl.rule(manager(X, Y), [X == "Barak Obama", Y == "Mark Zuckerberg"])
pl.rule(manager(X, Y), [X == "Kamala Harris", Y == "Mark Zuckerberg"])
pl.rule(manager(X, Y), [X == "Mark Zuckerberg", Y == "Jared Kushner"])
pl.rule(manager(X, Y), [X == "Joe Biden", Y == "Jared Kushner"])
pl.rule(manager(X, Y), [X == "Joe Bezos", Y == "Jared Kushner"])

    # Define the Supervisor rule
pl.rule(supervisor(X, Y), [X == "Mark Zuckerberg", Y == "Steve Wozniak"])
pl.rule(supervisor(X, Y), [X == "Mark Zuckerberg", Y == "Arvind Krisman"])
pl.rule(supervisor(X, Y), [X == "Kamala Harris", Y == "Arvind Krisman"])
pl.rule(supervisor(X, Y), [X == "Jared Kushner", Y == "Steve Wozniak"])
pl.rule(supervisor(X, Y), [X == "Jared Kushner", Y == "Arvind Krisman"])
pl.rule(supervisor(X, Y), [X == "Kamala Harris", Y == "Steve Wozniak"])

print(new_kb.query(pl.Expr("supervisor_de('', 'Mark zuckerberg')")))
