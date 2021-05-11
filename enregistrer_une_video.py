# indication que l'on a besoin de la librairie python "PiCamera"
from picamera import PiCamera

# indication que l'on a besoin de la librairie python "sleep"
from time import sleep

# création de l'interface PiCamera pour pouvoir interagir avec lui
camera = PiCamera()

# Démarrage de la prévisualisation
camera.start_preview()

# Démmarrage de l'enregistrement de la vidéo vers le bureau d'AstroPi
camera.start_recording('/home/pi/Desktop/video.h264')

# Attendre 5 secondes d'enregistrement
sleep(5)

# Arrêter l'enregistrement
camera.stop_recording()

# Arrêt de la prévisualisation
camera.stop_preview()
