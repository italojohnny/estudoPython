#!/usr/python3.5
"""
JSON  (JavaScript Object Notation)
Na biblioteca-padrao há um modulo de suporte json. O formato apresenta muitas
similaridades com YAML e tem o mesmo proposito.
"""
import json
desktop = {'arquitetura': 'pc', 'cpus': 2, 'hds': [520, 270]}
print(json.dumps(desktop))

# json usa a sintaxe do javascript para representar os dados e e suportado em
# varias linguagens.
