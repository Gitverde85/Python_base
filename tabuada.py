#!/usr/bin/env python3

__Version__="0.1.0"
__author__="Rodrigo"

template_base = """
---Tabuada do 2---

	{operacao}
	
#################
"""

numeros = list(range(1, 11))

# for numero in numeros:
# 	print("Tabuada do:", numero)
# 	for outro_numero in numeros:
# 		print(numero * outro_numero)
# 	print("-----------")

for n1 in numeros:
	for n2 in numeros:
		operacao = f"{n1} x {n2} = {n1 * n2}\n"
		print(operacao)
