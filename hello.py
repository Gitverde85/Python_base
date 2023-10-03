#!/usr/bin/env python3
"""
__version__ = "0.1.2"
__autor__ = "Rodrigo MC"

"""
import os

current_language = os.getenv("LANG")[:5]
msg = {
    "pt_BR": "Ola, Mundo!",
    "it_IT": "Ciao, Mondo",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour Monde!",
}


# if current_language == "pt_BR":
#     msg = "Ola, Mundo!"
# elif current_language == "it_IT":
#     msg = "Ciao, Mondo"
# elif current_language == "es_SP":
#     msg = "Hola, Mundo!"
# elif current_language == "fr_FR":
#     msg = "Bonjour Monde!"

print(msg[current_language])