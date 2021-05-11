# indication que l'on a besoin de la librairie python "SenseHat"
from sense_hat import SenseHat

# création de l'interface SenseHat pour pouvoir interagir avec lui
# toutes les fonctions du SenseHat sont documentées ici: https://pythonhosted.org/sense-hat/api/
sense = SenseHat()

# Exécute en boucle le code de la ligne 10 à la ligne 14 jusqu'à ce que l'AstroPi s'arrète
while True:
  # Obtient l'orientation actuelle en degrés en utilisant les axes principaux du SenseHat: tangage, roulis et lacet.
  orientation = sense.get_orientation()

  # Affiche l'orientation dans la fenêtre d'affichage de l'éditeur de code Python
  print(orientation)
