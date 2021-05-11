import ephem
import time
import math

# https://celestrak.com/NORAD/elements/stations.txt
name = "ISS (ZARYA)"
line1 = "1 25544U 98067A   21055.19206382  .00002355  00000-0  50882-4 0  9996"
line2 = "2 25544  51.6440 181.6089 0002935  47.3098  16.8001 15.49001629271086"

iss = ephem.readtle(name, line1, line2)

# loop forever
while True:
    # calculate the position of the ISS based on the system time
    iss.compute()
    # convert radians to degrees and show in shell
    print(math.degrees(iss.sublat), math.degrees(iss.sublong))
    
    # calculate solar elevation at the point on ground directly below the ISS
    # create observer object, set location to the computed location of the ISS
    ground = ephem.Observer()
    ground.lat = iss.sublat
    ground.long = iss.sublong
    # this assumes the observer is at sea level which is fine
    
    # sun object allows access to stellar computation functions
    sun = ephem.Sun()
    # pass our ground observer into the sun compute function
    sun.compute(ground)
    # convert the solar elevation angle from radians to degrees
    sun_angle = math.degrees(sun.alt)
    
    # show message in shell if sun above horizon at ground location
    if sun_angle > 0:
        print("Day", sun_angle)
    else:
        print("Night", sun_angle)
    
    #wait for 1 second
    time.sleep(1)
