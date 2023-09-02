#!/usr/bin/env python3

__Version__="0.1.0"
__author__="Rodrigo"

numeros = list(range(1, 11))

for numero in numeros:
	print("Tabuada do:", numero)
	for outro_numero in numeros:
		print(numero * outro_numero)
	print("-----------")
