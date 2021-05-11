# indication que l'on a besoin de la librairie python "SenseHat"
from sense_hat import SenseHat

# création de l'interface SenseHat pour pouvoir interagir avec lui
# toutes les fonctions du SenseHat sont documentées ici: https://pythonhosted.org/sense-hat/api/
sense = SenseHat()

# Remet toute la matrice LED à blanc.
sense.clear()

# Exécute le code à partir de la ligne 12 jusqu'à ce que l'AstroPi s'arrète
while True:
  # Obtient l'orientation actuelle en degrés en utilisant les axes principaux du SenseHat: tangage, roulis et lacet.
  orientation = sense.get_orientation()

  # Affiche l'orientation dans la fenêtre d'affichage de l'éditeur de code Python
  print(orientation)
