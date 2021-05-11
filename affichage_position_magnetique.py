# indication que l'on a besoin de la librairie python "SenseHat"
from sense_hat import SenseHat

# création de l'interface SenseHat pour pouvoir interagir avec lui
# toutes les fonctions du SenseHat sont documentées ici: https://pythonhosted.org/sense-hat/api/
sense = SenseHat()

# Remet toute la matrice LED à blanc.
sense.clear()

# Exécute le code à partir de la ligne 12 jusqu'à ce que l'AstroPi s'arrète
while True:
  # Obtient les données brutes du magnétomètre sur les axes x, y et z.
  raw = sense.get_compass_raw()

  # Affiche l'orientation magnétique dans la fenêtre d'affichage de l'éditeur de code Python
  print(raw)
