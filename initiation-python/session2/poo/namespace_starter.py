# coding: utf-8
import sys
import os

session_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(session_dir)

try:
    from poo import namespace_a, namespace_b
except:
    print("Erreur d'import")
else:
    print('On test les deux namespaces')
    print(namespace_a.a)
    namespace_a.afro_trap()
    print(namespace_b.b)
    namespace_b.afro_trap()

print('===========================')

try:
    from poo.namespace_a import afro_trap
    from poo.namespace_b import afro_trap
    #from module import *
except:
    print("Erreur d'import")
else:
    print('On importe les deux méthodes issues des deux modules')
    afro_trap()
    print('La dernière override la première')

print('===========================')

try:
    from poo.namespace_a import afro_trap
    from poo.namespace_b import afro_trap as afro
except:
    print("Erreur d'import")
else:
    print('On importe les deux méthodes issues des deux modules')
    afro_trap()
    afro()
