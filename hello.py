#! python3
"""Hello Wold Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.
"""
__version__ = "0.0.1"
__author__ = "dri"

import os

# teste

current_language = os.getenv("LANG", "en_US") [:5]
msg = "Hello, Wolrd!"

if current_language == "pt_BR_":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"



print (msg)
