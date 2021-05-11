# indication que l'on a besoin de la librairie python "SenseHat"
from sense_hat import SenseHat

# création de l'interface SenseHat pour pouvoir interagir avec lui
# toutes les fonctions du SenseHat sont documentées ici: https://pythonhosted.org/sense-hat/api/
sense = SenseHat()

# Reinitialisation de l'affichage LED en le remettant à blanc
sense.clear();

# Exécute en boucle le code de la ligne 13 à 32 jusqu'à ce que l'AstroPi s'arrète
while True:
  # Récupère les données brutes de l'accéléromètre sur les axes x, y et z.
  acceleration = sense.get_accelerometer_raw()
  
  # Place la valeur de l'accélération selon l'axe x dans la variable nommée x
  x = acceleration["x"]
  # Place la valeur de l'accélération selon l'axe y dans la variable nommée y
  y = acceleration["y"]
  # Place la valeur de l'accélération selon l'axe z dans la variable nommée z
  z = acceleration["z"]
  
  # Chaque variable est remplacée par sa valeur absolue, pour éliminer les chiffres négatifs.
  x = abs(x)
  y = abs(y)
  z = abs(z)
  
  # Affiche l'acceleration dans la fenêtre d'affichage de l'éditeur de code Python
  print(x, y, z)
  
  # Si la valeur d'une des variables est supérieure à 1, affichage d'un message sur la matrice LED
  if x > 1 or y > 1 or z > 1:
    sense.show_message("Vous vous déplacez vite!", scroll_speed=0.1)
