import ephem
import time
import math
import picamera

# https://celestrak.com/NORAD/elements/stations.txt
name = "ISS (ZARYA)"
line1 = "1 25544U 98067A   21055.19206382  .00002355  00000-0  50882-4 0  9996"
line2 = "2 25544  51.6440 181.6089 0002935  47.3098  16.8001 15.49001629271086"

iss = ephem.readtle(name, line1, line2)

# cam object allows access to the camera functions
cam = picamera.PiCamera()

# loop forever
while True:
    # calculate the position of the ISS based on the system time
    iss.compute()
    # convert the lat/long from radians to degrees and store in variables
    lat_deg = math.degrees(iss.sublat)
    long_deg = math.degrees(iss.sublong)
    
    # round the lat/long to two decimal places
    lat_deg = round(lat_deg, 2)
    long_deg = round(long_deg, 2)
    
    # show the lat/long in shell
    print(lat_deg, long_deg)
    
    # for text burnt into the image set annotate_text before calling capture
    # the %s in the string will be replaced by the lat/long values
    cam.annotate_text = "LAT: %s / LONG: %s" % (lat_deg, long_deg)    
    
    # take a picture and save it to the desktop with a unique file name
    cam.capture("Desktop/image_%i.jpg" % time.time())
    
    # see also cam.exif_tags
    
    # wait for 10 seconds
    time.sleep(10)
    
