# indication que l'on a besoin de la librairie python "SenseHat"
from sense_hat import SenseHat

# création de l'interface SenseHat pour pouvoir interagir avec lui
sense = SenseHat()

# définition des variables qui vont contenir chacune une couleur differente, en mélangeant les couleurs Rouge, Vert et Bleu.
# chaque élément du tableau de 3 valeurs est un nombre qui va de 0 (intensité minimale) à 255 (intensité maximale)
r = [255, 0, 0] # rouge - seul l'élement rouge est mis à la valeur maximale
g = [0, 255, 0] # vert - seul l'élement vert est mis à la valeur maximale
b = [0, 0, 255] # bleu - seul l'élement bleu est mis à la valeur maximale

w = [255, 255, 255] # blanc - quand rouge, vert et bleu sont au maximum, l'addition donne du blanc
e = [0, 0, 0] # vide - aucune couleur n'est activée

# Autres couleurs
o = [255, 127, 0] # orange
y = [255, 255, 0] # jaune
i = [75, 0, 130] # pourpre
v = [159, 0, 255] # violet

# définition du tableau de 8x8 éléments qui correspond à l'écran LED 8x8 du SenseHat
# chaque pixel est illuminé avec une des couleurs prédéfinie ci-dessus
image = [
  e, e, e, e, e, e, e, e,
  e, e, e, r, r, e, e, e,
  e, r, r, o, o, r, r, e,
  r, o, o, y, y, o, o, r,
  o, y, y, g, g, y, y, o,
  y, g, g, b, b, g, g, y,
  b, b, b, i, i, b, b, b,
  b, i, i, v, v, i, i, b,
]

# Nous indiquons au SenseHat d'afficher notre tableau sur l'écran LED
sense.set_pixels(image)
