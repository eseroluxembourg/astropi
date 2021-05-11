# indication que l'on a besoin de la librairie python "SenseHat"
from sense_hat import SenseHat

# création de l'interface SenseHat pour pouvoir interagir avec lui
# toutes les fonctions du SenseHat sont documentées ici: https://pythonhosted.org/sense-hat/api/
sense = SenseHat()

# Exécute en boucle le code de la ligne 10 à 14 jusqu'à ce que l'AstroPi s'arrète
while True:
  # Récupère les données brutes de l'accéléromètre sur les axes x, y et z.
  acceleration = sense.get_accelerometer_raw()

  # Affiche l'acceleration dans la fenêtre d'affichage de l'éditeur de code Python
  print(acceleration)
