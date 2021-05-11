# indication que l'on a besoin de la librairie python "PiCamera"
from picamera import PiCamera

# indication que l'on a besoin de la librairie python "sleep"
from time import sleep

# création de l'interface PiCamera pour pouvoir interagir avec lui
camera = PiCamera()

# Previsualisation de la photo
camera.start_preview()

# Attendre 3 secondes
sleep(3)

# Prendre une photo et la stocker dans le fichier image.jpg sur le bureau de l'AstroPi
camera.capture('/home/pi/Desktop/image.jpg')

# Arrêt de la prévisualisation de la photo
camera.stop_preview()
