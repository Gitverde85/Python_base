email_tmpl = """
Ola, %(nome)s
 
Tem interesse em comprar %(produto)s?
Este produto é otimo para resolver %(texto)s
Clique agora no %(link)s
Apenas %(quantidade)s disponiveis.
Preco promocional %(preco).2f
"""

clientes = ["Alessandra", "Rodrigo"]

for cliente in clientes:
     print(email_tmpl % {"nome":cliente, "produto": "Volvo xc60", "texto": "Carro muito bom", "link":"https://volvo.com", "quantidade":"2", "preco":12.30} )