#!/usr/bin/python
# -*- coding:Utf-8 -*-

import random

if __name__ == "__main__":
    print "Type: humanoïde"
    print "Taille:", random.choice(("très petit", "petit", "moyen", "grand", "très grand"))
    print "Graisse:", random.choice(("squelétique", "maigre", "normal", "gros", "très gros", "obèse", "colossale"))
    print "Largueur:", random.choice(("très fin", "fin", "normal", "large", "très large", "ridiculement large"))
    print "Musculature:", random.choice(("inexistante", "faible", "normal", "importante", "très importante"))

    if random.randint(0, 1):
        print "Ornement, type:", random.choice(("poils", "plumes",))
        print "          densité:", random.choice(("très faible", "faible", "normal", "importante", "forte",
                                                     "conséquente",))
        print "          longueur:", random.choice(("très courte (en mm)", "courte (1-2cm)", "normal (2-5cm)", "longue "
                                                    "(5-10cm)", "très longue (10-20cm)", "extrèmement longue (30cm+)"
                                                    "intense",))
        print "          localisation:", random.choice(("dorsale", "humaine", "intégrale", "extrémités", "primate",
                                                        "disparate", "aléatoire", "sur les parties exposés"))
        print "          couleur:", random.choice(("blanche", "beige", "jaune", "mate", "marron", "ocre", "pourpre",
                                                   "caca d'oie", "laiteu", "noirs", "gris", "gris claire", "gris sombre"))
    else:
        print "Ornement: inexistante"

    print "Epiderme, type:", random.choice(("peau", "écailles", "corne", "carapace", ))
    print "          couleur:", random.choice(("blanche", "beige", "jaune", "mate", "marron", "ocre", "pourpre",
                                                   "rose", "caca d'oie", "laiteu", "noirs", "gris", "gris claire",
                                                   "gris sombre"))

# nbr de doigts, bras, jambes
# cornes ou cerfs
# griffes, ongles
# ailes, nombres, taile, plumes/peau/insect
# yeux, nombre, couleur, forme, taille, abscen
# cheveulure
# bouche, dents, bec, abscence
# forme crane
# longueur bras, jambre, avant bras, colonne vetébrale, etc ...

#    print "          couleur:", random.choice(("blanche humaine", "blanche", "beige", "jaune", "jaune asiatique",
#                                               "mate", "orange", "rouge", "arabique", "marron", "ocre", "pourpre",
#                                               "rose", "caca d'oie", "laiteu", "violet", "bleu pale", "bleu", "bleu "
#                                               "foncé", "bleu-vert", "vert pale", "vert foncé", "vert", "noirs", "noirs "
#                                               "humain", "gris", "gris claire", "gris sombre"))
