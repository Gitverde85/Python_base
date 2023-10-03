#!/usr/bin/env python3
"""view reports of children by activity
print a list of children grouped by room who attend each of the activities
"""
__version__ = "0.1.0"

#Data
sala1 = ["Erick", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erick", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erick", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [("Ingles", aula_ingles),
              ("Musica", aula_musica),
              ("danca", aula_danca),
]


#list students in each activity by room

for nome_atividade, atividade in atividades:

    print(f"Alunos da atividade {nome_atividade}\n")

    atividade_sala1 = []
    atividade_sala2 = []

    for aluno in atividade:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)

    print("sala 1 ", atividade_sala1)
    print("sala 2 ", atividade_sala2)
    print("-" * 30)