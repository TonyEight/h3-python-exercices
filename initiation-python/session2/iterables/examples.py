# coding: utf-8
"""
    Les listes en intention
    Un concept assez simple en python mais qui permet de faire
    des choses très puissantes.
"""

# Prenons une liste "start"
start = [1, 2, 3, 4,]
# Ici, on veut afficher 2, 3, 4, 5 à partir de cette liste.
# Pour cela, on ferait assez naturellement la chose suivante :
for n in start:
    print(n + 1)
# Ce qui donne
# 2
# 3
# 4
# 5
# Essayez pour mieux comprendre !

# On veut maintenant modifier start pour avoir 2, 3, 4, 5
# en lieu et place de 1, 2, 3, 4.
# Vérifions le contenu de start
print(start)
# [1, 2, 3, 4]
# OK maintenant essayons de modifier son contenu : on crée une zone
# tampon pour stocker notre calcul.
buff = []
# Puis on procède au calcul :
for n in start:
    buff.append(n + 1)
# On n'oublie surtout pas de réaffecter notre buffer à start pour
# en modifier le contenu.
start = buff
# On vérifie à nouveau le contenu de start
print(start)
# [2, 3, 4, 5]
# Faites le test dans votre interpréteur !

"""
    Mais dans ces deux cas d'usages, on peut faire beaucoup plus simple.
"""

# Reprenons le premier cas.
start = [1, 2, 3, 4,]
# On va directement faire l'affichage de 2, 3, 4, 5 en une ligne de code.
print([n + 1 for n in start])
# [2, 3, 4, 5]
# Magie ! On utilise ici la syntaxe de la liste en intention dont
# la structure est : [ "expression" for "élément" in "itérable" ]
# On notera les crochets et l'ordre des mots-clés.
# Cette syntaxe suivante est une liste en intention :
[n + 1 for n in start]
# On parle aussi de comprehension list (en anglais) ou de
# liste en compréhension (en français).
# Faites des tests avec d'autres exemples et 
# vérifiez ceux présents dans le cours.

# Du coup, il est aisé de régler notre second cas en une ligne en s'appuyant
# à nouveau sur les listes en intention.
print(start)
# [1, 2, 3, 4]
start = [n + 1 for n in start]
print(start)
# [2, 3, 4, 5]

# Dernière astuce : que faire si je souhaite appliquer une condition ou un
# filtre à ma liste en intention ? C'est à dire ne pas prendre naïvement toutes
# les valeurs de ma boucle.
# Traitons cela par l'exemple. Disons que seuls les nombres pairs nous
# intéressent dans une liste de 0 à 20.
start = range(0, 21)
print(start)
start = [n for n in start if n % 2 == 0]
print(start)
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# On notera que le filtre (notre condition) est placé après 
# l'instruction d'itération (la boucle for).
# La syntaxe devient : [ "expression" for "élément" in "itérable" "condition" ]
