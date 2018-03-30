import ephem
import datetime
import geopy
import matplotlib as mpl
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

stars = [[45.645, 65.125],
         [50.491, 25.092],
         [19.254, 91.291],
         [28.222, 158.217],
         [73.078, 224.402]]

def altaz_to_radec(alt, az):
    print ("hello")

def main():
    mandi = ephem.Observer()
    mandi.lat = '31.7754'
    mandi.lon = '76.9861'
    mandi.elevation = 1000
    mandi.date = '2018/3/30 03:00:00'

    london = ephem.Observer()
    london.lat = '51.5074'
    london.lon = '0.1278'
    london.elevation = 100
    london.date = '2018/3/30 12:00:00'

    ny = ephem.Observer()
    ny.lat = '40.7128'
    ny.lon = '74.006'
    ny.elevation = 100
    ny.date = '2018/3/30 12:00:00'

    for s in stars:
        print(mandi.radec_of(s[0], s[1]))

    stars_ephem = []
    i = 1
    for s in stars:
        star = ephem.FixedBody()
        star.name = "Star" + str(i)
        i += 1
        (star._ra, star._dec) = mandi.radec_of(s[0], s[1])
        stars_ephem.append(star)
        star.compute()

    for s in stars_ephem:
        print (s.ra, s.dec)

    print ("hello\n\n\n")
    for s in stars_ephem:
        s.compute('2018/3/30 12:00:00')

    for s in stars_ephem:
        print (s.ra, s.dec)


    for s in stars_ephem:
        s.compute(london)


    print("hello\n\n\n")

    for s in stars_ephem:
        print (s.ra, s.dec)

    for s in stars_ephem:
        s.compute(ny)


    print("hello\n\n\n")

    for s in stars_ephem:
        print (s.ra, s.dec)

if __name__ == "__main__":
    main()