import ephem
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.basemap import Basemap
import pandas as pd
import os

# stars alt-az
stars = [[45.645, 65.125],
         [50.491, 25.092],
         [19.254, 91.291],
         [28.222, 158.217],
         [73.078, 224.402]]

# places
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

losAngeles = ephem.Observer()
losAngeles.lat = '34.0522'
losAngeles.lon = '118.2437'
losAngeles.elevation = 100
losAngeles.date = '2018/3/30 12:00:00'

chicago = ephem.Observer()
chicago.lat = '41.8781'
chicago.lon = '87.6298'
chicago.elevation = 100
chicago.date = '2018/3/30 12:00:00'

boston = ephem.Observer()
boston.lat = '42.3601'
boston.lon = '71.0589'
boston.elevation = 100
boston.date = '2018/3/30 12:00:00'

seattle = ephem.Observer()
seattle.lat = '47.6062'
seattle.lon = '122.3321'
seattle.elevation = 100
seattle.date = '2018/3/30 12:00:00'

lasVegas = ephem.Observer()
lasVegas.lat = '36.1699'
lasVegas.lon = '115.1398'
lasVegas.elevation = 100
lasVegas.date = '2018/3/30 12:00:00'

greenwich = ephem.Observer()
greenwich.lat = '51.4826'
greenwich.lon = '0.0077'
greenwich.lat = '51.5074'
greenwich.lon = '0.1278'
greenwich.elevation = 100
greenwich.date = '2018/3/30 12:00:00'


def draw_graph(az,alt,place='Mandi',time='12:00'):
    df = pd.DataFrame({'x': alt, 'y': az})
    # split dataframes
    df_plus = df[df.y >= 0]
    df_minus = df[df.y < 0]
    # plot scatter
    fig, ax = plt.subplots()
    ax.scatter(df_plus.x, df_plus.y, label='Above Horizon',marker='*', c='b')
    ax.scatter(df_minus.x, df_minus.y, label='Below Horizon',marker='x', c='r')
    ax.legend()
    ax.autoscale()
    #Add Annotation
    for i, j in zip(df.x, df.y):
        ax.annotate('%s)' % j, xy=(round(i), j), xytext=(
            10, 0), textcoords='offset points')
        ax.annotate('(%s,\n,' % i, xy=(round(i), j))
    #Add Label
    plt.ylabel('Altitude Angle')
    plt.xlabel('Azimuthal Angle')
    plt.title(place + " - " + str(time))
    #Draw x-axis
    kk = ax.get_xlim()
    xx = np.linspace(kk[0], kk[1])
    yy = np.linspace(0, 0)
    plt.plot(xx, yy)

    filename = os.getcwd() + "/astro/" + place + ".png"
    if not os.path.exists(filename):
        with open(filename, 'w'): pass
    plt.savefig(filename)

def main():
    # for s in stars:
    #     print(mandi.radec_of(s[0], s[1]))

    stars_ephem = []
    i = 1
    for s in stars:
        star = ephem.FixedBody()
        star.name = "Star" + str(i)
        i += 1
        (star._ra, star._dec) = mandi.radec_of(s[0], s[1])
        stars_ephem.append(star)
        star.compute()

    places = [["Mandi", mandi],
              ["London", london],
              ["New York", ny],
              ["Los Angeles", losAngeles],
              ["Chicago", chicago],
              ["Boston", boston],
              ["Seattle", seattle],
              ["Las Vegas", lasVegas],
              ["Greenwich", greenwich]]

    mandi.date = '2018/3/30 12:00:00'
    for place in places:
        alt = []
        az = []
        for s in stars_ephem:
            s.compute(place[1])
            alt.append(np.degrees(s.alt))
            az.append(np.degrees(s.az))
            print(s.name, np.degrees(s.alt), np.degrees(s.az), place[0], str(place[1].date))
        draw_graph(alt, az, place[0], place[1].date)

if __name__ == "__main__":
    main()