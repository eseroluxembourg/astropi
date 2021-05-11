# Use the astronomy library ephem
import ephem
import time
import math

# these 3 lines are the two-line-element parameters of the ISS orbit
name = "ISS (ZARYA)"
line1 = "1 25544U 98067A   21055.19206382  .00002355  00000-0  50882-4 0  9996"
line2 = "2 25544  51.6440 181.6089 0002935  47.3098  16.8001 15.49001629271086"
# they go out of date with the passage of time but can be updated from
# https://celestrak.com/NORAD/elements/stations.txt

# read the two-line-element parameters to predict the ISS location based on system time
# iss object allows access to the location computation functions
iss = ephem.readtle(name, line1, line2)

# loop forever
while True:
    # calculate the position of the ISS based on the system time
    iss.compute()
    # sublat and sublong are in radians, convert to degrees and show in shell
    print(math.degrees(iss.sublat), math.degrees(iss.sublong))
    # wait for 1 second
    time.sleep(1)
